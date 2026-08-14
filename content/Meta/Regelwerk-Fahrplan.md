---
tags: [meta, regelwerk]
typ: meta
status: entwurf
---

# Regelwerk-Fahrplan (Aufbau & Inhalt)

Bauplan für das kanonische, **druckbare** Ryssea-Regelwerk. Ziel: ein Buch, das man von vorne nach hinten lesen kann (Regeln kompakt) mit einem **Nachschlageteil** (lange Listen/Tabellen) hinten.

## Arbeitsweise (Clean-Room)

1. Alle jetzigen Regelnotizen → Sammelordner **`Regelwerk/_Unbestätigt/`** (`status: unbestätigt`, `publish: false`).
2. Kapitel für Kapitel: aus Material (+ Rohquellen: Notion-Export, Char-Tool-Excel im Anhänge-Ordner, Google Site) die **bestätigte** Version schreiben → in `Regelwerk/` als Kanon ablegen → Rohnotiz aus `_Unbestätigt/` entfernen.
3. Fertig, wenn `_Unbestätigt/` leer ist. Backup = Rohquellen + git-Historie.

**Legende Status:** ✅ Material vorhanden · ⚠️ vorhanden, aber unvollständig (siehe [[Regelwerk-Diskrepanzen]]) · ❌ Lücke / neu zu schreiben

---

## Inhaltsverzeichnis

### Teil I — Grundlagen
1. Einführung (Welt & Ton) — ❌ neu (kurz)
2. Würfelsystem & Proben — ✅
3. Begriffe & Abkürzungen — ⚠️ (aus Würfelsystem + Abgeleitete Werte zusammenziehen)

### Teil II — Charaktererstellung *(in Generierungs-Reihenfolge, als Leitfaden)*
4. Konzept — ❌ neu
5. Rasse *(+ Modifikatoren-Tabelle)* — ⚠️ (Beschreibung ✅, **Werte-Mods nur im Char-Tool** ❌)
6. Eigenschaften — ✅
7. Magieklasse(n) — ✅
8. Talente & Schwerpunkte — ✅
9. Vorteile & Nachteile — ⚠️ (~30 + Priester-Vorteile fehlen)
10. Ressourcen — ✅
11. Schicksalsgabe — ✅
12. Abgeleitete Werte berechnen — ✅
13. Startausrüstung — ❌ neu
14. **Beispielcharakter (Schritt für Schritt)** — ❌ neu
*(Schritt-Reihenfolge noch an das echte Gen-Tool / die Generierungs-Regeln angleichen.)*

### Teil III — Fortschritt
15. Heldenstufen & Steigerung *(+ Steigerungskosten-Tabelle)* — ✅ (Kosten-Tabelle aus Char-Tool ergänzen)
16. Meisterschaften *(System)* — ✅ (Listen ⚠️: ~150 fehlen)

### Teil IV — Talente & Gaben im Spiel
17. Talente außerhalb des Kampfes *(z.B. Anführen)* — ❌ neu (aus Schwerpunkten ausbauen)
18. Magische Gaben *(Traumweben, Landweben, Spiegelweben …, ausführlich)* — ⚠️ (Notiz Magische Gaben ausbauen)
19. Sprachen & Schriften *(3-Stufen-System)* — ❌ neu
20. **Vertraute & Begleiter** *(Tiergefährten, Elementar-/Naturgeister, KI-Golem/Untote, „Gefährte im Kampf")* — ❌ neu

### Teil V — Kampf
21. Kampfregeln — ✅
22. Zustände — ✅
23. **Heilung, Ruhe & Erholung** *(LeP/GLeP-Regeneration, Gift & Krankheit)* — ❌ neu
24. Waffen, Rüstungen & Schilde — ⚠️ (Rüstungen unvollständig, Legende TP/BW offen)

### Teil VI — Magie *(wächst)*
25. Magieregeln *(Parameter, Komponenten, Affinität/Kanalisierung, Fokus)* — ✅
26. Magiearten *(Illusion ✅; Nekromantie, Beschwörung, Analyse/Hellsicht ❌)* — ⚠️
27. Artefakte & Verzauberung — ❌ neu (Artefakte-Ordner + Regeln)
28. Grimoire *(→ Nachschlageteil)* — ⚠️ (~30 Zauber fehlen)

### Teil VII — Glaube & Götter
29. Götter & Karma — ✅ (Götterregeln)
30. **Priester & Weihe in Werten** — ❌ **große Lücke** (Char-Tool + Google Site „Götter in Werten")
31. Weiherituale — ❌ neu
32. „Göttliche Macht" *(neue Ressource, Legende/Bekanntheit)* — ❌ neu (geplant)

### Teil VIII — Handwerk
33. Handwerkssystem & Verbesserungen — ✅
34. Materialien & Handwerkstabellen *(→ Nachschlageteil)* — ❌ (auf Google Site nur Bilder)

### Teil IX — Am Spieltisch *(Spielleitung)*
35. Schnellreferenz (Proben auf einen Blick) — ❌ (Google Site, noch holen)
36. Meisterschirm *(abgeleitete Werte, Tabellen)* — ⚠️
37. **Token-System** *(weiße/schwarze Schicksalspunkte als Verhaltens-Mechanik + Fraktale, Götter-Segen, Hilfe, Special-Action-Token)* — ⚠️ (Token-Notiz ausbauen)
38. **Weltenwille** *(was die Spielleitung damit anstellen kann)* — ❌ neu (GM-Werkzeug, aus Kosmologie ableiten)
39. **Reisen & Nebeltore** *(zwischen Splittern)* — ❌ neu
40. Tisch- & optionale Regeln — ✅
41. Beta-Regeln — ✅

### Anhang — Nachschlageteil
- **Listen:** Vorteile/Nachteile · Talente · Meisterschaften · Zauber (Grimoire) · Waffen/Rüstungen/Merkmale
- **Bestiarium** (Gegner & Tiere) · **Flora** (Pflanzen) · **Materialien** — ⚠️ (Flora & Fauna-Ordner + Notion-Bestiarium)
- **Druckbarer Heldenbogen** — ❌ neu
- **Glossar & Index** — ❌ neu

---

## Nächste Schritte
1. Fahrplan freigeben / anpassen.
2. `Regelwerk/_Unbestätigt/` anlegen, alle Regelnotizen dorthin, `status: unbestätigt` + `publish: false`.
3. Mit Teil I / Kapitel 2 (Würfelsystem) als erstem kanonisiertem Abschnitt starten — oder mit einer der großen Lücken (Priester, Meisterschaften-Listen).
