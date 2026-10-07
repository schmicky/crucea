# Pădure Miyawaki în colțul de nord-est — Crucea

Schema interactivă: [index-est.html](https://schmicky.github.io/crucea/miyawaki/index-est.html), desenată cu **gardul de nord orizontal, sus** (nordul geografic la 29° spre dreapta, ca săgeata). Butonul „Tipărește” scoate schema pe pagina 1, legenda pe pagina 2 și apoi **câte o pagină pentru fiecare specie**: schema numai cu puieții acelei specii (numerotați ca în CSV, ceilalți gri), unde se așază (câți în interiorul cârligului, câți pe manta de hotar, câți lângă alee și luminiș) și cum se plantează (strat, distanțe, recepție) · pozițiile: `plantare-miyawaki-est.json` (metri locali cu nordul în sus și procente pe planul nord, pentru suprapunere).

## 1. Zona

Poligonul măsurat în aplicația planului nord („Contur 1”, 8 laturi), cu latura de nord trasă până la **0,5 m de gardul de nord** (la cererea beneficiarului; poligonul ajustat e în `plantare-miyawaki-est.json`, cheia `poligon_pct`): **339.6 m²**, în **colțul de nord-est al curții, pe perdeaua de est**: 19 m de-a lungul gardului de est (la 0,3–0,5 m de el), 20 m de-a lungul gardului de nord (la 0,5 m), lat de 13–21 m. Casa e la 56 m, sera la 40 m, iazul la 25 m: niciun efect de umbră, rădăcini sau frunze asupra lor. Livada caldă rămâne la sud, în soare.

Ce face pădurea aici:

- **îngroașă perdeaua de crivăț**: vântul de nord-est lovește latura lungă la 20° de perpendiculară; 15 m de pădure protejează 150 m de curte, adică tot lotul;
- **ia locul perdelei de est planificate** pe acest colț: perdeaua nu e plantată încă, așa că cele 34 de plante ale ei din interiorul poligonului (sălcioară 9, frasin 5, dud alb 4, pin negru 4, corn 3, ulm de turkestan 3, măceș 2, păducel 2, stejar pufos 1, pom de stafide 1) **se scot din planul nord**, iar pădurea, de 3 plante/m², face aceeași treabă mai bine. Din planul perdelei e preluat **pinul negru** (33 buc., strat A, în interior): e singura specie verde iarna și ține crivățul când foioasele sunt desfrunzite;
- restul perdelei de est (la sud de poligon) și perdeaua de nord rămân cum sunt în plan; pădurea e capătul lor gros din colț.

Reguli de hotar (Cod civil art. 613): pe primii **2 m de la gardul de est și de nord stau numai arbuști** (stratul D), subarboretul de la 1 m, arborii mici și mari de la 2 m. Arbuștii de pe hotar depășesc 2 m la maturitate (lemn câinesc 3 m, porumbar 3–4 m), deci fâșia e un gard viu în înțelesul obiceiului locului, nu o retragere legală strictă; drajonii de porumbar se cosesc pe linia gardului. Mantaua de arbuști de pe gard (păducel, porumbar, lemn câinesc, măceș) ține locul sălcioarelor din planul perdelei. Umbra de după-amiază cade peste gardul de est, pe terenul vecinului, pe 19 m de hotar; perdeaua planificată ar fi făcut același lucru cu pini și frasini de 12–30 m, dar merită o vorbă cu vecinul înainte de plantare.

## 2. Cifre

| | |
|---|---:|
| suprafață | 339.6 m², din care ≈ 25 m² alee și luminiș |
| puieți | 919 |
| densitate | 3 / m² |
| specii | 30 (cele 29 din celelalte variante + pin negru) |
| arbori mari (A) | 165 |
| arbori mici (B) | 221 |
| subarboret (C) | 222 |
| arbuști, manta (D) | 311 |

**Aleea** de 80 cm e un traseu propus (8 puncte, ≈ 29 m), netezit în curbe largi: **intră dinspre nord-vest**, de pe latura 2–3 a poligonului, lângă colțul de vest, urcă spre nord-est, **ocolește luminișul la 4–5 m prin nord și est** și intră în el dinspre sud. Toate curbele au raza de cel puțin 3 m, ca roaba să treacă fără să calce marginea și ca inelul de pădure dintre alee și luminiș (2,5–3 m) să fie plantabil. **Luminișul rotund de 10 m²** (3,6 m diametru), cu băncuța de 1,6 m pe partea opusă intrării, e așezat în punctul cel mai depărtat de marginile pădurii: **cel puțin 6 m de pădure de jur împrejur**, singurul loc din poligon unde e posibil. Aleea are nevoie de bordură (scândură pe muchie sau nuiele), altfel mulciul de 20 cm curge pe pietriș. **Interiorul buclei** (inelul dintre alee și luminiș, plus zona dintre brațul de intrare și cel de întoarcere) e plantat numai cu arbuști și subarboret, cu speciile cele mai dese pe margine (lemn câinesc, porumbar, păducel, corn, sânger, dârmox, scumpie), fără niciun arbore mic sau mare: un perete verde compact de la sol, care ascunde băncuța de la intrare și de pe tot ocolul. Pozițiile aleii sunt în `plantare-miyawaki-est.json` (cheile `poteca`, `poteca_pct`, `carlig`) și se pot muta în aplicația planului nord. Arborii mari stau la peste 1,3 m de alee, arborii mici la peste 0,9 m; luminișul e înconjurat de arbuști și subarboret, deci la 4–5 ani băncuța e într-o cameră verde, nu sub coroane.

**De modificat în planul nord:** cele 34 de plante ale perdelei de est din interiorul poligonului se șterg din `pozitie-nord.json` (lista e în `plantare-miyawaki-est.json`, cheia `plante_plan_nord_in_zona`), iar comenzile de noiembrie scad cu ele: sălcioară −9, frasin −5, dud alb −4, pin negru −4, corn −3, ulm de turkestan −3, măceș −2, păducel −2, stejar pufos −1, pom de stafide −1 (ulmii sunt din rândul de pe nord, care intră acum în fâșia de 0,5 m). În schimb pădurea cere puieții din tabelele de mai jos.

## 3. Speciile

### Strat A — arbori mari
| Cod | Specie | Nume latin | Buc. | De ce | Puieți la pepiniere silvice |
|---|---|---|---:|---|---|
| Qp | Stejar pufos | *Quercus pubescens* | 39 | arborele-cheie al silvostepei dobrogene; 100 % rezistent la secetă | 3 oferte, de la 1.00 lei |
| Qb | Stejar brumăriu | *Quercus pedunculiflora* | 28 | stejarul de stepă al Dobrogei, frunze brumării | 8 oferte, de la 0.90 lei |
| Tt | Tei argintiu | *Tilia tomentosa* | 22 | crește repede, umbră, albine în iunie | 1 oferte, de la 2.50 lei |
| Qc | Cer | *Quercus cerris* | 16 | stejar rapid, tolerant la calcar | 7 oferte, de la 0.90 lei |
| Um | Ulm de câmp | *Ulmus minor* | 16 | autohton, rapid; puțini, din cauza grafiozei | 2 oferte, de la 0.90 lei |
| St | Sorb | *Sorbus torminalis* | 11 | rar, fructe pentru păsări, roșu toamna | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Pn | Pin negru | *Pinus nigra* | 33 | conifer, singura specie verde iarna: ține crivățul când foioasele sunt desfrunzite; preluat din planul perdelei de est | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |

### Strat B — arbori mici
| Cod | Specie | Nume latin | Buc. | De ce | Puieți la pepiniere silvice |
|---|---|---|---:|---|---|
| Fo | Mojdrean | *Fraxinus ornus* | 44 | flori parfumate în mai; specie de bază în pădurile Babadag | 5 oferte, de la 0.24 lei |
| Ac | Jugastru | *Acer campestre* | 38 | umple stratul mijlociu, galben toamna | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| At | Arțar tătăresc | *Acer tataricum* | 38 | samare roșii, tipic silvostepei | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Co | Cărpiniță | *Carpinus orientalis* | 38 | arborele Dobrogei de piatră; frunziș des, ține umbra | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Pp | Păr sălbatic | *Pyrus pyraster* | 22 | flori în aprilie, pere mici pentru păsări | 1 oferte, de la 2.50 lei |
| Pm | Vișin turcesc | *Prunus mahaleb* | 22 | parfum, fructe, calcar | 1 oferte, de la 1.00 lei |
| Pa | Cireș sălbatic | *Prunus avium* | 11 | crește repede, flori, cireșe pentru păsări | 6 oferte, de la 0.93 lei |
| Ms | Măr pădureț | *Malus sylvestris* | 8 | flori roz, mere mici iarna pentru păsări | 2 oferte, de la 1.50 lei |

### Strat C — subarboret
| Cod | Specie | Nume latin | Buc. | De ce | Puieți la pepiniere silvice |
|---|---|---|---:|---|---|
| Cm | Corn | *Cornus mas* | 49 | flori în martie, coarne; lemn tare | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Cr | Păducel | *Crataegus monogyna* | 49 | cuiburi, flori, fructe; ghimpos | 2 oferte, de la 1.00 lei |
| Ca | Alun | *Corylus avellana* | 33 | alune, umbră deasă la sol | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Cs | Sânger | *Cornus sanguinea* | 33 | ramuri roșii iarna, fructe pentru păsări | 2 oferte, de la 1.02 lei |
| Cc | Scumpie | *Cotinus coggygria* | 36 | roșu toamna, calcar uscat | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Pc | Corcoduș | *Prunus cerasifera* | 22 | primul înflorit, fructe | 4 oferte, de la 0.80 lei |

### Strat D — arbuști și manta
| Cod | Specie | Nume latin | Buc. | De ce | Puieți la pepiniere silvice |
|---|---|---|---:|---|---|
| Lv | Lemn câinesc | *Ligustrum vulgare* | 60 | manta deasă, semipersistent | 2 oferte, de la 1.00 lei |
| Ps | Porumbar | *Prunus spinosa* | 49 | manta ghimpoasă, flori în martie | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Vl | Dârmox | *Viburnum lantana* | 44 | frunze pâsloase, fructe roșii-negre | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Rc | Măceș | *Rosa canina* | 44 | măceșe, adăpost | 5 oferte, de la 1.00 lei |
| Ev | Salbă râioasă | *Euonymus verrucosus* | 27 | arbust de pădure de stejar; fructe toxice | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Rh | Verigar | *Rhamnus cathartica* | 27 | fluturi (lămâița), fructe pentru păsări | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Jf | Iasomie sălbatică | *Jasminum fruticans* | 22 | specie dobrogeană, flori galbene | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Sn | Soc | *Sambucus nigra* | 16 | flori, fructe; crește repede | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Cl | Bășicoasă | *Colutea arborescens* | 22 | fixează azot, păstăi pentru copii | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |

Pentru speciile care nu se găsesc la pepiniere (cărpiniță, salbă râioasă, verigar, iasomie sălbatică, bășicoasă), înlocuitorii sunt în `resurse/oferte/pepiniere-mizil-cobadin.md`.

## 4. Pregătire, plantare, întreținere

Ca în varianta de 9 × 12 m (`plan-miyawaki.md`), scalate la suprafață. Pinii negri se iau cu balot sau din container (nu rădăcină nudă) și se plantează în interior, la cel puțin 2 m unul de altul. Cantități: **35–45 m³ de compost**, mulci 15–20 cm (≈ 60 m³ tocătură sau 135 de baloți de paie), plasă de iepuri pe laturile dinspre curte (≈ 55 m; gardurile de hotar există), udare 20–25 l/m² o dată pe săptămână în anul 1 (≈ 7 500 l pe udare), nimic din anul 4. Echipă: 4 oameni plantează cei 919 de puieți în două zile.

Zăpada: perdeaua densă de pe nord-est depune troianul la 15–45 m în curte, spre livadă; să nu fie acolo o alee de acces de iarnă.

Legătura cu irigarea planului nord: zona preia vana V2 (est, uscat) și o parte din V3; are nevoie de un circuit propriu cu ≈ 900 m de tub de 16 mm cu picurătoare integrate la 33 cm, așezat șerpuit la 60 cm, sub mulci.

## 5. Cost orientativ

| | lei |
|---|---:|
| puieți din pepiniere silvice (≈ 500 buc., inclusiv pin negru) | 650–900 |
| puieți din pepiniere ornamentale (≈ 450 buc., 4–8 lei) | 1 800–3 600 |
| compost / gunoi fermentat 40 m³, cu transport | 4 500–8 000 |
| mulci | 2 000–4 000 |
| excavator mic, 2–3 zile | 1 600–3 600 |
| plasă de iepuri 55 m + țăruși | 650–900 |
| băncuță | 300–800 |
| **Total** | **≈ 11 500–22 000** |

Din comenzile de noiembrie ale planului nord dispar cele 34 de plante ale perdelelor din acest colț (≈ 150–300 lei).

Fără manoperă și fără apă.
