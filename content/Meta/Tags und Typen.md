---
tags: [meta]
---

# Tags und Typen

Übersicht aller `typ`-Werte und `tags` die im Vault verwendet werden. Dient als Referenz beim Anlegen neuer Notizen.

## Typ-Werte nach Ordner

Der `typ` im Frontmatter ist die **primäre Klassifizierung** jeder Notiz. Jede Notiz hat genau einen `typ`.

### Atlas

| typ | Beschreibung | Beispiele |
|---|---|---|
| `splitter` | Weltfragment, das größte geografische Gebilde | Baryia, Sharanma, Sultannii |
| `ebene` | Kosmologische Existenzebene | Elementarebene, Traumebene |
| `region` | Größeres Gebiet innerhalb eines Splitters (politisch oder geografisch abgegrenzt) | Unter-Baryia, Nerayan |
| `stadt` | Stadt oder große Siedlung | Aziza, Karasim, Kronrimar |
| `dorf` | Kleine Siedlung, Weiler, Bauernhöfe | Fares, Karaska |
| `gebirge` | Gebirgszug oder Bergmassiv | Askari-Gebirge |
| `gewässer` | Fluss, See, Meer, Küste | — |
| `wildnis` | Wald, Dschungel, Steppe, Wüste — unbesiedeltes Naturgebiet | Panthaura-Dschungel, Zentaurensteppe |
| `tempel` | Heiligtum, Schrein, göttlicher Ort | Quelle des Lebens |
| `gebäude` | Einzelnes Gebäude, Akademie, Festung, Turm | Landweber-Akademie |
| `ruine` | Zerstörter oder verlassener Ort | — |
| `ort` | Generischer Ort der in keine andere Kategorie passt | Fuchskopf |

**Region vs. Reich:** Eine Region (`typ: region`, Atlas/) beschreibt die **Geografie** — wo ist es, wie sieht es aus. Ein Reich (`typ: fraktion`, Fraktionen/) beschreibt die **Politik** — wer herrscht, welche Gesetze, welche Konflikte. Beide verlinken sich gegenseitig. Beispiel: [[Baryia (Splitter)]] (Splitter/Geografie) ↔ [[Baryia (Reich)]] (Politik).

### Völker

| typ | Beschreibung | Beispiele |
|---|---|---|
| `volk` | Eine Rasse/Spezies — Biologie, Merkmale, Verbreitung | Menschen, Phaerie, Zentauren |

### Kulturen

| typ | Beschreibung | Beispiele |
|---|---|---|
| `kultur` | Spezifische Kultur eines Volkes auf einem Splitter | Askasi, Kultur der Zwerge |

### Götter

| typ | Beschreibung | Beispiele |
|---|---|---|
| `gott` | Eine Gottheit — Aspekte, Karma, Anhänger, Domäne | Kaarsi, Horus, Bastet |

### Kosmologie

| typ | Beschreibung | Beispiele |
|---|---|---|
| `kosmologie` | Fundamentale Weltmechanik oder kosmisches Konzept | Zwielicht, Weltenweber, Weltenwille |
| `elementarlord` | Einer der 10 Elementarlords | Kirellian |

### Magie

| typ | Beschreibung | Beispiele |
|---|---|---|
| `magie` | Magiekonzept, Regelwerk-Element | Alltagsmagie, Schicksalspunkte |

### Fraktionen

| typ | Beschreibung | Beispiele |
|---|---|---|
| `reich` | Staat, Königreich, Imperium — politische Großmacht | Baryia (Reich), Taskasia, Panthaura (Reich) |
| `orden` | Ritter- oder Wächterorden — militärisch/spirituell organisiert | Cheyannin |
| `kult` | Geheimbund, religiöse Sekte — oft im Verborgenen | Kultisten des Weltenfressers |
| `gilde` | Handels- oder Handwerksorganisation | — |
| `kirche` | Organisierte Religion, Tempelstruktur | — |
| `fraktion` | Generisch, passt in keine andere Kategorie | — |

### Charaktere

| typ | Beschreibung | Beispiele |
|---|---|---|
| `npc` | Nicht-Spieler-Charakter | Ram'Aches, Rehotep, Anef |
| `spielercharakter` | Spielercharakter | Sethos |
| `begleiter` | Tierbegleiter oder Vertrauter eines SC | Resul |

### Artefakte

| typ | Beschreibung | Beispiele |
|---|---|---|
| `artefakt` | Magischer Gegenstand, Relikt | Dissonanz-Nadel, Elementarkernkompass |

### Flora & Fauna

| typ | Beschreibung | Beispiele |
|---|---|---|
| `kreatur` | Kreatur, Pflanze oder Ökosystem eines Splitters | — |

### Sprachen

| typ | Beschreibung | Beispiele |
|---|---|---|
| `sprache` | Eine Sprache Rysseas | — |

### Geschichte

| typ | Beschreibung | Beispiele |
|---|---|---|
| `ereignis` | Historisches Ereignis | — |

### Kampagnen

| typ | Beschreibung | Beispiele |
|---|---|---|
| `kampagne` | Kampagnen-Hauptnotiz | Sethos Gang, Nebelkinder |
| `abenteuer` | Einzelner Handlungsbogen | Missing Cat |
| `spieltag` | Session-Protokoll | Spieltag 001 |
| `plot` | Plotfaden mit Fortschrittstracking | Einfluss von Kaarsi |

