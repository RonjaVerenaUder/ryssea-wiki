---
tags: [regelwerk, kampf]
typ: regelwerk
status: fertig
publish: true
quelle: Regeldesign 2026-08 (System) + Notion-Export/Ryssea_Tool_25.0.7 (Werte)
---

# Rüstungen

Rüstungen schützen im [[Kampfregeln|Kampf]], indem sie **Schaden schlucken** — anders als Schilde, die Angriffe *abwehren*. Der Schutz ist an **Trefferzonen** gebunden: Jede Rüstung deckt nur die Körperteile, die sie tatsächlich bedeckt. Bezahlt wird das mit **Belastung** — der Kämpfer wird unbeweglicher und träger.

> [!abstract] Kennwerte
> **RS** = Rüstschutz (Schadensreduktion), **pro Trefferzone** eingetragen · **Ø RS** = gewichteter Schnitt-RS (optional, für schnelles Spiel) · **BE** = Behinderung (Gesamtwert) · **TZ** = Tick-Zuschlag (Gesamtwert)

---

## Schadensreduktion (RS) — wie Schutz wirkt

Trifft ein Angriff, zählt der RS **der getroffenen Zone**. Ablauf pro Treffer:

1. Die Waffe würfelt ihre **TP** (inkl. *Scharf*, *Wuchtig*, Erfolgs-Boni).
2. Die **Trefferzone** wird bestimmt (siehe unten) → deren RS ist maßgeblich.
3. **Durchdringend (X)** der Waffe senkt diesen RS für den Treffer um X.
4. Der Rest-RS wird vom Schaden abgezogen — was übrig bleibt, trifft die **LeP**.

> *Beispiel:* Kettenhemd, Brust-RS **4**. Ein Säbel trifft die Brust (8 Schaden, *Durchdringend 1*) → RS zählt als 3 → **5 Schaden** kommen durch. Träfe derselbe Hieb den ungeschützten Arm (RS 0), kämen alle 8 durch.

Die Rüstungs-Merkmale greifen hier automatisch: **Stabil** ignoriert Durchdringung komplett, **Wattiert** halbiert den *Wuchtangriff*-Bonus, **Gehärtet** gibt +1 RS (bei +1 TZ).

---

## Trefferzonen

Die **7 Zonen**: Kopf · Brust · Bauch · Rücken · li. Arm · re. Arm · Beine.

**Zonenbestimmung ohne Extra-Wurf:** Der **W10, den der Angreifer ohnehin für den Ergebniswert wirft** (siehe [[Würfelsystem & Proben]]), liest zugleich die Trefferzone ab:

| W10 | Zone | ≈ Anteil |
|---|---|---|
| 1 | Rücken | 10 % |
| 2–3 | Brust | 20 % |
| 4–5 | Bauch | 20 % |
| 6–7 | Beine | 20 % |
| 8 | li. Arm | 10 % |
| 9 | re. Arm | 10 % |
| 10 | Kopf | 10 % |

So fällt die Zone als Nebenprodukt des Angriffs ab — keine zusätzliche Würfelaktion. Die **10** (höchster Wurf) trifft den Kopf, die **1** den Rücken.

**Gezielter Schlag** (Manöver): Wer eine bestimmte Zone treffen will — etwa die ungeschützten Beine —, gibt **Erfolge** aus und wählt die Zone selbst, statt sie dem W10 zu überlassen.

---

## Belastung

Der Preis des Schutzes, zwei getrennte Achsen:

- **Behinderung (BE)** — Malus in Höhe der BE auf körperbetonte Proben (Akrobatik, Klettern, Schwimmen, Heimlichkeit) und auf die reflexbasierte **passive Verteidigung / Ausweichen**. Siehe [[Abgeleitete Werte]]. BE kann **Dezimalstellen** haben — Teilrüstungen tragen nur anteilig bei. Die BE aller getragenen Teile werden **summiert**; der wirksame Malus ist die **auf ,5 aufgerundete** Gesamt-BE (Rundung wie beim Grundwert in [[Würfelsystem & Proben]]).
  Zusätzlich senkt die Gesamt-BE die **[[Abgeleitete Werte|Geschwindigkeit]] um 1 Punkt je volle 6 Punkte** (nie unter 1). In diese Gesamt-BE zählt auch die Behinderung aus **[[Traglast]]** hinein — der Vorteil *Kompakt* setzt sie für die Geschwindigkeit um 6 Punkte niedriger an und gibt so genau einen Punkt zurück.
