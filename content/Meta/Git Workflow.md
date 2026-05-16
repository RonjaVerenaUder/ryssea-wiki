---
tags:
  - meta
---

# Git Workflow

Dieses Vault wird über zwei getrennte Git-Repos verwaltet:

| Repo | Zweck | Sichtbarkeit |
|------|-------|-------------|
| **Ryssea-Vault-Synch** | Der komplette Obsidian-Vault mit allen Notizen | Privat |
| **ryssea-wiki** | Quartz-Projekt für wiki.ryssea.de | Je nach GitHub-Einstellung |

Das Vault-Repo enthält alles — auch GM-Geheimnisse, Entwürfe und Meta-Dateien. Das Wiki-Repo enthält nur die publizierten Inhalte plus das Quartz-Framework.

### Speicherorte pro Rechner

| Rechner | Vault | Wiki |
|---------|-------|------|
| **Syral (Haupt-PC)** | `C:\Users\Syral\OneDrive\Dokumente\Ryssea` | `C:\Users\Syral\OneDrive\Dokumente\ryssea-wiki` |
| **Ronja (Zweit-PC)** | `C:\Users\Ronja\Documents\Obsidian\ryssea-vault-synch` | *noch nicht geklont* |

---

## Teil 1: Mit dem Vault arbeiten (Ryssea-Vault-Synch)

Das ist der normale Arbeitsalltag. Notizen schreiben, bearbeiten, Worldbuilding betreiben.

### Neuen Rechner einrichten (einmalig)

```bash
# 1. Repo klonen (Zielordner frei wählbar)
git clone https://github.com/RonjaVerenaUder/Ryssea-Vault-Synch.git

# 2. Obsidian öffnen → "Open folder as vault" → den geklonten Ordner wählen

# 3. Obsidian-Plugins installieren (werden nicht mit-synchronisiert):
#    - Community Plugin "BRAT" installieren
#    - Claudian Plugin über BRAT installieren
```

### Täglicher Workflow

#### Bevor du anfängst: Änderungen vom anderen Rechner holen

> [!warning] Immer zuerst pullen!
> Wenn du auf zwei Rechnern gleichzeitig arbeitest ohne zu pullen, gibt es Merge-Konflikte. Die sind bei Markdown-Dateien lösbar, aber nervig.

**Auf dem Haupt-PC (Syral):**
```bash
cd "C:\Users\Syral\OneDrive\Dokumente\Ryssea"
git pull
```

**Auf dem Zweit-PC (Ronja):**
```bash
cd "C:\Users\Ronja\Documents\Obsidian\ryssea-vault-synch"
git pull
```

#### Wenn du fertig bist: Änderungen hochladen

**Auf dem Haupt-PC (Syral):**
```bash
cd "C:\Users\Syral\OneDrive\Dokumente\Ryssea"
git add -A
git commit -m "Kurze Beschreibung was du gemacht hast"
git push
```

**Auf dem Zweit-PC (Ronja):**
```bash
cd "C:\Users\Ronja\Documents\Obsidian\ryssea-vault-synch"
git add -A
git commit -m "Kurze Beschreibung was du gemacht hast"
git push
```

Beispiele für Commit-Messages:
- `"Neuer Splitter: Aeltharis"`
- `"Spieltag 013 Sethos Gang eingepflegt"`
- `"Pantheon der Sharnai ausgearbeitet"`
- `"Diverse Korrekturen und neue NPCs"`

### Kurzreferenz: Die wichtigsten Git-Befehle

| Befehl | Was er tut |
|--------|-----------|
| `git pull` | Holt Änderungen vom Server |
| `git add -A` | Markiert alle Änderungen zum Speichern |
| `git commit -m "Text"` | Speichert die Änderungen lokal mit Beschreibung |
| `git push` | Lädt die gespeicherten Änderungen auf den Server |
| `git status` | Zeigt was sich geändert hat seit dem letzten Commit |
| `git log --oneline -10` | Zeigt die letzten 10 Commits |
| `git diff` | Zeigt die konkreten Änderungen im Detail |

### Wenn etwas schiefgeht

**Merge-Konflikt nach `git pull`:**
Git markiert die Konfliktstelle in der Datei mit `<<<<<<<` und `>>>>>>>`. Öffne die Datei, entscheide welche Version richtig ist, lösche die Markierungen, dann:
```bash
git add -A
git commit -m "Merge-Konflikt gelöst"
```

