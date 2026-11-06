# Studiu de caz — vegetația de la Peschiera del Garda

Inventar botanic făcut din 19 fotografii, la fața locului, pe 23–27 octombrie 2026, la
Peschiera del Garda (Veneto, Italia), pe malul de sud al lacului Garda: parcul de pe
bastioanele cetății, promenada de pe lac, străzile din jurul portului, jardinierele
din fața restaurantelor și a băncii, plus poze din Sirmione, din parcul Gardaland și dintr-un oraș
din apropiere. **23 de taxoni** — 7 arbori, 12 arbuști și 4 conifere, mulți
mediteraneeni sau de climă blândă, dar și câțiva care merg oriunde.

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
- `poze/thumb/p01..p19.webp` — miniaturi, latura lungă 480 px
- `poze/mare/p01..p19.webp` — imagini de vizualizare, latura lungă 1400 px

Numerotarea `p01`–`p19` urmează ordinea în care au fost trimise pozele (`poze/origine.txt`).
Originalele (3000×4000) nu sunt incluse.

## De reținut

Șapte specii trec de iernile din Crucea: carpenul (deja în pădurea Miyawaki), cedrul de
Himalaya, arborele lui Iuda, teiul, ienupărul târâtor, iedera și dracila aurie. Douăsprezece
nu trec: portocalul și bougainvillea mor în
orice iarnă (−3…−5 °C), pinul umbrelă, palmierul de Chusan, dafinul, loropetalum,
leandrul, măslinul, feijoa și iasomia stelată îngheață la −8…−15 °C, hortensia și bambusul mor de
sete (și bambusul e invaziv). Patru sunt la limită: chiparosul de Italia (soiuri rezistente, loc
adăpostit lângă casă), rozmarinul (soiuri rezistente, la zidul de sud), abelia (lângă
casă) și stejarul verde, pe care Pepiniera Silvică Agigea îl are în stoc, deci experimentul cu
două exemplare în colțul adăpostit costă câțiva lei.

Solul calcaros se vede și în Italia: loropetalum din jardinieră are cloroză de fier.
Loessul din Crucea e la fel de calcaros, deci plantele acidofile nu intră în plan.

Silueta mediteraneană se obține cu specii de stepă: pinul negru din schema pădurii face
la 40 de ani coroana plată a pinului umbrelă, ienupărul de Virginia dă coloana
chiparosului, stejarul pufos ține frunza toată iarna.

Carpenul e deja în planurile Crucea (înlocuitorul cărpiniței în pădure); ar merita să intre cedrul de Himalaya
(arbore solitar pe pajiștea de sud, propus deja după Tăbăcărie), arborele lui Iuda
(arbore mic de secetă lângă casă), stejarul verde ca experiment, rozmarinul ca
bordură aromatică la zidul de sud, ienupărul târâtor pe taluzuri și iedera pe gardul
de plasă. Gardurile vii de leandru și zidurile de iederă de aici se fac la Crucea cu
laurul portughez și photinia, deja alese; frunza argintie a măslinului o dă sălcioara, iar cățărătoarele înflorite de pe
zidurile din Sirmione se fac cu trompeta, glicina și caprifoiul.

Cele cinci probleme — chiparoșii elagați până la 10 m, pinii de 20 m în alveole de un
metru pătrat, plantele de sol acid pe calcar, gardul viu otrăvitor de leandru pe trotuar
și solul gol sub stejarii verzi — sunt aceleași decizii proaste ca la
Constanța, în altă climă.

## Precizări

Determinările sunt făcute din fotografii, la nivel de specie acolo unde caracterele
o permit și la nivel de gen sau grup acolo unde nu; cele nesigure (6 din 23) sunt
marcate în pagină ca „determinare probabilă". Înălțimile și dozele de udare sunt
estimări pentru material de pepinieră obișnuit în clima Dobrogei, nu măsurători pe
exemplarele fotografiate; rezistențele la ger sunt cele din literatura horticolă pentru
exemplare mature.

Pagina nu are dependențe externe și funcționează și deschisă direct de pe disc.
Linkurile către Wikipedia se verifică la deschiderea fișei, dacă există conexiune.