- **Tick-Zuschlag (TZ)** — jede Handlung im Kampf kostet **+TZ Ticks** auf der Tickleiste. Schwere Rüstung lässt den Träger seltener agieren. Siehe [[Kampfregeln]].

Zwei Achsen, weil Rüstung „unbeweglich" und „träge" getrennt sein können — die Merkmale *Wattiert* (erhöht beide) und *Standfestigkeit* (wahlweise eine) setzen das voraus.

---

## Rüstungen kombinieren

Mehrere Teile lassen sich tragen (Kettenhemd + Stahlarmschienen, oder Polsterung unter Kette unter Platte):

- **RS pro Zone:** Die RS aller Teile, die dieselbe Zone bedecken, **addieren sich** — Lagen stapeln also ihren Schutz (Gambeson + Kette + Platte auf der Brust ergeben zusammen).
- **BE und TZ:** Die Gesamtwerte der Teile **addieren** sich ebenfalls.

> [!tip] Sinnvoll layern
> Nur Teile, die physisch übereinander passen, lassen sich kombinieren (nicht zwei Plattenpanzer übereinander). Im Zweifel entscheidet die Spielleitung — der steigende BE/TZ-Preis begrenzt exzessives Stapeln von selbst.

**Voraussetzung (Mindest-KK):** Wie bei Waffen. Unterschreitet der Träger die Mindest-KK einer Rüstung, fällt **+1 BE** obendrauf. Die Mindest-KK ist aus dem Rüstungsgewicht abgeleitet — leichte Rüstungen und alle Zusatzstücke *(Z)* haben keine, schwere skalieren stufenweise bis **KK 6** (Turnierpanzer).

---

## Rüstungs-Merkmale

