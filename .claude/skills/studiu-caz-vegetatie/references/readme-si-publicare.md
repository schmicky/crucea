# README-ul studiului, rândul din README-ul proiectului, jurnalul și publicarea

## `README.md` al studiului (în directorul studiului)

```
# Studiu de caz — vegetația <locul>

<Un paragraf: inventar botanic din N fotografii, data, locul exact, câți taxoni pe tipuri.>

<Un paragraf: la ce întrebare răspunde studiul și ce legătură are cu studiile anterioare (link relativ ../studiu-caz-xxx/).>

## Conținut

- `index.html` — pagina studiului: fișă per specie, în același format cu cea din studiile anterioare și din
  [planul de amenajare](../time-lapse/plan-amenajare.html) — fotografii, ce s-a văzut în teren, cerința de lumină,
  înălțimea la 2 ani / 5 ani / maturitate, dozele de udare din primii doi ani, calendarul fenologic, linkuri către
  Wikipedia și o concluzie pentru Crucea (de reținut / cu rezerve / de evitat)
- `date.py` — datele studiului (fișele, problemele, textele paginii); pagina se regenerează cu
  `python3 .claude/skills/studiu-caz-vegetatie/scripts/build.py <director>`
- `poze/thumb/p01..pNN.webp` — miniaturi, latura lungă 480 px
- `poze/mare/p01..pNN.webp` — imagini de vizualizare, latura lungă 1400 px

Numerotarea `p01`–`pNN` urmează ordinea în care au fost trimise pozele (`poze/origine.txt`). Originalele nu sunt incluse.

## De reținut

<3–4 paragrafe: speciile deja în plan și cele care ar merita să intre; lecția cea mai directă pentru proiect;
 starea vegetației la data vizitei; problemele găsite, într-o frază.>

## Precizări

Determinările sunt făcute din fotografii, la nivel de specie acolo unde caracterele o permit și la nivel de gen sau grup
acolo unde nu; cele nesigure (X din N) sunt marcate în pagină ca „determinare probabilă". Înălțimile și dozele de udare
sunt estimări pentru material de pepinieră obișnuit în clima Dobrogei, nu măsurători pe exemplarele fotografiate.

Pagina nu are dependențe externe și funcționează și deschisă direct de pe disc. Linkurile către Wikipedia se verifică
la deschiderea fișei, dacă există conexiune.
```

## Rândul din `README.md` al proiectului

Tabelul „Studii de caz din teren" (caută `## Studii de caz`): un rând nou, deasupra celor vechi, în același format:

```
| [🌿 Studiu de caz — vegetație <Loc>](https://schmicky.github.io/crucea/studiu-caz-<slug>/) | <o propoziție lungă: câți taxoni, de unde, din câte poze, la ce dată; fișă per specie în același format; lecția principală; câte probleme; concluzia pentru Crucea> |
```

Emoji diferit de cele folosite deja (🔬 Kaufland, 🌳 Tăbăcărie). `index.html` din rădăcină se generează din README la publicare,
nu se editează.

## Jurnalul

În `time-lapse/plan-implementare-nord-miyawaki.md`, secțiunea de jurnal (intrări `- **<data>**: …`, cea mai nouă prima): o intrare
cu studiul nou, taxonii, lecțiile care schimbă ceva în plan și ce s-a modificat efectiv (dacă s-a modificat ceva, ex. schema pinilor).

## Publicarea

Regula proiectului: fiecare pas se comite pe ramura de lucru, se împinge, apoi se îmbină în `master` cu
`git merge --no-ff --no-edit` și se împinge și `master`; dacă `master` de pe GitHub a avansat între timp, întâi
`git fetch origin master && git reset --hard origin/master` pe master, apoi merge. Pagina apare la
`https://schmicky.github.io/crucea/studiu-caz-<slug>/` după rularea acțiunii GitHub Pages (1–2 minute).
La final se trimit utilizatorului capturile `grila.png` și `fisa.png` (SendUserFile) și linkul paginii.
