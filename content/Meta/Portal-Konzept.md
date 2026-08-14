---
tags: [meta]
---

# Portal-Konzept (Ryssea-Website)

Arbeitsdokument für die öffentliche Ryssea-Website („das Portal"). Hält Vision, Design-System, Architektur und Fahrplan fest, damit jederzeit — auch in einer neuen Session — sauber weitergearbeitet werden kann.

> [!info] Stand
> Konzept-Phase. Es existieren mehrere Optik-Mockups (siehe [[#Was schon existiert]]). Noch keine echte Umsetzung. Reihenfolge bewusst: erst Lore & Regeln reifen lassen, dann bauen.

---

## 1. Vision & Zweck

Das Portal ist **kein zweites Wiki**, sondern drei Dinge zugleich:
- **Schaufenster** — atmosphärischer Einstieg in die Welt.
- **Lebendige Referenz** — kuratierte Seiten zu Welt, Splittern, Göttern, Regeln.
- **Werkzeuge** — Nebelkarte, Kampagnen-Chroniken und der Heldengenerator.

**Drei Türen (Publika):** Neugierige (Atmosphäre, große Haken), Spieler (Kampagnen, Regeln, Tool), Spielleiter (Tiefe + GM-Wissen).
**Spoiler-Ebenen als Kernprinzip** — Spieler-/SL-Sicht umschaltbar; GM-Wissen bleibt eingeklappt (die Vault-Policy `gm-geheim` / GM-Callouts trägt das schon).

## 2. Website ↔ Wiki

**Ansatz: ergänzen.** Website = Schaufenster + Tools, Wiki = tiefe Referenz. Aber **beide sollen ein gemeinsames Gesicht** haben.
- **Weg A:** Quartz-Wiki mit dem Zwielicht-Design neu themen. Schnell, aber innerhalb der Quartz-Grenzen.
- **Weg B (✅ entschieden, 2026-08-02):** *Ein* Framework (**Next.js**), das den Vault-Inhalt als Wiki rendert und die kuratierten Seiten + Tools daneben — alles aus **einer Quelle**, ein Design. Löst das Quartz-Wiki (wiki.ryssea.de) ab.
- **Framework-Entscheidung: Next.js statt Astro.** Ausschlaggebend: (1) Die GM/Spieler-Spoiler-Ebenen sollen *echt geschützt* sein — serverseitiges Rechtesystem mit Login, GM-Inhalte werden an Spieler gar nicht erst ausgeliefert. (2) Das Heldentool braucht ohnehin Accounts + Datenbank. (3) „Ein Stack, drei Ernten": Login/Rechtesystem (Better Auth + `sichtbarkeit:`-Feld), Drizzle/Neon, Markdown-Pipeline und Vercel-Deploy existieren als Blaupause im Hundetraining-Portal (`C:\Users\Syral\dev\hundetraining-portal`) und im Wissensportal (`C:\Users\Syral\dev\wissensportal`) und werden wiederverwendet.

## 3. Design-System

**Weltidentität = das Zwielicht:** dunkler Grund, **Amethyst + Gold** als Akzente, das **Zehnstern-Wappen** & die **Elementrunen** als Motive, Nebel/Partikel als Atmosphäre. Serif-Display (Palatino-Stil) + klarer System-Sans. **„Ryssea" nie trennen** (kein „Rys·sea").

**Farbsystem in 3 Ebenen** (greift ineinander):
1. **Portal (Zwielicht)** — Nav, Footer, Grundgerüst, überall gleich → hält alles zusammen.
2. **Splitter (Grundstimmung)** — jeder Splitter *eine* übergreifende Farbwelt aus seinem Gesamtcharakter (z. B. Baryia = warm, sandstein-golden). Die Splitter-Seite ist der ruhige Hub.
3. **Reich/Region (Akzent)** — jedes Reich seine eigene Farbe + eigene Unterseite mit vollem Skin.

**Wichtig:** Splitter ≠ Element. Splitter sind **gerettete Fragmente** aus alten Zyklen; ein Elementarlord residiert nur auf *manchen* → dort ein **◆-Heiligtum-Merkmal**. Reich-Unterseiten nutzen **eine geteilte Vorlage, nur die „Haut" (Farben + Symbol) wechselt** (Pharaonenreich = Gold/Lapis + Aton-Sonne; Panthaura = Grün/Schwarz + Panther).

## 4. Informationsarchitektur (Sitemap)

```
Start            → Welt-Einführung, Wappen-Hero, Wege in alle Bereiche
Die Welt         → Kosmologie · Völker · Götter · Magie · Geschichte · Artefakte
  └ Splitter     → je eine Seite (Baryia-Stil), Reiche/Regionen als Unterseiten
  └ Nebelkarte   → interaktive Karte der treibenden Splitter (HERZSTÜCK)
Regelwerk        → Kapitel · Kompendien · Werkzeuge (siehe Abschnitt 6)
Kampagnen        → Sethos Gang · Nebelkinder · Team Synfathia (Storyline + Helden)
Heldentool       → interaktiver Charaktergenerator
```
Zusätzliche Motive: **Nebelkarte** als zentrale Atlas-Navigation; das **Wappen als Navigations-Element** (Element anklicken → dessen Bereich).

## 5. Seiten-Typen (Web-Templates)

Jeder Vault-Notiz-Typ bekommt **ein** Web-Template (sein optischer Zwilling). Die Taxonomie ist im Vault schon gemacht (`Meta/Templates/`, [[Meta/Tags und Typen]]). ~12–15 Templates decken das ganze Wiki ab — einmal bauen, hunderte Notizen rendern durch.

| Web-Template | Vault-Typ |
|---|---|
| Übersicht (MOC) | die „X von Ryssea"-Hubs |
| Splitter (+ Nebelkarte) | splitter |
| Ort / Stadt / Region | ort, stadt, region … |
| Volk · Kultur · Gott | volk / kultur / gott |
| Fraktion / Reich | fraktion (reich, orden …) |
| NPC · Held | npc / spielercharakter |
| Ereignis (Timeline) | ereignis |
| Artikel (Konzept) | kosmologie / magie |
| Artefakt · Kreatur · Sprache | artefakt / kreatur / sprache |
| Kampagne · Chronik · Plot | kampagne / spieltag / plot |

Die „Skins" (Element-/Reich-Akzente) sind eine Schicht obendrauf, gesteuert vom Frontmatter (`typ`, `element`, `zyklus`, `splitter` …).

## 6. Regel-Präsentation

Regeln = **Nachschlagen**, nicht Schmökern. Drei Ebenen:
1. **Regelkapitel** (Prosa + Tabellen) — erklären *wie* etwas funktioniert. Mit **Beispiel-Boxen**, Querverweisen, Quick-Reference. Gruppen wie in [[Regelwerk von Ryssea]]: Grundlagen · Charaktererstellung · Magie · Kampf · Fortschritt · Optional/SL.
2. **Kompendien** (durchsuchbare Datentabellen) — die großen Listen: Grimoire (Zauber), **Meisterschaften (524)**, Talente, Vor-/Nachteile (239), Waffen, Rüstungen (70). Filter + Suche statt Endlos-Scroll.
3. **Werkzeuge** — Probe-Würfler, Kostenrechner, und der **Heldengenerator**.

**Kern-Hebel:** Kompendien + Werkzeuge + Heldentool lesen **dieselben strukturierten Daten**. Eine Quelle → Nachschlagewerk *und* Tool. → starkes Argument für Weg B.

## 7. Heldentool (letzter, größter Baustein)

Interaktiver 10-Schritte-Generator (Rasse → Kultur → Abstammung → Ausbildung → Eigenschaften → Element/Schicksalsgabe → abgeleitete Werte → Bogen). Muss am Ende **Charakterbögen als PDF ausgeben** *und* Helden **steigerbar** speichern (gespeicherte Chars mit AP weiterentwickeln). Datenquelle: `Anhänge/Ryssea_Tool_25.0.7.xlsx` (Rechenkern) + Regelwerk-Notizen.

## 8. Datenmodell — bewusst später

- Das **Schema** (Felder je Liste) existiert de-facto schon als **Spalten im `Ryssea_Tool.xlsx`**.
- **Reihenfolge:** erst die **Regeln fertig** (Zauber, Meisterschaften etc.), *dann* Felder festzurren, *dann* Pipeline (xlsx → Daten) + Kompendien + Tool. Kein Datenmodell auf Treibsand.
- Sobald es soweit ist: xlsx-Spalten je Blatt auslesen → als Schema festhalten.

## 9. Technische Basis

- **Next.js** (✅ entschieden, siehe [[#2. Website ↔ Wiki]]) — rendert die Vault-Notizen → **Vault = eine Quelle** für Website *und* Wiki. Öffentliche Seiten statisch generiert (schnell, SEO), geschützte Inhalte + Werkzeuge serverseitig mit Login/Rechtesystem. Stack wie Wissensportal & Hundetraining-Portal: Next.js + TypeScript + Tailwind, Better Auth, Drizzle + Neon, Deploy auf Vercel.
- Für reine Optik-Mockups: self-contained HTML, **keine CDN-Fonts** (Artifact-CSP) → System-Serifen oder Data-URI. Fotos an SVG-Platzhalter-Stellen später einsetzen.

## 10. Fahrplan (Etappen)

1. **Fundament** — Design-System festzurren · Splitter-Vorlage (Element-Skin) · Start/Welt-Intro.
2. **Inhalt** — weitere Splitter · Welt-Übersichten · Kampagnen-Seiten.
3. **Vereinen** — Wiki-Weg (A/B) entscheiden · Regel-Übersicht + Links · live schalten.
4. **Werkzeuge** — xlsx-Schema · Kompendien · Heldentool.

## Was schon existiert

**Echte Dateien** in `Dokumente\Ryssea-Website\`:
- `Wappen von Ryssea.html` — animiertes Zehnstern-Wappen (robust, „Bewegung"-Schalter)
- `Regelwerk (Konzept).html` — Regel-Präsentation (Probe-Würfler, filterbares Kompendium)

**Assets** in `Anhänge/`: `Wappen von Ryssea.svg` (+ `(animiert).svg`), `Runen/` (12 Element-Runen-SVGs).

**Nur als claude.ai-Artifacts** (frühere Mockups, keine lokalen Dateien mehr): Landing-Startseite · Portal-Konzept · Portal-Brainstorm (mit Nebelkarte) · Baryia-Regionen-Farbkonzept · zwei Reich-Skins (Pharaonenreich/Panthaura) · Helden Fenvarion & Sethos · Elementschrift/Runen-Werkstätten.

## Offene Entscheidungen / nächste Schritte

- ~~Wiki-Weg A vs. B~~ — ✅ entschieden (2026-08-02): **Weg B mit Next.js** (echter GM-Schutz, Heldentool braucht Backend, Stack-Wiederverwendung).
- **Layout-Feinschliff** — Ausrichtung *innerhalb* der Seiten sitzt noch nicht; Display-Schrift & Farbnuancen justieren; Splitter optisch „aufhübschen" (Symbole/Motive pro Splitter).
- **Lore-Lücken schließen** (Voraussetzung für gute Seiten): Baryia vs. **Barya'Aches** (Schreibweise vereinheitlichen) · **Nebeltor-Verbindungen** definieren · **Elementarlord-Zuordnung** (nur 3/10 ausgearbeitet) · **Geschichte/Timeline** ist leer (Rahmen für die Zyklen).
- **Regeln fertigstellen** → dann Datenmodell → dann Kompendien/Tool.

## Siehe auch
- [[Regelwerk von Ryssea]] · [[Die Elementschrift]] · [[Atlas von Ryssea]] · [[Meta/Aufgaben]] · [[Meta/Tags und Typen]]
