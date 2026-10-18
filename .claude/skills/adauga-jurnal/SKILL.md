---
name: adauga-jurnal
description: Adaugă o însemnare în jurnalul de pe poienel.ro din pozele urcate în repo și din informațiile din commit și din mesaj. Se folosește când utilizatorul spune „adaugă jurnal” / „adauga jurnal” (sau trimite poze și cere o însemnare). Trage branch-ul, pregătește pozele, scrie însemnarea, face build, commit și push; întreabă dacă lipsește data sau ce s-a făcut.
---

# Adaugă jurnal

Fluxul complet pentru o însemnare nouă în `poienel.ro/jurnal.html`. Regulile paginii sunt în `poienel.ro/CLAUDE.md` (secțiunea despre `jurnal.html`); acest skill spune doar ordinea pașilor.

## 1. Pull

`git fetch origin <branch-curent>` și `git merge --ff-only origin/<branch-curent>` (branch-ul pe care lucrează sesiunea). Dacă nu intră fast-forward, oprește-te și spune ce s-a întâmplat; nu rebase, nu force.

## 2. Pozele noi

- Pozele noi sunt în `poienel.ro/resurse/jurnal/` și **nu** respectă numele `AAAA-LL-ZZ-subiect.jpg` (de obicei `WhatsApp Image … .jpeg`, `IMG_….jpg`); folderul `thumb/` se ignoră.
- Citește mesajele commit-urilor care le-au adăugat: `git log --format='%h %ci %s' --diff-filter=A -- 'poienel.ro/resurse/jurnal/*'`. Mesajul poate conține data și descrierea lucrării.
- Uită-te la fiecare poză (previzualizare mică cu Pillow în scratchpad, apoi Read), ca să știi ce arată și ce `alt` să scrii. Verifică și EXIF `DateTimeOriginal` (WhatsApp îl șterge de obicei).

## 3. Informațiile necesare; întreabă dacă lipsesc

O însemnare are nevoie de: **data** lucrării (ISO) și **ce s-a făcut** (în 1–3 fraze de la utilizator). Sursele, în ordine: mesajul utilizatorului, mesajul de commit, EXIF-ul pozelor (doar ca propunere).

Dacă data lipsește sau e ambiguă, sau dacă nu reiese clar ce s-a făcut, **întreabă înainte să scrii** (AskUserQuestion, o singură întrebare cu tot ce lipsește; propune data din EXIF sau din commit dacă există). Nu inventa activități din ce pare că se vede în poze; pozele doar completează textul.

## 4. Pregătirea pozelor

Din `poienel.ro/`, pentru fiecare poză: `python3 -I foto.py <AAAA-LL-ZZ> <subiect> "<fișierul original>"` (subiect scurt, fără diacritice, cu cratime: `trasare-ruleta`, `gunoi-gramezi`). Scriptul face fișierul de 900 px și miniatura pătrată de 300 × 300 în `thumb/`. Apoi șterge originalele (`rm`), nu rămân în repo.

## 5. Însemnarea

Adaugă în `poienel.ro/jurnal.json` un obiect:

```json
{ "id": "AAAA-LL-ZZ-subiect", "data": "AAAA-LL-ZZ", "titlu": "…",
  "text": ["paragraf 1", "paragraf 2"],
  "foto": [{ "src": "resurse/jurnal/AAAA-LL-ZZ-subiect.jpg", "alt": "ce se vede" }],
  "linkuri": [{ "titlu": "…", "url": "…" }] }
```

- Text la persoana întâi plural, 1–3 paragrafe, fapte din teren, cu legătura spre plan unde are sens (de ce s-a făcut lucrarea, ce urmează).
- `alt` descrie concret ce e în poză; ordinea pozelor urmează ordinea lucrării.
- `linkuri` relevante: planul pădurii Miyawaki (`https://schmicky.github.io/crucea/miyawaki/index-est.html`), planul de implementare (`https://github.com/schmicky/crucea/blob/master/time-lapse/plan-implementare-nord-miyawaki.md`), fișa unui obiectiv din `atractii.html#id` dacă e vorba de o vizită.
- Dacă există deja o însemnare cu aceeași dată, întreabă dacă e completare la ea sau însemnare separată.

## 6. Build, verificare, commit, push

1. `node build.mjs` din `poienel.ro/` (se oprește dacă lipsește o miniatură).
2. Verificare rapidă: pagina `jurnal.html` servită local, pozele se încarcă (naturalWidth 300), fără 404; ordinea însemnărilor descrescătoare după dată.
3. `git add -A poienel.ro`, commit cu mesaj „poienel.ro: însemnarea din <data>, <subiect>” (cu atribuirea cerută de sesiune), `git push -u origin <branch-curent>`.
4. Răspuns scurt: data și titlul însemnării, pozele (nume → ce arată), ce a rămas de făcut (publicarea cu `sync-to-ftp.ps1`).
