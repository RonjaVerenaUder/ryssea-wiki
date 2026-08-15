---
tags:
  - meta
---

# Wiki veröffentlichen

Anleitung: So kommen Notizen aus dem Ryssea-Vault auf `wiki.ryssea.de`.

## 1. Notiz zum Veröffentlichen markieren

Im Frontmatter der Notiz `publish: true` setzen:

```yaml
---
publish: true
tags:
  - ort
---
```

Nur Notizen mit `publish: true` erscheinen auf der Website. Alle anderen bleiben unsichtbar.

> [!tip] Spoiler innerhalb einer Notiz
> Inhalte die Spieler erst aufklappen müssen:
> ```markdown
> <details>
> <summary>Spoiler: Geheimnis</summary>
> 
> Verborgener Text. Wird erst sichtbar wenn der Spieler klickt.
> 
> </details>
> ```

---

## 2. Content ins Quartz-Projekt kopieren

> [!warning] Vor dem Kopieren immer erst `git pull` im Wiki-Repo machen, damit keine Änderungen vom anderen Rechner überschrieben werden!

> [!danger] Nicht alles mitkopieren
> Ein einfaches `Copy-Item -Recurse` nimmt **alles** mit — auch den `Notion`-Ordner (2216 Dateien, 75 MB Rohexport) und das **`.git` des Vaults** (rund 90 MB). Beides gehört nicht ins Wiki: Der Notion-Export ist reines Archiv, und ein `.git` im `content/` erzeugt ein verschachteltes Repo, das Git stillschweigend ignoriert und das nur Platz frisst.
>
> Die Befehle unten schließen `Notion`, `.git`, `.obsidian` und `.claude` deshalb ausdrücklich aus. **Robocopy** eignet sich dafür besser als `Copy-Item`.

### Ronja-Rechner

```powershell
Remove-Item -Recurse -Force "C:\Users\Ronja\Documents\ryssea-wiki\content"
robocopy "C:\Users\Ronja\Documents\Obsidian\Ryssea-Vault-Synch" "C:\Users\Ronja\Documents\ryssea-wiki\content" /E /XD Notion .git .obsidian .claude .claudian
```

### Syral-Rechner

```powershell
Remove-Item -Recurse -Force "C:\Users\Syral\OneDrive\Dokumente\ryssea-wiki\content"
robocopy "C:\Users\Syral\OneDrive\Dokumente\Ryssea" "C:\Users\Syral\OneDrive\Dokumente\ryssea-wiki\content" /E /XD Notion .git .obsidian .claude .claudian
```

> [!tip] Kontrolle nach dem Kopieren
> `content/` sollte rund **375 Markdown-Dateien** und **etwa 45 MB** umfassen. Liegt dort ein Ordner `Notion` oder ein `.git`, hat der Ausschluss nicht gegriffen.

---

## 3. Änderungen committen und pushen

### Ronja-Rechner

```bash
cd "C:\Users\Ronja\Documents\ryssea-wiki"
git pull
git add content/
git commit -m "Update Vault Content"
git push
```

### Syral-Rechner

```bash
cd "C:\Users\Syral\OneDrive\Dokumente\ryssea-wiki"
git pull
git add content/
git commit -m "Update Vault Content"
git push
```

> [!info] Der Wiki-Branch heißt `v4`, nicht `master`
> Das Quartz-Repo arbeitet auf dem Branch **v4**. `git pull` und `git push` ohne weitere Angabe treffen ihn automatisch, solange nicht der Branch gewechselt wurde.

---

## 4. Warten

GitHub Actions baut die Seite automatisch neu. Dauert ca. 1–2 Minuten. Danach ist die aktualisierte Version auf `wiki.ryssea.de` live.

## Lokal testen (optional)

Falls du vor dem Pushen prüfen willst wie die Seite aussieht:

### Ronja-Rechner

```bash
cd "C:\Users\Ronja\Documents\ryssea-wiki"
npx quartz build --serve
```

### Syral-Rechner

```bash
cd "PFAD_ZUM_WIKI"
npx quartz build --serve
```

Dann `http://localhost:8080` im Browser öffnen.

---

## Checkliste vor dem Veröffentlichen

- [ ] `publish: true` im Frontmatter gesetzt?
- [ ] GM-Geheimnisse in Spoiler-Callouts oder ganz ohne `publish: true`?
- [ ] Wikilinks zeigen auf Notizen die ebenfalls `publish: true` haben?
- [ ] Keine persönlichen/Meta-Notizen versehentlich markiert?

## Referenzen

- Publish-Status und Prüfliste: [[Publish-Status]]
