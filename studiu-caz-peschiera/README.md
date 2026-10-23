# Studiu de caz — vegetația de la Peschiera del Garda

Inventar botanic făcut din 3 fotografii, la fața locului, pe 23 octombrie 2026, la
Peschiera del Garda (Veneto, Italia), pe malul de sud al lacului Garda: parcul de pe
bastioanele cetății și promenada de pe lac. **8 taxoni** — 4 arbori, 1 arbust și 3
conifere, aproape toți mediteraneeni sau de climă blândă.

Studiul răspunde la întrebarea din fiecare vacanță: ce din peisajul italian trece de
iernile Dobrogei și ce nu. Lacul ține iarna la −3…−5 °C (zona 8b–9a), Crucea coboară
din când în când la −20 °C (zona 7a); diferența la minimul absolut decide lista.
Studiile pereche: [banda de la Kaufland](../studiu-caz-kaufland/) (ce rezistă pe asfalt)
și [Parcul Tăbăcărie](../studiu-caz-tabacarie/) (cum arată după 40 de ani).

## Conținut

- `index.html` — pagina studiului: fișă per specie, în același format cu cea din
  studiile anterioare și din [planul de amenajare](../time-lapse/plan-amenajare.html) —
  fotografii, ce s-a văzut în teren, cerința de lumină, înălțimea la 2 ani / 5 ani /
  maturitate, dozele de udare din primii doi ani, calendarul fenologic, linkuri către
  Wikipedia și o concluzie pentru Crucea (de reținut / cu rezerve / de evitat)
- `date.py` — datele studiului (fișele, problemele, textele paginii); pagina se regenerează cu
  `python3 .claude/skills/studiu-caz-vegetatie/scripts/build.py studiu-caz-peschiera`
- `poze/thumb/p01..p03.webp` — miniaturi, latura lungă 480 px
- `poze/mare/p01..p03.webp` — imagini de vizualizare, latura lungă 1400 px

Numerotarea `p01`–`p03` urmează ordinea în care au fost trimise pozele (`poze/origine.txt`).
Originalele (3000×4000) nu sunt incluse.

## De reținut

Trei specii trec de iernile din Crucea: cedrul de Himalaya, arborele lui Iuda și teiul.
Trei nu trec: pinul umbrelă, palmierul de Chusan și dafinul îngheață la −12…−15 °C.
Două sunt la limită: chiparosul de Italia (soiuri rezistente, loc adăpostit lângă casă)
și stejarul verde, pe care Pepiniera Silvică Agigea îl are în stoc, deci experimentul
cu două exemplare în colțul adăpostit costă câțiva lei.

Silueta mediteraneană se obține cu specii de stepă: pinul negru din schema pădurii face
la 40 de ani coroana plată a pinului umbrelă, ienupărul de Virginia dă coloana
chiparosului, stejarul pufos ține frunza toată iarna.

Nicio specie din poze nu e în planurile Crucea; ar merita să intre cedrul de Himalaya
(arbore solitar pe pajiștea de sud, propus deja după Tăbăcărie), arborele lui Iuda
(arbore mic de secetă lângă casă) și stejarul verde ca experiment.

Cele trei probleme — chiparoșii elagați până la 10 m, pinii de 20 m în alveole de un
metru pătrat și solul gol sub stejarii verzi — sunt aceleași decizii proaste ca la
Constanța, în altă climă.

## Precizări

Determinările sunt făcute din fotografii, la nivel de specie acolo unde caracterele
o permit și la nivel de gen sau grup acolo unde nu; cele nesigure (3 din 8) sunt
marcate în pagină ca „determinare probabilă". Înălțimile și dozele de udare sunt
estimări pentru material de pepinieră obișnuit în clima Dobrogei, nu măsurători pe
exemplarele fotografiate; rezistențele la ger sunt cele din literatura horticolă pentru
exemplare mature.

Pagina nu are dependențe externe și funcționează și deschisă direct de pe disc.
Linkurile către Wikipedia se verifică la deschiderea fișei, dacă există conexiune.
