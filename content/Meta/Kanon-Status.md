---
tags: [meta]
---

# Kanon-Status

Übersicht über den Bearbeitungsstand aller Notizen im Vault. Ziel: Schritt für Schritt Notizen von `entwurf` auf `status: fertig` setzen — als Signal dass Inhalt geprüft, ausgearbeitet und als Kanon gesichert gilt.

> [!info] Wie wird eine Notiz "fertig"?
> Eine Notiz gilt als fertig wenn: Inhalt ausgearbeitet (keine leeren Abschnitte), Fakten mit Ronja abgestimmt, Wikilinks gesetzt, Frontmatter vollständig. Dann `status: fertig` im Frontmatter setzen.

---

## Zusammenfassung

| Status         | Anzahl                                                                                                                              |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| ✅ Fertig       | `$= dv.pages().where(p => p.status == "fertig" && !p.file.path.includes("Meta/") && !p.file.path.includes("Anhänge/")).length`      |
| 📝 Entwurf     | `$= dv.pages().where(p => p.status == "entwurf" && !p.file.path.includes("Meta/") && !p.file.path.includes("Anhänge/")).length`     |
| 🪨 Platzhalter | `$= dv.pages().where(p => p.status == "platzhalter" && !p.file.path.includes("Meta/") && !p.file.path.includes("Anhänge/")).length` |

---

## ✅ Fertig — gesicherter Kanon

Notizen die ausgearbeitet und geprüft sind.

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  file.folder as "Ordner",
  tags as "Tags"
FROM ""
WHERE status = "fertig"
AND !contains(file.path, "Meta/")
AND !contains(file.path, "Anhänge/")
SORT file.folder ASC, file.name ASC
```

---

## 📝 Entwurf — in Bearbeitung

Notizen die angefangen aber noch nicht fertig sind. Diese sollten nach und nach ausgearbeitet und auf `fertig` gesetzt werden.

### Kosmologie & Magie

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  tags as "Tags"
FROM "Kosmologie" OR "Magie"
WHERE status = "entwurf"
SORT file.name ASC
```

### Völker & Kulturen

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  tags as "Tags"
FROM "Völker" OR "Kulturen"
WHERE status = "entwurf"
SORT file.name ASC
```

### Atlas — Splitter & Orte

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  file.folder as "Ordner",
  tags as "Tags"
FROM "Atlas"
WHERE status = "entwurf"
SORT file.folder ASC, file.name ASC
```

### Götter

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  tags as "Tags"
FROM "Götter"
WHERE status = "entwurf"
SORT file.name ASC
```

### Fraktionen

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  tags as "Tags"
FROM "Fraktionen"
WHERE status = "entwurf"
SORT file.name ASC
```

### Charaktere & NPCs

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  file.folder as "Ordner",
  tags as "Tags"
FROM "Charaktere"
WHERE status = "entwurf"
SORT file.name ASC
```

### Artefakte, Flora & Fauna, Geschichte

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  file.folder as "Ordner",
  tags as "Tags"
FROM "Artefakte" OR "Flora & Fauna" OR "Geschichte"
WHERE status = "entwurf"
SORT file.folder ASC, file.name ASC
```

### Kampagnen (Abenteuer & Plots)

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  file.folder as "Ordner",
  tags as "Tags"
FROM "Kampagnen"
WHERE status = "entwurf"
AND !contains(file.path, "Spieltage/")
SORT file.folder ASC, file.name ASC
```

---

## 🪨 Platzhalter — noch nicht befüllt

Notizen die nur als Link-Ziel existieren. Vollständige Liste auch in [[Meta/Aufgaben]].

```dataview
TABLE WITHOUT ID
  file.link as "Notiz",
  file.folder as "Ordner"
FROM ""
WHERE status = "platzhalter"
AND !contains(file.path, "Meta/")
AND !contains(file.path, "Anhänge/")
SORT file.folder ASC, file.name ASC
```
