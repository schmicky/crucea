# Schema fișierului `date.py` al unui studiu de caz

`date.py` stă în directorul studiului (lângă `index.html`) și definește trei obiecte: `META`, `TAXONI`, `PROBLEME`.
Exemplul complet, cu 19 taxoni și 6 probleme: `studiu-caz-tabacarie/date.py` din repo. Citește-l înainte să scrii unul nou:
tonul fișelor și lungimea textelor de acolo sunt etalonul.

## META — textele paginii

| cheie | ce e | exemplu |
|---|---|---|
| `titlu` | `<title>` al paginii | `Studiu de caz — vegetația din Parcul Tăbăcărie` |
| `eyebrow` | rândul mic de deasupra titlului | `Studiu de caz · 10 octombrie 2026` |
| `h1` | titlul mare | `Vegetația din Parcul Tăbăcărie` |
| `lead` | listă de 1–2 paragrafe HTML: ce loc, câte poze, câți taxoni, la ce întrebare răspunde studiul | vezi exemplul |
| `concluzii_titlu` | titlul secțiunii de concluzii | `Ce arată parcul` / `Ce arată banda` |
| `concluzii` | listă de 5–7 puncte HTML, fiecare începe cu `<b>propoziția-cheie.</b>` | vezi exemplul |
| `nr_poze` | numărul fotografiilor aduse (p01…pNN) | `15` |
| `footer` | HTML: cum s-au făcut determinările, ale cui sunt pozele, data, studiile pereche, linkul înapoi la proiect | vezi exemplul |
| `cache` | cheia localStorage pentru linkurile Wikipedia, unică per studiu | `tabacarie-wiki` |

Statisticile din antet (taxoni, arbori, arbuști, conifere, fotografii, probleme) se calculează singure.

## TAXONI — o intrare per taxon

| cheie | obligatoriu | valori / format |
|---|---|---|
| `id` | da | slug unic, latin, `pinus-nigra` |
| `lat` | da | numele latin, `Pinus nigra`; soiul separat în `cv`, ex. `"'Italica'"` |
| `ro` | da | numele românesc uzual |
| `en` | da | titlul articolului Wikipedia EN (de obicei numele latin) |
| `row` | nu | titlul articolului Wikipedia RO, dacă există |
| `tip` | da | `arbore` · `arbust` · `conifer` · `spontan` (spontan = buruiană/iederă/ierburi, fără fișă de plantare) |
| `lum` | da | `soare` · `mixt` · `umbra` |
| `lumd` | nu | o propoziție despre lumină, dacă e ceva de spus (ex. pinul moare la umbră) |
| `poze` | da | lista pozelor în care apare, `['p03', 'p07']`, prima e cea din grilă |
| `incert` | nu | `True` când determinarea e la nivel de gen/grup sau probabilă; apare ca etichetă „determinare probabilă" |
| `inPlan` | nu | codul din planurile Crucea, ex. `'A34 · Pn'`, `'F11 · Pc'`, `'Lv'` (vezi mai jos de unde se iau) |
| `nota` | da | **ce s-a văzut în poze**: unde e exemplarul, vârsta estimată, caracterele după care s-a determinat, starea în data vizitei |
| `h2`, `h5`, `hm` | da (nu la spontan) | înălțimea la 2 ani, 5 ani, maturitate, ca text: `'1,0–1,5 m'`, `'20–30 m, coroană 10 m'` |
| `apa` | da (nu la spontan) | `dict(l=litri pe udare, f=udări pe săptămână)` pentru primul an; pagina derivă anii 2 și 3 |
| `luni` | da | 12 stări, una pe lună, din `luni((R,2),(I,1),(V,7),(R,2))`; stări: `R` repaus, `P` frunziș peren, `V` vegetație, `I` înflorire, `F` fructificare |
| `verdict` | da | `retine` (de reținut) · `neutru` (cu rezerve) · `evita` (de evitat) |
| `problema` | nu | o propoziție despre ce e în neregulă cu exemplarul din poză; aprinde filtrul „Cu probleme" |
| `crucea` | da | **concluzia pentru proiect**: merită sau nu la Crucea, unde, cu ce condiții, ce lecție dă pentru plan |

Taxonii spontani (`tip='spontan'`) au `apa=None` și pot sări `h2/h5/hm`; pagina scrie „Nu se plantează — specie spontană".

### Cum se scriu `nota` și `crucea`

- `nota` e martorul: cineva care deschide poza trebuie să regăsească ce scrie acolo. Numește poza, poziția în cadru, caracterele
  (formă de frunză, scoarță, port, fructe), vârsta aproximativă și starea la data vizitei (frunză verde/galbenă/căzută, uscări, dăunători).
  Dacă determinarea e nesigură, spune cu ce se poate confunda și pune `incert=True`.
- `crucea` e judecata: se leagă de terenul din Crucea (stepă dobrogeană, secetă, vânt, sol de loess, fără udare după primii ani)
  și de planurile existente (perdea, pădure Miyawaki, pajiște, iaz). Spune dacă specia e deja în plan, unde ar intra, ce condiție are
  (distanță de case, lumină, apă) și ce lecție dă exemplarul văzut.
- Înălțimile și dozele de apă sunt estimări pentru material de pepinieră obișnuit în clima Dobrogei, nu măsurători; subsolul spune asta.

### De unde se ia `inPlan`

Codurile speciilor din planuri: `time-lapse/plan-amenajare-nord.html` (baza de specii, coduri `A..`, `F..`, `S..`) și
`miyawaki/plantare-miyawaki-est.json` (coduri de două litere din `specii[].cod`, ex. `Pn`, `Tt`, `Pc`).
Caută după numele latin: `grep -n "Pinus nigra" time-lapse/plan-amenajare-nord.html miyawaki/plantare-miyawaki-est.json`.
Formatul: codul planului nord, apoi codul Miyawaki, despărțite de ` · `; doar unul dacă specia e într-un singur plan.

## PROBLEME — ce e în neregulă în teren

Listă de `dict(titlu=, unde=, poza=, text=)`: `titlu` scurt (3–6 cuvinte), `unde` = „poza 4" / „pozele 6 și 12", `poza` = pNN
pentru miniatură, `text` = ce se vede, de ce s-a întâmplat, ce înseamnă pentru Crucea (o frază de tipul „la tine: …").
Caută probleme de plantare și întreținere, nu de climă: distanțe greșite, specii umbrite, colet îngropat, sol gol, tăieri la
moment nepotrivit, dăunători specifici, specii invazive, rădăcini sub fundații, bifurcații cu scoarță inclusă.

## Checklist de analiză a pozelor

Pentru fiecare poză, înainte de a scrie: ce specii se văd (toate, nu doar cea din prim-plan), vârsta plantării (epoci: ani '70–'80,
2000, recent), starea în data vizitei (frunzișul în raport cu data, uscări, lăstari), distanțele față de construcții, ce acoperă solul,
semne de întreținere (tăieri, mulci, terasamente, jardiniere), dăunători vizibili. Numără ce specii sunt deja în planurile Crucea și
care ar merita să intre; acestea devin ultimul punct din concluzii.
