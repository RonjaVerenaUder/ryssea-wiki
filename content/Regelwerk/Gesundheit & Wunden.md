---
tags: [regelwerk, kampf]
typ: regelwerk
status: fertig
publish: true
quelle: Regeldesign 2026-08
---

# Gesundheit & Wunden

Wie viel Schaden ein Wesen wegsteckt, bevor es zusammenbricht — und wie Verletzungen auf seine Proben durchschlagen.

---

## Gesundheitsstufen

Der Körper ist in **5 Gesundheitsstufen** unterteilt. Jede Stufe fasst so viele Schadenspunkte, wie die **Lebenspunkte (LeP = KO + GK)** des Wesens betragen — dieser Wert ist die **Wundschwelle**. (Herleitung der LeP siehe [[Abgeleitete Werte]].)

> [!info] Gesamter Puffer = 5 × LeP
> LeP ist also **nicht** der ganze Trefferpuffer, sondern die Größe *einer* Stufe. Ein Held mit LeP 8 steckt insgesamt **40** Schaden weg — verteilt auf fünf Gesundheitsstufen.

---

## Schaden und Absinken

Erlittener Schaden (nach Abzug von [[Rüstungen|Rüstschutz]]) wird als **kumulierter Schaden** notiert. Überschreitet dieser eine weitere volle **Wundschwelle (LeP)**, sinkt das Wesen um **eine Gesundheitsstufe** und erleidet den zugehörigen **Wundabzug**:

| Kumulierter Schaden | Gesundheitsstufe | Wundabzug |
|---|---|---|
| 0 | **Unversehrt** | — |
| > 1× LeP | **Angeschlagen** | −2 |
| > 2× LeP | **Verletzt** | −4 |
| > 3× LeP | **Schwer verletzt** | −6 |
| > 4× LeP | **Kampfunfähig** | bewusstlos ([[Zustände#Bewusstlos]]) |
| > 5× LeP | — | **[[Zustände#Sterbend|Sterbend]]** / Tod |

---

## Wundabzüge

Der **Wundabzug** der aktuellen Gesundheitsstufe gilt als **Malus auf alle aktiven Proben** — Fertigkeiten, Angriff, Aktive Abwehr und Zauber. Die **passiven Verteidigungswerte** ([[Abgeleitete Werte#Passive Verteidigungen|Ausweichen, Resistenzen]]) bleiben davon unberührt.

Steigt das Wesen durch Heilung wieder eine Stufe auf, entfällt der entsprechende Abzug.

---

## Zusammenhang mit Zuständen

- **[[Zustände#Verwundet|Verwundet [Stufe]]]** — zählt für den Wundabzug als um *Stufe* Gesundheitsstufen tiefer, **ohne** echten LeP-Verlust (reiner Schmerz-/Wundeffekt).
- **[[Zustände#Sterbend|Sterbend [Stufe]]]** — frisst pro Intervall eine **ganze Gesundheitsstufe** an LeP; sind alle verbraucht, tritt der Tod ein.
- **[[Zustände#Bewusstlos|Bewusstlos]]** — die Folge der Gesundheitsstufe *Kampfunfähig*.

---

## Geistige Gesundheit & Betäubung (GLeP)

Sowohl **geistiger Schaden** (Furcht, Zermürbung, bestimmte Zauber) als auch **Betäubungsschaden** (nicht-tödliche Treffer — *Betäubungsschlag*, Waffenmerkmal *Stumpf*, *Wuchtangriff* als Betäubung) laufen über die **Geistigen Lebenspunkte (GLeP = ENT + LG)** als Wundschwelle: fünf geistige Gesundheitsstufen, dieselben Wundabzüge (−2 / −4 / −6, dann auf **geistige** Proben).

Der Endpunkt ist **eigenständig** — das Bewusstsein schwindet bzw. der Geist bricht, statt zu sterben:

- Die letzte geistige Stufe bedeutet **geistige Handlungsunfähigkeit ohne Tod**: bei Betäubung **[[Zustände#Bewusstlos|Bewusstlos]]** (k. o. geschlagen), bei Furcht/Zermürbung **geistig gebrochen** (willenlos, apathisch).
- Ein geistiges *Sterbend*-Pendant gibt es nicht. Erholung läuft über **GLeP-Regeneration**, das Manöver **Atemholen** (10 + KO Punkte Betäubungsschaden, siehe [[Kampfregeln]]) und Zeit.

---

## Heilung

Die **LeP-Regeneration (KO + KK)** baut kumulierten Schaden ab (siehe [[Abgeleitete Werte]]). Mit jeder zurückgewonnenen Wundschwelle steigt das Wesen eine Gesundheitsstufe auf und verliert den zugehörigen Wundabzug.