**Letzte Änderung war Mist und noch nicht gepusht:**
```bash
git reset --soft HEAD~1
```
Das macht den letzten Commit rückgängig, behält aber die Dateien.

**Datei auf den letzten Stand zurücksetzen:**
```bash
git checkout -- "Pfad/zur/Datei.md"
```

---

## Teil 2: Wiki veröffentlichen (ryssea-wiki)

Wenn Inhalte auf wiki.ryssea.de erscheinen sollen. Detaillierte Anleitung auch in [[Wiki veröffentlichen]].

### Voraussetzung

Das Quartz-Repo muss auf dem Rechner geklont sein:
```bash
git clone https://github.com/RonjaVerenaUder/ryssea-wiki.git
```

### Publish-Workflow

#### Schritt 1: Notizen mit `publish: true` markieren

Im Frontmatter jeder Notiz die auf die Website soll:
```yaml
---
publish: true
---
```

**Nicht publishen:** Meta-Dateien, Anhänge, CLAUDE.md, GM-Spieltage, aktive Abenteuer.
Vollständige Regeln in [[Wiki veröffentlichen]] und [[Publish-Status]].

#### Schritt 2: Content ins Quartz-Projekt kopieren

**Auf dem Haupt-PC (Syral):**
```powershell
Remove-Item -Recurse -Force "C:\Users\Syral\OneDrive\Dokumente\ryssea-wiki\content"
Copy-Item -Recurse "C:\Users\Syral\OneDrive\Dokumente\Ryssea" "C:\Users\Syral\OneDrive\Dokumente\ryssea-wiki\content"
```

**Auf dem Zweit-PC (Ronja):**
```powershell
Remove-Item -Recurse -Force "WIKI-PFAD\content"
Copy-Item -Recurse "C:\Users\Ronja\Documents\Obsidian\ryssea-vault-synch" "WIKI-PFAD\content"
```

> [!info] Wiki-Repo noch nicht auf dem Zweit-PC?
> Falls du auch vom Zweit-PC publishen willst, muss dort das ryssea-wiki Repo geklont sein (siehe Voraussetzung oben). Dann hier den `WIKI-PFAD` mit dem tatsächlichen Pfad ersetzen und in der Tabelle oben ergänzen.

#### Schritt 3: Committen und pushen

**Auf dem Haupt-PC (Syral):**
```bash
cd "C:\Users\Syral\OneDrive\Dokumente\ryssea-wiki"
git add content/
git commit -m "Update Wiki-Inhalte"
git push
```

**Auf dem Zweit-PC (Ronja):**
```bash
cd "WIKI-PFAD"
git add content/
git commit -m "Update Wiki-Inhalte"
git push
```

GitHub Actions baut die Seite automatisch neu. Nach 1-2 Minuten ist die Änderung auf wiki.ryssea.de live.

#### Schritt 4 (optional): Lokal testen vor dem Pushen

**Auf dem Haupt-PC (Syral):**
```bash
cd "C:\Users\Syral\OneDrive\Dokumente\ryssea-wiki"
npx quartz build --serve
```

**Auf dem Zweit-PC (Ronja):**
```bash
cd "WIKI-PFAD"
npx quartz build --serve
```

Dann `http://localhost:8080` im Browser öffnen.

### Kurzreferenz: Publish-Checkliste

- [ ] `publish: true` im Frontmatter gesetzt?
- [ ] GM-Geheimnisse in `> [!danger]- GM-Wissen` Callouts verpackt?
- [ ] Spoiler in `> [!warning]- Spoiler` Callouts?
- [ ] Wikilinks zeigen auf Notizen die ebenfalls `publish: true` haben?
- [ ] Keine Meta-Notizen oder CLAUDE.md versehentlich markiert?

---

## Übersicht: Was liegt wo?

```
Ryssea-Vault-Synch (dieses Repo)    ryssea-wiki (Quartz-Repo)
├── Alles aus dem Vault              ├── quartz/ (Framework)
├── GM-Geheimnisse                   ├── content/ (kopierte Notizen)
├── Meta-Dateien                     ├── quartz.config.ts
├── Entwürfe                         └── GitHub Actions → wiki.ryssea.de
├── .obsidian/ (Settings)
└── CLAUDE.md
```

Der Vault ist die **einzige Quelle der Wahrheit**. Das Wiki-Repo bekommt nur Kopien der publizierten Inhalte.
