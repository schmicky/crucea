# Pădure Miyawaki în colțul de nord-est — Crucea

Schema interactivă: [index-est.html](https://schmicky.github.io/crucea/miyawaki/index-est.html) · pozițiile: `plantare-miyawaki-est.json` (metri locali și procente pe planul nord, pentru suprapunere).

## 1. Zona

Poligonul măsurat în aplicația planului nord („Contur 1”, 8 laturi, 73 m perimetru, **305.9 m²**), în **colțul de nord-est al curții, pe perdeaua de est**: 19 m de-a lungul gardului de est (la 0,4–0,5 m de el), 20 m de-a lungul gardului de nord (la 2,0–2,3 m), lat de 12–20 m. Casa e la 56 m, sera la 40 m, iazul la 25 m: niciun efect de umbră, rădăcini sau frunze asupra lor. Livada caldă rămâne la sud, în soare.

Ce face pădurea aici:

- **îngroașă perdeaua de crivăț**: vântul de nord-est lovește latura lungă la 20° de perpendiculară; 15 m de pădure protejează 150 m de curte, adică tot lotul;
- **ia locul perdelei de est planificate** pe acest colț: perdeaua nu e plantată încă, așa că cele 31 de plante ale ei din interiorul poligonului (sălcioară 9, frasin 5, dud alb 4, pin negru 4, corn 3, păducel 2, stejar pufos 1, măceș 1, pom de stafide 1, ulm de turkestan 1) **se scot din planul nord**, iar pădurea, de 3 plante/m², face aceeași treabă mai bine. Din planul perdelei e preluat **pinul negru** (31 buc., strat A, în interior): e singura specie verde iarna și ține crivățul când foioasele sunt desfrunzite;
- restul perdelei de est (la sud de poligon) și perdeaua de nord rămân cum sunt în plan; pădurea e capătul lor gros din colț.

Reguli de hotar (Cod civil art. 613): pe primii **2 m de la gardul de est și de nord stau numai arbuști** (stratul D), subarboretul de la 1 m, arborii mici și mari de la 2 m. Mantaua de arbuști de pe gard (păducel, porumbar, lemn câinesc, măceș) ține locul sălcioarelor din planul perdelei. Umbra de după-amiază cade peste gardul de est, pe terenul vecinului, pe 19 m de hotar; perdeaua planificată ar fi făcut același lucru cu pini și frasini de 12–30 m, dar merită o vorbă cu vecinul înainte de plantare.

## 2. Cifre

| | |
|---|---:|
| suprafață | 305.9 m², din care ≈ 12 m² alee și luminiș |
| puieți | 858 |
| densitate | 3 / m² |
| specii | 30 (cele 29 din celelalte variante + pin negru) |
| arbori mari (A) | 153 |
| arbori mici (B) | 207 |
| subarboret (C) | 207 |
| arbuști, manta (D) | 291 |

**Aleea** de 80 cm e un traseu propus (6 puncte, 17,5 m), netezit în curbe: **intră dinspre nord-vest**, de pe latura 2–3 a poligonului, lângă colțul de vest, urcă spre nord-est, cotește spre est și se întoarce spre sud-vest, în cârlig, până lângă **centrul pădurii**, într-un **luminiș rotund de 2,6 m** cu băncuța de 1,6 m, de-a curmezișul, cu fața înapoi spre alee. **Interiorul cârligului** (≈ 35 m², între brațul de intrare și cel de întoarcere) e plantat numai cu arbuști și subarboret, cu speciile cele mai dese pe margine (lemn câinesc, porumbar, păducel, corn, sânger, dârmox, scumpie), fără niciun arbore mic sau mare: un perete verde compact de la sol, care ascunde băncuța de la intrare și de pe primul braț. Pozițiile aleii sunt în `plantare-miyawaki-est.json` (cheile `poteca`, `poteca_pct`, `carlig`) și se pot muta în aplicația planului nord. Arborii mari stau la peste 1,3 m de alee, arborii mici la peste 0,9 m; luminișul e înconjurat de arbuști și subarboret, deci la 4–5 ani băncuța e într-o cameră verde, nu sub coroane.

**De modificat în planul nord:** cele 31 de plante ale perdelei de est din interiorul poligonului se șterg din `pozitie-nord.json` (lista e în `plantare-miyawaki-est.json`, cheia `plante_plan_nord_in_zona`), iar comenzile de noiembrie scad cu ele: pin negru −4, frasin −5, dud alb −4, sălcioară −9, corn −3, păducel −2, stejar pufos −1, măceș −1, pom de stafide −1, ulm de Turkestan −1. În schimb pădurea cere puieții din tabelele de mai jos.

## 3. Speciile

### Strat A — arbori mari
| Cod | Specie | Nume latin | Buc. | De ce | Puieți la pepiniere silvice |
|---|---|---|---:|---|---|
| Qp | Stejar pufos | *Quercus pubescens* | 36 | arborele-cheie al silvostepei dobrogene; 100 % rezistent la secetă | 3 oferte, de la 1.00 lei |
| Qb | Stejar brumăriu | *Quercus pedunculiflora* | 26 | stejarul de stepă al Dobrogei, frunze brumării | 8 oferte, de la 0.90 lei |
| Tt | Tei argintiu | *Tilia tomentosa* | 20 | crește repede, umbră, albine în iunie | 1 oferte, de la 2.50 lei |
| Qc | Cer | *Quercus cerris* | 15 | stejar rapid, tolerant la calcar | 7 oferte, de la 0.90 lei |
| Um | Ulm de câmp | *Ulmus minor* | 15 | autohton, rapid; puțini, din cauza grafiozei | 2 oferte, de la 0.90 lei |
| St | Sorb | *Sorbus torminalis* | 10 | rar, fructe pentru păsări, roșu toamna | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Pn | Pin negru | *Pinus nigra* | 31 | conifer, singura specie verde iarna: ține crivățul când foioasele sunt desfrunzite; preluat din planul perdelei de est | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |

### Strat B — arbori mici
| Cod | Specie | Nume latin | Buc. | De ce | Puieți la pepiniere silvice |
|---|---|---|---:|---|---|
| Fo | Mojdrean | *Fraxinus ornus* | 41 | flori parfumate în mai; specie de bază în pădurile Babadag | 5 oferte, de la 0.24 lei |
| Ac | Jugastru | *Acer campestre* | 36 | umple stratul mijlociu, galben toamna | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| At | Arțar tătăresc | *Acer tataricum* | 36 | samare roșii, tipic silvostepei | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Co | Cărpiniță | *Carpinus orientalis* | 36 | arborele Dobrogei de piatră; frunziș des, ține umbra | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Pp | Păr sălbatic | *Pyrus pyraster* | 20 | flori în aprilie, pere mici pentru păsări | 1 oferte, de la 2.50 lei |
| Pm | Vișin turcesc | *Prunus mahaleb* | 20 | parfum, fructe, calcar | 1 oferte, de la 1.00 lei |
| Pa | Cireș sălbatic | *Prunus avium* | 10 | crește repede, flori, cireșe pentru păsări | 6 oferte, de la 0.93 lei |
| Ms | Măr pădureț | *Malus sylvestris* | 8 | flori roz, mere mici iarna pentru păsări | 2 oferte, de la 1.50 lei |

### Strat C — subarboret
| Cod | Specie | Nume latin | Buc. | De ce | Puieți la pepiniere silvice |
|---|---|---|---:|---|---|
| Cm | Corn | *Cornus mas* | 46 | flori în martie, coarne; lemn tare | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Cr | Păducel | *Crataegus monogyna* | 46 | cuiburi, flori, fructe; ghimpos | 2 oferte, de la 1.00 lei |
| Ca | Alun | *Corylus avellana* | 31 | alune, umbră deasă la sol | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Cs | Sânger | *Cornus sanguinea* | 31 | ramuri roșii iarna, fructe pentru păsări | 2 oferte, de la 1.02 lei |
| Cc | Scumpie | *Cotinus coggygria* | 33 | roșu toamna, calcar uscat | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Pc | Corcoduș | *Prunus cerasifera* | 20 | primul înflorit, fructe | 4 oferte, de la 0.80 lei |

### Strat D — arbuști și manta
| Cod | Specie | Nume latin | Buc. | De ce | Puieți la pepiniere silvice |
|---|---|---|---:|---|---|
| Lv | Lemn câinesc | *Ligustrum vulgare* | 56 | manta deasă, semipersistent | 2 oferte, de la 1.00 lei |
| Ps | Porumbar | *Prunus spinosa* | 46 | manta ghimpoasă, flori în martie | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Vl | Dârmox | *Viburnum lantana* | 41 | frunze pâsloase, fructe roșii-negre | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Rc | Măceș | *Rosa canina* | 41 | măceșe, adăpost | 5 oferte, de la 1.00 lei |
| Ev | Salbă râioasă | *Euonymus verrucosus* | 26 | arbust de pădure de stejar; fructe toxice | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Rh | Verigar | *Rhamnus cathartica* | 26 | fluturi (lămâița), fructe pentru păsări | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Jf | Iasomie sălbatică | *Jasminum fruticans* | 20 | specie dobrogeană, flori galbene | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Sn | Soc | *Sambucus nigra* | 15 | flori, fructe; crește repede | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |
| Cl | Bășicoasă | *Colutea arborescens* | 20 | fixează azot, păstăi pentru copii | pepinieră ornamentală (Mizil, Cobadin) sau înlocuitorii din pepiniere-mizil-cobadin.md |

Pentru speciile care nu se găsesc la pepiniere (cărpiniță, salbă râioasă, verigar, iasomie sălbatică, bășicoasă), înlocuitorii sunt în `resurse/oferte/pepiniere-mizil-cobadin.md`.

## 4. Pregătire, plantare, întreținere

Ca în varianta de 9 × 12 m (`plan-miyawaki.md`), scalate la suprafață. Pinii negri se iau cu balot sau din container (nu rădăcină nudă) și se plantează în interior, la cel puțin 2 m unul de altul. Cantități: **30–40 m³ de compost**, mulci 15–20 cm (≈ 55 m³ tocătură sau 120 de baloți de paie), plasă de iepuri pe laturile dinspre curte (≈ 55 m; gardurile de hotar există), udare 20–25 l/m² o dată pe săptămână în anul 1 (≈ 6 500 l pe udare), nimic din anul 4. Echipă: 4 oameni plantează cei 858 de puieți în două zile.

Zăpada: perdeaua densă de pe nord-est depune troianul la 15–45 m în curte, spre livadă; să nu fie acolo o alee de acces de iarnă.

Legătura cu irigarea planului nord: zona preia vana V2 (est, uscat) și o parte din V3; are nevoie de un circuit propriu cu ≈ 900 m de tub de 16 mm cu picurătoare integrate la 33 cm, așezat șerpuit la 60 cm, sub mulci.

## 5. Cost orientativ

| | lei |
|---|---:|
| puieți din pepiniere silvice (≈ 460 buc., inclusiv pin negru) | 600–800 |
| puieți din pepiniere ornamentale (≈ 420 buc., 4–8 lei) | 1 700–3 400 |
| compost / gunoi fermentat 35 m³, cu transport | 4 000–7 000 |
| mulci | 1 800–3 500 |
| excavator mic, 2–3 zile | 1 600–3 600 |
| plasă de iepuri 55 m + țăruși | 650–900 |
| băncuță | 300–800 |
| **Total** | **≈ 10 500–20 000** |

Din comenzile de noiembrie ale planului nord dispar cele 31 de plante ale perdelei din acest colț (≈ 150–300 lei).

Fără manoperă și fără apă.
