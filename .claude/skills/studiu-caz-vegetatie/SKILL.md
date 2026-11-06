---
name: studiu-caz-vegetatie
description: Face un studiu de caz de vegetație pentru proiectul Poienel (Crucea) din fotografiile trimise de utilizator dintr-un loc real — parc, bandă plantată, perdea, grădină, pădure — ca cele de la Kaufland și din Parcul Tăbăcărie - identifică taxonii din poze, scrie fișa fiecărei specii (ce s-a văzut, lumină, creștere, udare, calendar fenologic, verdict pentru Crucea), problemele de plantare și întreținere, și generează pagina HTML în formatul comun al proiectului, README-ul, rândul din README-ul proiectului și jurnalul. Folosește-l ori de câte ori utilizatorul trimite poze cu plante dintr-un loc și cere un „studiu de caz", „inventar", „ce specii sunt aici", „analiză a vegetației", „ca la Kaufland/Tăbăcărie", sau vrea să compare un loc văzut cu planurile din Crucea, chiar dacă nu spune cuvântul „studiu".
---

# Studiu de caz de vegetație

Un studiu de caz răspunde la o întrebare a proiectului Poienel („ce rezistă pe asfalt fără udare", „cum arată după 40 de ani",
„ce greșeli se văd la maturitate") folosind un loc real pe care utilizatorul l-a fotografiat. Produsul e o pagină în formatul
comun al proiectului (fișă per specie, filtre, probleme, lupă pe poze), cu datele într-un `date.py` din care pagina se regenerează.
Modelele: `studiu-caz-kaufland/` (banda plantată, 21 de taxoni, 28 de poze) și `studiu-caz-tabacarie/` (parc, 19 taxoni, 15 poze,
`date.py` complet). Deschide `studiu-caz-tabacarie/date.py` înainte de a scrie: e etalonul de ton și de lungime.

## Pașii

1. **Stabilește întrebarea studiului și locul.** Din mesaj și din poze: ce loc e, când au fost făcute pozele (data e în mesaj sau
   în EXIF), ce întrebare a proiectului lămurește locul ăsta altfel decât studiile anterioare. Întrebarea intră în `lead` și decide
   ce cauți în poze. Dacă data lipsește, întreabă sau folosește data mesajului și spune asta în subsol.

2. **Adu pozele în proiect.** Director nou `studiu-caz-<slug>/` (slug scurt, fără diacritice). Pozele în ordinea în care au fost
   trimise, pentru că utilizatorul se referă la ele ca „poza 3":
   `python3 .claude/skills/studiu-caz-vegetatie/scripts/poze.py studiu-caz-<slug> <poza1> <poza2> …`
   (sau `--dir <director>` pentru ordinea numelor). Scriptul face `poze/thumb` (480 px) și `poze/mare` (1400 px) WebP și
   `poze/origine.txt`. Originalele nu intră în repo. Dacă `import PIL` dă eroare, rulează scriptul cu `/usr/bin/python3`
   (interpretorul de sistem are Pillow) sau instalează `pillow` cu `pip`. Pentru poze adăugate ulterior (p06, p07…), același
   script cu `--de-la <nr>` continuă numerotarea și completează `origine.txt`.

3. **Uită-te la fiecare poză, pe rând, cu Read**, și notează pentru fiecare: toate speciile vizibile (și cele din fundal și
   acoperitorii), caracterele după care le determini, vârsta plantării, starea la data vizitei, distanțele față de construcții,
   solul, întreținerea, dăunătorii. Checklist-ul complet e în `references/schema.md`. Ce nu poți determina la specie, determină la
   gen și marchează `incert=True`; o fișă sinceră la nivel de gen valorează mai mult decât o specie ghicită.

4. **Scrie `studiu-caz-<slug>/date.py`** după `references/schema.md`: `META` (titlu, antet, 1–2 paragrafe lead, 5–7 concluzii,
   subsol, cheie de cache), `TAXONI` (o fișă per taxon) și `PROBLEME` (3–8 probleme de plantare/întreținere, fiecare cu poza ei).
   Pentru `inPlan`, caută numele latin în `time-lapse/plan-amenajare-nord.html` și `miyawaki/plantare-miyawaki-est.json`.
   Concluziile se scriu la sfârșit, după fișe: ele sunt răspunsul la întrebarea de la pasul 1, nu un rezumat al fișelor; ultimul
   punct spune câte specii din loc sunt deja în planurile Crucea și care ar merita să intre.

5. **Generează și verifică.** `python3 .claude/skills/studiu-caz-vegetatie/scripts/build.py studiu-caz-<slug>` validează datele
   (chei lipsă, valori greșite, poze inexistente) și scrie `index.html`. Apoi testul de fum, din scratchpad (are nevoie de
   `playwright-core`: `npm i playwright-core` acolo, o dată pe sesiune):
   `node .claude/skills/studiu-caz-vegetatie/scripts/test.js studiu-caz-<slug> <director-capturi>`
   — numără fișele, caută imagini rupte și erori, face `grila.png` și `fisa.png`. Deschide capturile cu Read și uită-te la ele:
   textele tăiate, pozele rotite greșit sau o fișă goală se văd doar așa.

6. **Scrie README-ul studiului, rândul din README-ul proiectului și intrarea din jurnal** după `references/readme-si-publicare.md`.
   Dacă o lecție schimbă ceva în plan (cum a mutat pinii pe banda de sud studiul Tăbăcărie), spune asta explicit în concluzii, în
   jurnal și în fișa speciei, dar schimbarea planului se face doar dacă utilizatorul o cere.

7. **Publică**: commit pe ramura de lucru, push, merge `--no-ff` în `master`, push master (detalii în
   `references/readme-si-publicare.md`). Trimite capturile cu SendUserFile și linkul `https://schmicky.github.io/crucea/studiu-caz-<slug>/`.

## Ce face studiul bun

- Fișele spun ce s-a văzut, nu ce scrie în cărți: poza, locul în cadru, caracterul, starea. Partea de carte (înălțimi, apă, calendar)
  e scurtă și estimativă, iar subsolul o spune.
- Verdictul e pentru Crucea, nu pentru oraș: stepă, secetă, vânt, loess, fără udare după primii ani, case și iaz în plan. „De reținut"
  înseamnă că specia merită un loc concret în plan; „cu rezerve" că merge doar cu o condiție spusă în fișă; „de evitat" are motivul.
- Problemele sunt decizii, nu vreme: cineva a plantat prea aproape, a îngropat coletul, a lăsat solul gol, a tăiat în octombrie.
  Fiecare se termină cu ce înseamnă pentru teren („la tine: …").
- Studiile se leagă între ele: lead-ul spune la ce întrebare răspunde acesta față de cele dinainte, subsolul leagă studiile pereche.
- Pagina nu se editează de mână: orice corectură se face în `date.py` și se regenerează, ca pagina și datele să nu se despartă.