### Meta/Strukturell

| typ | Beschreibung | Beispiele |
|---|---|---|
| `moc` | Map of Content — Übersichtsseite eines Bereichs | Atlas von Ryssea, Völker von Ryssea |
| `index` | Zentraler Einstiegspunkt des Vaults | index.md |

---

## Tags

Tags ergänzen den `typ` um **Querschnittsthemen** und **Metadaten**. Eine Notiz kann mehrere Tags haben.

### Inhalts-Tags (Oberkategorie)

Diese Tags markieren die grobe Zugehörigkeit. Der erste Tag sollte immer die Oberkategorie sein:

| Tag | Verwendung |
|---|---|
| `splitter` | Alle Splitter-Notizen |
| `ort` | Alle Orte innerhalb eines Splitters (stadt, dorf, region, gebirge, wildnis etc.) |
| `volk` | Alle Völker |
| `kultur` | Alle Kulturen |
| `gott` | Alle Götter |
| `kosmologie` | Alle Kosmologie-Notizen |
| `magie` | Alle Magie-Notizen |
| `fraktion` | Alle Fraktionen |
| `npc` | Alle NPCs |
| `spielercharakter` | Alle Spielercharaktere |
| `artefakt` | Alle Artefakte |
| `kreatur` | Alle Kreaturen, Flora & Fauna |
| `sprache` | Alle Sprachen |
| `kampagne` | Kampagnen-Hauptnotizen |
| `abenteuer` | Abenteuer-Notizen |
| `spieltag` | Spieltag-Notizen |
| `plot` | Plot-Notizen |

### Sub-Tags (Spezifizierung)

Zweiter Tag für die genauere Einordnung:

**Orte (Oberkategorie `ort`):**

| Tag | Verwendung |
|---|---|
| `stadt` | Städte und große Siedlungen |
| `dorf` | Kleine Siedlungen |
| `region` | Größere Gebiete |
| `gebirge` | Gebirgszüge |
| `wildnis` | Naturgebiete |
| `tempel` | Heiligtümer |
| `gebäude` | Einzelgebäude |
| `ruine` | Zerstörte Orte |
| `gewässer` | Gewässer |

**Fraktionen (Oberkategorie `fraktion`):**

| Tag | Verwendung |
|---|---|
| `reich` | Staaten und Königreiche |
| `orden` | Ritter- oder Wächterorden |
| `kult` | Geheimbünde und Sekten |
| `gilde` | Handels- oder Handwerksorganisationen |
| `kirche` | Organisierte Religionen |

**Sonstige:**

| Tag | Verwendung |
|---|---|
| `elementarlord` | Elementarlords |
| `begleiter` | Tierbegleiter |
| `ebene` | Kosmologische Ebenen |

### Status- und Meta-Tags

| Tag | Verwendung |
|---|---|
| `gm-geheim` | Inhalt den Spieler nicht kennen dürfen |
| `spieler-kanon` | Aus dem Spiel entstandene Lore |
| `regelwerk` | Notizen die zum Regelwerk gehören |
| `moc` | Map of Content / Übersichtsseite |
| `meta` | Vault-Verwaltung (Aufgaben, Tags, Publish-Status) |

### Kampagnen-Tags

| Tag | Verwendung |
|---|---|
| `sethos-gang` | Gehört zur Sethos Gang Kampagne |
| `nebelkinder` | Gehört zur Nebelkinder Kampagne |
| `synfathia` | Gehört zur Team Synfathia Kampagne |

---

## Frontmatter-Felder

Neben `tags` und `typ` gibt es je nach Notiz-Typ weitere Frontmatter-Felder:

| Feld | Verwendung | Notiz-Typen |
|---|---|---|
| `status` | platzhalter / entwurf / fertig | Alle |
| `publish` | true — erscheint auf wiki.ryssea.de | Alle |
| `splitter` | Zugehöriger Splitter als Wikilink | Orte, Städte, Regionen etc. |
| `reich` | Zugehöriges Reich als Wikilink | Städte |
| `größe` | Dorf / Kleinstadt / Stadt / Großstadt / Metropole | Städte |
| `nebeltore` | Liste verbundener Splitter | Splitter |
| `elementarlord` | Zugehöriger Elementarlord | Splitter |
| `inspiration` | Reale Inspiration/Vorbild | Splitter |
| `volk` | Zugehöriges Volk | Kulturen, NPCs |
| `domäne` | Machtbereich eines Gottes | Götter |
| `element` | Zugehöriges Element | Elementarlords, Völker |
| `kampagne` | Zugehörige Kampagne | Abenteuer, Spieltage, Plots |
| `zyklus` | Aus welchem Weltenzyklus das Fragment stammt | Splitter, Ereignisse |
| `art` | Untertyp / Kategorie | Völker, Artefakte, Kreaturen |
| `ursprung` | Herkunft / Erschaffer | Völker, Artefakte |
| `besitzer` | Aktueller Besitzer oder Ort | Artefakte |
| `verbreitung` | Vorkommen (Splitter / Regionen) | Völker, Kreaturen |
| `gefahr` | Gefahrenstufe | Kreaturen |
| `sprecher` | Wer die Sprache spricht | Sprachen |
| `schrift` | Zugehörige Schrift | Sprachen |
| `verwandt` | Verwandte Sprachen | Sprachen |
