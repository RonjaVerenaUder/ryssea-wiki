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

## 2. Content ins Quartz-Projekt kopieren

In PowerShell:

```powershell
Remove-Item -Recurse -Force "C:\Users\Syral\OneDrive\Dokumente\ryssea-wiki\content"
Copy-Item -Recurse "C:\Users\Syral\OneDrive\Dokumente\Ryssea" "C:\Users\Syral\OneDrive\Dokumente\ryssea-wiki\content"
```

Das ersetzt den gesamten `content/`-Ordner mit dem aktuellen Vault-Stand.

## 3. Änderungen committen und pushen

```bash
cd "C:\Users\Syral\OneDrive\Dokumente\ryssea-wiki"
git add content/
git commit -m "Update Vault Content"
git push
```

## 4. Warten

GitHub Actions baut die Seite automatisch neu. Dauert ca. 1–2 Minuten. Danach ist die aktualisierte Version auf `wiki.ryssea.de` live.

## Lokal testen (optional)

Falls du vor dem Pushen prüfen willst wie die Seite aussieht:

```bash
cd "C:\Users\Syral\OneDrive\Dokumente\ryssea-wiki"
npx quartz build --serve
```

Dann `http://localhost:8080` im Browser öffnen.

## Checkliste vor dem Veröffentlichen

- [ ] `publish: true` im Frontmatter gesetzt?
- [ ] GM-Geheimnisse in Spoiler-Callouts oder ganz ohne `publish: true`?
- [ ] Wikilinks zeigen auf Notizen die ebenfalls `publish: true` haben?
- [ ] Keine persönlichen/Meta-Notizen versehentlich markiert?

## Referenzen

- Publish-Status und Prüfliste: [[Publish-Status]]
- Projekt-Übersicht: Im Wissensdatenbank-Vault unter `02 Lernprojekte/Ryssea Wiki Setup.md`