Die relevanten Merkmale sind gemeinsam mit den Waffenmerkmalen in [[Waffen#Waffenmerkmale]] definiert: **Gehärtet**, **Primitiv**, **Stabil**, **Standfestigkeit**, **Wattiert** (sowie die Schild-Merkmale *Deckung*, *Dornen*, *Schildwall*).

> [!important] Merkmal-Effekt ohne Doppelkosten
> Bei Rüstungen zählt vom Merkmal nur der **Effekt** — die BE/TZ-Aufschläge aus der Merkmal-Definition sind in den Werten der jeweiligen Rüstung **bereits enthalten** (die Polsterung *ist* ja der Grund für das hohe BE) und werden nicht erneut addiert.

**Zuordnung in dieser Liste:**
- **Wattiert** (halbiert den *Wuchtangriff*-Bonus) → gepolsterte Tuch- und Kleidungsrüstungen
- **Stabil** (ignoriert Durchdringung komplett) → starre Metallplatte (Plattenrüstungen; nicht Kettengeflecht oder Lamellar)
- **Standfestigkeit** (KW +3 gegen Umwerfen/Positionsänderung) → die schwersten Rüstungen (TZ ≥ 4)
- **Primitiv** (*Nachteil*: volle Schaden auch von primitiven Waffen) → krude Naturmaterialien (Krötenhaut, Streifenschurz, Beinschuppen, Hartholz)
- **Gehärtet** (+1 RS) → einzelnen Meisterstücken bei Bedarf, nicht Teil dieser Standard-Zuordnung

---

## Rüstungsliste

> [!note]- Importiert aus dem Char-Tool
> Zonen-RS, **Ø RS**, **BE** und **TZ** stammen aus der Rüstungsliste (Char-Tool). DSA/Aventurien-Herkunftsnamen wurden Ryssea-konform umbenannt. **Voraussetzung** (Mindest-KK) aus dem Rüstungsgewicht abgeleitet — Zusatzrüstungen *(Z)* ohne Mindest-KK. **Merkmale** nach Material/Kategorie zugeordnet (Erklärung im Abschnitt *Rüstungs-Merkmale*). *(Z)* = Zusatzrüstung (kombinierbares Teilstück).

### Kleidung

| Rüstung | Kopf | Brust | Bauch | Rücken | li. Arm | re. Arm | Beine | Ø RS | BE | TZ | Voraussetzung | Merkmale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anorak | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 4 | 2 | KK 2 | Wattiert |
| Dicke Kleidung | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0,9 | 0,9 | 0 | — | Wattiert |
| Fellumhang/Fuhrmannsmantel (Z) | 0 | 1 | 0 | 2 | 1 | 1 | 1 | 0,9 | 0,9 | 0 | — | — |
| Hohe Stiefel (Z) | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0,2 | 0,2 | 0 | — | — |
| Lederhose (Z) | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0,4 | 0,4 | 0 | — | — |
| Lederweste / Pelzweste | 0 | 1 | 1 | 1 | 0 | 0 | 0–1 | 0,6–0,8 | 0,6–0,8 | 0 | — | — |

### Tuchrüstungen

| Rüstung | Kopf | Brust | Bauch | Rücken | li. Arm | re. Arm | Beine | Ø RS | BE | TZ | Voraussetzung | Merkmale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gambeson | 0 | 2 | 2 | 2 | 1 | 1 | 1 | 1,5 | 1,5 | 1 | — | Wattiert |
| Mattenrücken | 1 | 1 | 0 | 3 | 0 | 0 | 0 | 0,9 | 0,9 | 0 | — | Wattiert |
| Tuchrüstung | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 1,2 | 1,2 | 1 | — | Wattiert |
| Unterzeug mit Kettenteilen | 0 | 2 | 1 | 2 | 2 | 2 | 1 | 1,4 | 1,4 | 1 | KK 2 | Wattiert |
| Wattierte Kappe (Z) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0,1 | 0,1 | 0 | — | Wattiert |
| Wattiertes Unterzeug | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0,9 | 0,9 | 0 | — | Wattiert |

### Lederrüstungen

| Rüstung | Kopf | Brust | Bauch | Rücken | li. Arm | re. Arm | Beine | Ø RS | BE | TZ | Voraussetzung | Merkmale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Armschienen, Leder (Z) | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0,1 | 0,1 | 0 | — | — |
| Beinschienen, Leder (Z) | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0,2 | 0,2 | 0 | — | — |
| Brustplatte, Leder | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0,6 | 0,6 | 0 | — | — |
| Echsenlederrüstung | 0 | 3 | 2 | 2 | 0 | 0 | 1 | 1,6 | 0,6 | 0 | — | — |
| Krötenhaut | 0 | 3 | 2 | 2 | 1 | 1 | 0 | 1,5 | 0,5 | 0 | KK 2 | Primitiv |
| Lederharnisch | 0 | 3 | 3 | 3 | 0 | 0 | 0 | 1,8 | 1,8 | 1 | KK 2 | — |
| Lederhelm (Z) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0,2 | 0,2 | 0 | — | — |
| Lederhelm, verstärkt (Z) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0,3 | 0,3 | 0 | — | — |
| Streifenschurz (Z) | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0,8 | 0,4 | 0 | — | Primitiv |

### Exotische Materialien

| Rüstung | Kopf | Brust | Bauch | Rücken | li. Arm | re. Arm | Beine | Ø RS | BE | TZ | Voraussetzung | Merkmale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beinschuppenpanzer | 0 | 4 | 4 | 4 | 2 | 2 | 2 | 3 | 2 | 2 | KK 3 | Primitiv |
| suironischer Hartholzharnisch | 0 | 4 | 4 | 4 | 1 | 1 | 1 | 1,7 | 1,7 | 1 | KK 3 | Primitiv |

### Kette/Schuppe

| Rüstung | Kopf | Brust | Bauch | Rücken | li. Arm | re. Arm | Beine | Ø RS | BE | TZ | Voraussetzung | Merkmale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Brigantina | 0 | 5 | 4 | 4 | 2 | 2 | 0 | 2,8 | 2,8 | 2 | KK 3 | — |
| Eisenmantel | 0 | 5 | 2 | 5 | 2 | 2 | 2 | 3,6 | 2,6 | 3 | KK 3 | — |
| Fünflagenharnisch | 0 | 5 | 4 | 5 | 0 | 0 | 1 | 3 | 3 | 3 | KK 3 | — |
| Kettenbeinlinge, Paar (Z) | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0,8 | 0,8 | 0 | — | — |
| Kettenhandschuhe, Paar (Z) | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0,1 | 0,1 | 0 | — | — |
| Kettenhaube (Z) | 3 | 1 | 0 | 1 | 0 | 0 | 0 | 0,7 | 0,7 | 0 | — | — |
| Kettenhaube mit Gesichtsschutz (Z) | 4 | 1 | 0 | 1 | 0 | 0 | 0 | 0,8 | 0,8 | 0 | — | — |
| Kettenhemd, lang | 0 | 4 | 4 | 4 | 3 | 3 | 2 | 3,1 | 2,1 | 2 | KK 4 | — |
| Kettenhemd, ½ Arm | 0 | 4 | 4 | 4 | 2 | 2 | 1 | 2,8 | 1,8 | 1 | KK 3 | — |
| Kettenkragen (Z) | 2 | 1 | 0 | 1 | 0 | 0 | 0 | 0,6 | 0,3 | 0 | — | — |
| Kettenmantel | 0 | 4 | 4 | 4 | 3 | 3 | 3 | 3,3 | 2,3 | 2 | KK 4 | — |
| Kettenweste | 0 | 4 | 4 | 4 | 0 | 0 | 0 | 2,4 | 1,4 | 1 | KK 2 | — |
| Löwenmähne (Z) | 2 | 2 | 0 | 2 | 1 | 1 | 0 | 1,1 | 0,55 | 0 | — | — |
| parsianischer Ringmantel | 0 | 3 | 3 | 3 | 2 | 2 | 2 | 2,4 | 1,4 | 1 | KK 4 | — |
| Ringelpanzer | 0 | 4 | 4 | 4 | 3 | 3 | 1 | 2,9 | 1,9 | 2 | KK 3 | — |
| Schuppenpanzer | 0 | 5 | 5 | 5 | 3 | 3 | 3 | 3,9 | 3,9 | 4 | KK 4 | Standfestigkeit |
| Schuppenpanzer, lang | 0 | 5 | 5 | 5 | 3 | 3 | 4 | 4,1 | 4,1 | 4 | KK 5 | Standfestigkeit |
| Spiegelpanzer | 0 | 5 | 5 | 5 | 3 | 3 | 2 | 3,7 | 2,7 | 3 | KK 4 | — |

### Plattenrüstungen

| Rüstung | Kopf | Brust | Bauch | Rücken | li. Arm | re. Arm | Beine | Ø RS | BE | TZ | Voraussetzung | Merkmale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Armschienen, Bronze (Z) | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0,2 | 0,2 | 0 | — | Stabil |
| Armschienen, Stahl (Z) | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 0,3 | 0,3 | 0 | — | Stabil |
| Bart / Halsberge (Z) | 2 | 1 | 0 | 1 | 0 | 0 | 0 | 0,6 | 0,6 | 0 | — | — |
| Beinschienen, Bronze (Z) | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0,4 | 0,4 | 0 | — | Stabil |
| Beinschienen, Stahl (Z) | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0,6 | 0,6 | 0 | — | Stabil |
| Beintaschen / Schürze (Z) | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0,8 | 0,8 | 0 | — | Stabil |
| Bronzeharnisch | 0 | 5 | 4 | 4 | 0 | 0 | 0 | 2,6 | 2,6 | 3 | KK 3 | Stabil |
| Brustplatte, Stahl | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0,6 | 0,6 | 0 | — | Stabil |
| Brustschalen (Z) | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0,4 | 0,4 | 0 | — | Stabil |
| Drachenhelm (Z) | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0,5 | 0,5 | 0 | — | Stabil |
| fraysteinische Platte | 0 | 6 | 6 | 5 | 5 | 5 | 4 | 4,7 | 3,7 | 4 | KK 5 | Stabil, Standfestigkeit |
| Gestechrüstung (komplett) | 8 | 8 | 8 | 7 | 7 | 7 | 7 | 7,5 | 7,5 | 5 | KK 6 | Stabil, Standfestigkeit |
| Gladiatorenschulter | 0 | 3 | 0 | 2 | 3 | 0 | 0 | 1,15 | 0,15 | 0 | KK 2 | Stabil |
| granischer Reiterharnisch (komplett) | 3 | 7 | 7 | 5 | 5 | 5 | 5 | 5,6 | 3,6 | 4 | KK 5 | Stabil, Standfestigkeit |
| Kürass | 0 | 5 | 2 | 1 | 0 | 0 | 0 | 1,6 | 0,6 | 0 | KK 2 | Stabil |
| Lamellenpanzer | 0 | 5 | 4 | 4 | 1 | 1 | 1 | 2,9 | 2,9 | 3 | KK 3 | — |
| Leichte Platte | 0 | 5 | 5 | 4 | 0 | 0 | 2 | 3,2 | 2,2 | 2 | KK 3 | Stabil |
| Morion (Z) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0,3 | 0,15 | 0 | — | Stabil |
| Panzerbein (Z) | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0,8 | 0,8 | 0 | — | Stabil |
| Panzerhandschuhe, Paar (Z) | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0,2 | 0,2 | 0 | — | Stabil |
| Panzerschuh (Z) | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0,2 | 0,2 | 0 | — | Stabil |
| Plattenarme (Z) | 0 | 0 | 0 | 0 | 5 | 5 | 0 | 0,5 | 0,5 | 0 | — | Stabil |
| Plattenschultern (Z) | 0 | 1 | 0 | 1 | 2 | 2 | 0 | 0,6 | 0,6 | 0 | — | Stabil |
| Schaller (Z) | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0,4 | 0,2 | 0 | — | Stabil |
| Stechhelm / Visierhelm (Z) | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0,5 | 0,5 | 0 | — | Stabil |
| Sturmhaube (Z) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0,3 | 0,15 | 0 | — | Stabil |
| sultanischer Eisenhut (Z) | 4 | 0 | 0 | 1 | 0 | 0 | 0 | 0,6 | 0,3 | 0 | — | Stabil |
| Tellerhelm (Z) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0,2 | 0,2 | 0 | — | Stabil |
| Topfhelm (Z) | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0,5 | 0,5 | 0 | — | Stabil |

---

## Schilde

Ein Schild wird **aktiv geführt** und belegt eine Hand — er trägt daher **kein RS** und keine Trefferzonen. Stattdessen gibt er einen **Verteidigungsbonus (VTD)**, der deinen Verteidigungswert bei der Abwehr erhöht (siehe [[Kampfregeln]]). Die Belastung funktioniert wie bei Rüstung: **BE + TZ** addieren sich mit der getragenen Rüstung.

> [!abstract] Kennwerte Schild
> **VTD** = Verteidigungsbonus · **BE** = Behinderung · **TZ** = Tick-Zuschlag · **Voraussetzung** = Mindest-KK

| Schild | VTD | BE | TZ | Voraussetzung | Merkmale |
|---|---|---|---|---|---|
| Faustschild | +1 | 0 | 0 | — | Dornen |
| Kampfschild | +3 | 1 | 1 | KK 2 | Deckung |
| Nordschild | +2 | 0 | 1 | KK 2 | Schildwall |
| Reiterschild | +2 | 1 | 0 | — | — |
| Rundschild | +2 | 1 | 0 | — | — |
| Setzschild | +4 | 3 | 2 | KK 3 | Deckung, Schildwall |
| Turmschild | +3 | 2 | 1 | KK 3 | Deckung, Schildwall |

Die Schild-Merkmale *Deckung* (leichte Deckung im Fernkampf), *Schildwall* (+2 Schadensreduktion bei gelungener Abwehr) und *Dornen* (Schild als Waffe nutzbar) sind in [[Waffen#Waffenmerkmale]] definiert.

---

## Optional: Schnitt-RS (Ø RS)

Für NSC-Massen und schnelles Spiel führt jede Rüstung einen **gewichteten Durchschnitts-RS** (Spalte **Ø RS**), damit man bei Statisten die Zonen überspringen kann. Die Werte stammen aus der Quelltabelle (dort nach Zonenfläche gewichtet) und weichen minimal von unserer W10-Verteilung ab — für den Schnellzugriff unerheblich.
