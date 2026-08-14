# Erzeugt Regelwerk/Meisterschaften – Talentregister.md aus den kanonisierten
# Meisterschaften-Listen. Nach jeder neu kanonisierten Kategorie erneut laufen lassen:
# neue Datei in SRC eintragen, dann  python talentregister.py
import re, io, os, collections

BASE = r"C:\Users\Syral\OneDrive\Dokumente\Ryssea\Regelwerk"

SRC = [("Meisterschaften – Allgemein.md", "Meisterschaften – Allgemein"),
       ("Meisterschaften – Kampf.md",     "Meisterschaften – Kampf"),
       ("Meisterschaften – Wissen.md",    "Meisterschaften – Wissen"),
       ("Meisterschaften – Handwerk.md",  "Meisterschaften – Handwerk"),
       ("Meisterschaften – Zauberei.md",  "Meisterschaften – Zauberei")]

KATEGORIEN = ["Allgemeine Talente", "Wissenstalente", "Handwerkstalente",
              "Kampftalente", "Magie- und Priestertalente"]
UNIV = "alle Talente"          # Großmeister — gilt für jedes Talent
SONST = "Waffengruppen und Sonderfälle"


def talent_kategorien():
    """Talent -> Kategorie, gelesen aus der Talentübersicht in Talente.md."""
    kat, cur = {}, None
    for ln in io.open(os.path.join(BASE, "Talente.md"), encoding="utf-8"):
        m = re.match(r"^### (.+)", ln)
        if m:
            cur = m.group(1).strip()
            continue
        m = re.match(r"^\| \*\*(.+?)\*\* \|", ln)
        if m and cur:
            kat[m.group(1).strip()] = cur
    return kat


def waffengruppen():
    """Gruppenname -> Talentliste, gelesen aus der Präambel von Meisterschaften – Kampf."""
    g, pfad = {}, os.path.join(BASE, "Meisterschaften – Kampf.md")
    if not os.path.exists(pfad):
        return g
    for ln in io.open(pfad, encoding="utf-8"):
        m = re.match(r"^\| \*\*(.+?)\*\* \| (.+?) \|", ln)
        if not m:
            continue
        name, inhalt = m.group(1).strip(), m.group(2).strip()
        if "·" in inhalt:
            g[name.lower()] = [x.strip() for x in inhalt.split("·")]
    if "nahkampftalente" in g and "fernkampftalente" in g:
        g["alle waffentalente"] = g["nahkampftalente"] + g["fernkampftalente"]
    return g


def kategoriegruppen(kat):
    """'alle Allgemeinen Talente' & Co. — je Kategorie eine Gruppe aus Talente.md."""
    inv = collections.defaultdict(list)
    for talent, k in kat.items():
        inv[k].append(talent)
    g = {}
    for k, talente in inv.items():
        g["alle " + k.lower()] = talente                      # 'alle allgemeine talente'
        g["alle " + k.lower().replace("e talente", "en talente")] = talente  # '... allgemeinen talente'
    return g


def aufloesen(bezeichnung, gruppen):
    """'Nahkampftalente außer Lanzenreiten' -> Liste echter Talente. Sonst None."""
    m = re.match(r"^(.*?)\s+außer\s+(.*)$", bezeichnung)
    basis, ausnahmen = (m.group(1), m.group(2)) if m else (bezeichnung, "")
    talente = gruppen.get(basis.strip().lower())
    if not talente:
        return None
    raus = {x.strip().lower() for x in re.split(r"·| und ", ausnahmen) if x.strip()}
    return [t for t in talente if t.lower() not in raus]


def sammeln():
    reg = collections.defaultdict(lambda: collections.defaultdict(list))
    gruppen = waffengruppen()
    gruppen.update(kategoriegruppen(talent_kategorien()))
    quelle, n = {}, 0
    for fn, link in SRC:
        pfad = os.path.join(BASE, fn)
        if not os.path.exists(pfad):
            continue
        schwelle = None
        for ln in io.open(pfad, encoding="utf-8"):
            m = re.match(r"^## Schwelle (\d+)", ln)
            if m:
                schwelle = int(m.group(1))
                continue
            m = re.match(r"^\*\*(.+?)\*\*\s*·\s*(\w+)\s*·\s*_(.+?)_", ln)
            if not m:
                continue
            n += 1
            roh = m.group(3).strip()
            aufgeloest = aufloesen(roh, gruppen)
            ziele = aufgeloest if aufgeloest else [x.strip() for x in roh.split("·")]
            for t in ziele:
                if m.group(1) not in reg[t][schwelle]:
                    reg[t][schwelle].append(m.group(1))
                quelle[t] = link
    return reg, quelle, n


def block(t, heading, reg, quelle):
    anz = sum(len(v) for v in reg[t].values())
    o = [f"### {heading}\n",
         f"*{anz} Meisterschaft{'en' if anz != 1 else ''}* · [[{quelle[t]}]]\n"]
    for s in sorted(reg[t]):
        o.append(f"**Schwelle {s}** — " + " · ".join(sorted(reg[t][s], key=str.lower)) + "\n")
    o.append("")
    return o


def main():
    reg, quelle, n = sammeln()
    kat = talent_kategorien()
    out = ["---\ntags: [regelwerk, meisterschaft]\ntyp: regelwerk\nstatus: entwurf\npublish: true\n---\n",
           "Meisterschaften – Talentregister\n",
           "Nachschlagehilfe für die Charaktererstellung: Welche Meisterschaften stehen einem Talent offen? "
           "Hier stehen nur Name und Schwelle — die vollständigen Regeltexte in den Kategorie-Listen, je Talent verlinkt. "
           "Gegliedert wie die [[Talente#Talentübersicht|Talentübersicht]]. Zurück zur [[Meisterschaften|Übersicht]].\n",
           "> [!info] Stand\n> Das Register erfasst die **kanonisierten** Kategorien und wächst mit jeder weiteren mit. "
           "Talente ohne Eintrag haben bislang keine Meisterschaften.\n", "---\n"]

    if UNIV in reg:
        out += ["## Talentübergreifend\n"] + block(UNIV, "Für jedes Talent", reg, quelle) + ["---\n"]

    zugeordnet = set()
    for k in KATEGORIEN:
        drin = sorted([t for t in reg if kat.get(t) == k and t != UNIV], key=str.lower)
        if not drin:
            continue
        out.append(f"## {k}\n")
        for t in drin:
            out += block(t, t, reg, quelle)
            zugeordnet.add(t)
        out.append("---\n")

    rest = sorted([t for t in reg if t not in zugeordnet and t != UNIV], key=str.lower)
    if rest:
        out.append(f"## {SONST}\n")
        out.append("Kopfzeilen, die auf eine Gruppe zielen statt auf ein einzelnes Talent. "
                   "Die Waffengruppen sind in [[Meisterschaften – Kampf#Waffengruppen|Meisterschaften – Kampf]] "
                   "definiert; *alle Magieklassen* meint die Klassen aus [[Magieklassen]] und bleibt so lange "
                   "ungeteilt, bis [[Talente]] die Magie- und Priestertalente führt.\n")
        for t in rest:
            out += block(t, t, reg, quelle)

    io.open(os.path.join(BASE, "Meisterschaften – Talentregister.md"), "w",
            encoding="utf-8").write("\n".join(out))
    nennungen = sum(sum(len(v) for v in d.values()) for d in reg.values())
    print(f"{n} Einträge · {len(reg)} Abschnitte · {nennungen} Nennungen · "
          f"{len(rest)} in „{SONST}\"")


main()
