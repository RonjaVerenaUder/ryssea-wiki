---
tags: [regelwerk, charaktererstellung]
typ: regelwerk
status: fertig
publish: true
---

# Abgeleitete Werte

Aus [[Eigenschaften]], [[Talente|Talenten]], Rasse und Heldenstufe ergeben sich weitere Werte. Sie werden **nicht getrennt gesteigert**, sondern steigen automatisch mit ihren Grundlagen (siehe [[Steigerung]]).

Grundlage sind die acht Eigenschaften (BW, CH, ENT, FF, IN, KO, KK, LG) sowie die **Größenklasse (GK)** aus der [[Rassen|Rasse]].

---

## Aus Eigenschaften & Größenklasse

| Wert | Formel |
|---|---|
| **Geschwindigkeit** (GS) | BW + GK |
| **Initiative** (Ini) | (2 × IN + ENT + BW) ÷ 2 |
| **Lebenspunkte** (LeP) | KO + GK |
| **LeP-Regeneration** | KO + KK |
| **Geistige Lebenspunkte** (GLeP) | ENT + LG |
| **GLeP-Regeneration** | KO + ENT |
| **Erinnern** | (2 × LG + IN) ÷ 2 |

*(Werte mit ÷ 2 werden — wie der Grundwert — ab ,5 aufgerundet.)*

> [!info] LeP & GLeP sind Wundschwellen
> **LeP** und **GLeP** geben nicht den gesamten Trefferpuffer an, sondern die Größe *einer* Gesundheitsstufe. Wie Schaden daraus in Stufen und Wundabzüge umschlägt, steht in [[Gesundheit & Wunden]].

> [!warning] Die Geschwindigkeit sinkt unter Last
> Die **Gesamt-Behinderung** aus Rüstung, Schild, Parierwaffe und [[Traglast]] senkt die Geschwindigkeit um **1 Punkt je volle 6 Punkte BE** — bei BE 6 also −1, bei BE 12 −2. Sie fällt dabei nie unter **1**. Näheres unter [[Rüstungen#Belastung|Belastung]] und [[Traglast]].

---

## Aus der Heldenstufe

| Wert | Formel |
|---|---|
| **Schicksalspunkte** (SP) | Heldenstufe + 2 |
| **Zauberaffinität** | Heldenstufe × 2 |
| **Kanalisierungspunkte** | Heldenstufe × 2 |

---

## Passive Verteidigungen

Die passiven Verteidigungswerte entsprechen dem [[Würfelsystem & Proben|Grundwert]] je eines Talents — der Wert, den ein Angreifer mit seinem Ergebniswert übertreffen muss, solange das Ziel nicht **aktiv** abwehrt:

| Verteidigung | = Grundwert von | Eigenschaften |
|---|---|---|
| **Ausweichen** | Akrobatik | BW • ENT • KK |
| **Körperliche Resistenz** | Zähigkeit | ENT • KK • KO |
| **Geistige Resistenz** | Selbstbeherrschung | CH • ENT • KO |

*(Auch diese Werte werden — wie der Grundwert — ab ,5 aufgerundet.)*

Die **aktiven** Abwehraktionen (Parade, aktives Ausweichen, Schildparade) kosten Zeit auf der Tickleiste und werden im [[Kampfregeln|Kampfkapitel]] behandelt.
