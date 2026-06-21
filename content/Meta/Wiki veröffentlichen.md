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

### Ronja-Rechner

In PowerShell:

```powershell
Remove-Item -Recurse -Force "C:\Users\Ronja\Documents\ryssea-wiki\content"
Copy-Item -Recurse "C:\Users\Ronja\Documents\Obsidian\Ryssea-Vault-Synch" "C:\Users\Ronja\Documents\ryssea-wiki\content"
```

### Syral-Rechner

> [!todo] Pfade noch eintragen!

```powershell
Remove-Item -Recurse -Force "PFAD_ZUM_WIKI\content"
Copy-Item -Recurse "PFAD_ZUM_VAULT" "PFAD_ZUM_WIKI\content"
```

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

> [!todo] Pfad noch eintragen!

```bash
cd "PFAD_ZUM_WIKI"
git pull
git add content/
git commit -m "Update Vault Content"
git push
```

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
