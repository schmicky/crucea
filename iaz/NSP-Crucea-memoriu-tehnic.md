# Iaz de înot natural — Crucea, Dobrogea
## Memoriu tehnic și sinteza deciziilor de proiectare

**Amplasament:** 44,53187 N / 28,22835 E — parcelă 50 × 100 m (5.000 m²), pantă 3% orientată sud, stradă pe latura sudică
**Document însoțitor:** `NSP-Crucea-planse-tehnice.html` (planșele PL-00 … PL-06, antemăsurătoare, ordine de execuție)
**Stadiu:** revizia D · august 2026

---

## 1. Punctul de plecare și ce s-a schimbat pe parcurs

Discuția a pornit de la dorința de a reproduce abundența vegetală dintr-un făget montan umed (fotografii de referință: fag, carpen, ferigi, vinăriță, covor ierbos închis). Concluzia rapidă a fost că **modelul acela nu e transferabil** în Dobrogea: presupune 800–1000 mm precipitații anuale și umiditate atmosferică constantă, față de ~400 mm și un deficit de evapotranspirație de câteva sute de mm vara.

Modelul corect de copiat există însă local — **pădurile submediteraneene din depresiunile dobrogene** (Hagieni, Dumbrăveni, Canaraua Fetii, Esechioi), unde pe versanți nordici și în văi adăpostite se formează etaj ierbos închis în climat semiarid. Mecanismul nu e apa, ci **umbra**: etajul ierbos apare doar *după* ce există coronament.

De aici, discuția a migrat firesc spre iaz — care s-a dovedit a fi cel mai puternic element de microclimat posibil pe proprietate, dar și cel mai constrâns tehnic.

---

## 2. Condițiile de amplasament

### Solul (din profilul săpăturii pentru fosă, 1,5 m)

| Orizont | Adâncime | Descriere |
|---|---|---|
| A humifer | 0–30/40 cm | brun închis, structură bună, rădăcini |
| AB / Cca | 40–70 cm | concrețiuni albicioase — carbonat secundar (bieloglazkă) |
| C | 70–150 cm | loess galben-roșcat, omogen, poros, fără rocă compactă |

**Diagnostic:** cernoziom carbonatic pe loess adânc. Textură lut-nisipoasă / lut prăfos, pH estimat 7,5–8,3.

**Vestea bună:** niciun orizont de blocaj până la 1,5 m. Toată lista de specii arboricole rămâne deschisă, inclusiv tei argintiu și *Celtis australis*. Loessul are capacitate mare de reținere a apei disponibile (150–200 mm/m) — un arbore cu rădăcina la 3–4 m își trage rezerva din iarnă și traversează vara. Acesta e mecanismul care face pădurea posibilă în Dobrogea.

### De ce iazul de pământ este exclus

Două motive independente, fiecare suficient:

1. **Permeabilitate.** Conductivitatea hidraulică a loessului lut-prăfos: 10⁻⁵–10⁻⁶ m/s (1–10 cm/zi infiltrare). Pentru un iaz e nevoie de ≤10⁻⁸ m/s. Suntem la 2–3 ordine de mărime distanță.
2. **Colapsibilitate.** Structura poroasă a loessului e cimentată de carbonați; la umezire prelungită cimentul se dizolvă și scheletul se prăbușește. Un iaz săpat direct în loess nu doar pierde apa — își deformează cuveta, crapă și își extinde în timp traseele de scurgere.

Argilizarea (bentonită, gleizare) și baterea mecanică a cuvetei **nu sunt soluții** pe loess colapsibil: se fisurează la primul ciclu uscare/umezire.

**Concluzie: membrană EPDM, obligatoriu.**

---

## 3. Soluția adoptată — parametri de bază

| Parametru | Valoare |
|---|---|
| Zonă de înot | 6,00 × 10,00 m · adâncime 1,80 m · 60 m² · 108 m³ |
| Zonă de regenerare | bandă 2,50 m pe trei laturi · 77,5 m² |
| Amprentă totală | 11,40 × 12,70 m |
| Luciu de apă | ≈ 137 m² |
| Volum total sistem | ≈ 175 m³ |
| Raport înot : regenerare | 44 : 56 |
| Perete despărțitor | 26 ml · H 1,73 m · coamă la −0,05…−0,10 |

Regenerarea e terasată pe trei trepte (buzunar profund la perete → 0,80 m apă pentru submerse → 0,35 m apă pentru emergente), tocmai pentru a evita eroarea clasică a patului uniform de pietriș, care devine anaerob sub 40 cm și **eliberează fosfor înapoi în apă**.

Referință de proiectare: **FLL — Richtlinie für Schwimm- und Badeteiche** (standardul german, cu dimensionările tabelate).

---

## 4. Istoricul reviziilor — ce s-a corectat și de ce

### Rev. A → B (autoanaliză critică a planului inițial)

| # | Problema | Corecția |
|---|---|---|
| 1 | Skimmere amplasate în pereții despărțitori — imposibil fizic, coama e submersă 5–10 cm | Mutate pe peretele sudic, singurul la linia apei. Coincide cu direcția în care Crivățul (N/NE) împinge polenul și frunzele |
| 2 | Talpă 0,60 m subdimensionată pentru cazul de golire (19 kN/ml) | Talpă 0,90 × 0,25 cu călcâi + contraforți 0,20 × 0,60 la interax 3,00 m |
| 3 | Preaplin descărcat în loess lângă cuvetă | Dus ≥12 m în aval, bazin de infiltrare plantat |
| 4 | Bilanț de apă subestimat — ignora evapotranspirația emergentelor | Deficit corectat de la 69 la 75–85 m³/sezon |
| 5 | Lipsea complet capitolul de iernare | Adăugat: 6 puncte, gheață de 10–15 cm e normală la Crucea |

### Rev. B → C (metoda David Pagan Butler / Organic Pools)

Comparația între școala germană FLL (pat de pietriș cu percolare forțată) și școala britanică minimalistă a produs un **hibrid**:

- **Se păstrează** geometria, patul de pietriș activ și prefiltrul — pentru că la Crucea completarea masivă din puț calcaros aduce continuu nutrienți, iar un sistem pur pasiv poate fi copleșit
- **Se înlocuiește** pompa centrifugă de 300 W cu **două coloane airlift DN110** alimentate de o suflantă de membrană de 50–70 W

Câștigul: consum de la ~1.300 la ~250–300 kWh/sezon (un panou PV de 100 W acoperă tot), zero piese în mișcare în apă, și — esențial — **dafnia trece nevătămată**. O pompă centrifugă toacă zooplanctonul care face de fapt limpezirea.

Prețul: sensibilitate la înălțimea de ridicare. Jgheabul de distribuție se ține la **maximum 20 cm peste nivelul apei**; peste această cotă debitul se prăbușește neliniar. Cota se stabilește cu nivelă laser la montaj.

### Rev. C → D (amplasarea pe parcelă)

Cu strada la sud și zona de refulare a fosei tot spre sud, ordinea pe pantă se aranjează natural:

> **ecran N/NE → iaz → grădină tampon → anexă → casă → fosă + refulare → stradă**

Două corecții rezultate:

1. **Bazinul de infiltrare al preaplinului se mută lateral (est)**, nu în ax spre sud. Descărcarea în axul sudic ar satura exact coloana de loess pe care se bazează câmpul de infiltrare al fosei — pierdere de capacitate a drenajului și risc de tasare (nu contaminare: apa curge dinspre iaz).
2. **Se adaugă un al doilea ecran de arbori, pe N/NE.** Iazul poziționat în amonte e pe latura expusă Crivățului; vântul peste 137 m² de luciu poate adăuga 15–30% la deficitul de sezon. Costul în lumină e neglijabil — la 44,5°N soarele de iunie răsare la azimut ~55°, deci umbrirea încetează pe la ora 7.

Separarea rezultată iaz ↔ zonă de refulare: **28 m** (minim cerut 20), obținută prin deplasarea fosei lateral în colțul SE.

---

## 5. Bilanțul apei — constrângerea care decide proiectul

Aceasta este, de departe, cea mai serioasă limitare. Nu impermeabilizarea, nu structura.

| Parametru | Valoare |
|---|---|
| Evaporație mai–septembrie | ≈ 700 mm → 96 m³ |
| Precipitații mai–septembrie | ≈ 200 mm → 27 m³ |
| Evapotranspirație emergente | +20–50% pe ~30 m² de stand dens |
| **Deficit net de sezon** | **75–85 m³** (43–49% din volumul total) |
| Vârf iulie | ≈ 0,8 m³/zi |
| **Suprafață de captare necesară** | **230–250 m²** |
| Tanc-tampon | 20 m³ |

### Deficitul de acoperiș — punct de atenție

O casă de ~120 m² amprentă produce ≈41 m³/an, adică **jumătate** din necesar. **Anexa sau șopronul de încă ~130 m² nu e opțional** — face parte din sistemul iazului și trebuie prevăzut din faza de autorizare, cu jgheaburi dirijate spre tanc.

Alternativa — completarea integrală din puțul calcaros — transformă iazul într-un sistem evaporativ închis care concentrează carbonați, nitrați și fosfați an după an.

### Preaplinul

La cotă fixă, obligatoriu. Fără el, în 3–4 ani ai un iaz sărat. Precipitațiile de iarnă trebuie să poată spăla excesul de săruri.

> **Notă:** duritatea și calcarul nu au soluție biologică. Se rezolvă exclusiv hidraulic — preaplin plus diluție cu apă de ploaie.

---

## 6. Biologia — bugetul de fosfor

Pragul de funcționare: **fosfor total sub 10 µg/L**. La 175 m³, asta înseamnă un buget de **≈1,75 grame de fosfor în tot sistemul**.

Cifra explică toate regulile care par excesive:

- Zero pământ, zero compost, zero îngrășământ în zona de regenerare
- Plante aduse cu rădăcina spălată, în pietriș **spălat**, fără fracție fină
- Nuferii doar în coșuri izolate
- **Tăierea și îndepărtarea biomasei în octombrie** — singura cale prin care fosforul iese din sistem
- Ecranul V/SV taie și praful de la stradă, care aduce fosfor direct în luciu

### Fauna utilă

| Organism | Rol | Observații |
|---|---|---|
| **Dafnia** (*Daphnia* spp.) | pilonul limpezirii — 1–5 ml/individ/oră | apare singură; cere refugii între submerse, zero UV, zero pompă centrifugă |
| **Melci** (*Planorbarius*, *Lymnaea*) | rad biofilmul de pe liner și pereți | 20–50 exemplare la start, se înmulțesc singuri |
| **Larve de insecte** (efemeroptere, tricoptere, chironomide) | consumă detritus înainte de mineralizare | colonizează spontan în anul 2 |
| **Broaște** (*Pelophylax*, *Bufo*, *Bombina*) | mormolocii pasc alge filamentoase primăvara | vin singure dacă există rampă de acces; adulții consumă țânțari |
| **Libelule** | prădători de nevertebrate | compromis: mănâncă și dafnie, dar în densitate moderată |

**Inoculare recomandată:** în luna a doua după umplere, două găleți de apă și sediment dintr-o baltă naturală sănătoasă din zonă. Aduce dintr-un foc dafnie, ciclopi, ostracode, rotifere, protozoare și bacterii — populația de pornire care altfel se așteaptă un sezon întreg.

### De evitat categoric

- **Orice pește.** Inclusiv „peștii sanitari": amurul e macrofitofag și rade zona de regenerare; novacul și sângerul filtrează și zooplanctonul, deci elimină dafnia — clarificatorul principal. În plus, peștele nu scoate nimic din sistem: ce mănâncă revine ca excreție, într-o formă *mai* biodisponibilă. Un pește de 1 kg excretă 5–8 g fosfor pe sezon, de câteva ori bugetul total al iazului. Biomanipularea clasică pentru limpezirea unui lac constă tocmai în *îndepărtarea* peștilor.
- **Rațe și gâște** — o rață ≈ 10 g fosfor/zi
- **Raci americani** (*Procambarus*) — sapă malurile, pot perfora linerul la muchii
- **Scoici** (*Anodonta*) — filtrează impresionant, dar au mortalitate mare pe substrat de pietriș, iar o scoică moartă eliberează brusc tot fosforul acumulat
- **Sterilizator UV** — omoară dafnia
- **Filtru cu nisip** — reține particule, nu extrage fosfor

**Dacă vrei totuși pești:** un al doilea iaz, mai jos pe pantă, alimentat din preaplinul celui de înot. Bazinul de infiltrare lateral se pretează perfect — acolo încărcarea de nutrienți e binevenită, nu problematică.

---

## 7. Rezumatul soluțiilor tehnice

### Stratificația cuvetei (de jos în sus)
1. Loess afânat cu furca — **niciodată netezit sau compactat cu utilaj**
2. Nisip 0–2 mm, 5 cm
3. Geotextil 500 g/m² — *mai important decât cel de deasupra*; loessul are concrețiuni calcaroase dure care perforează EPDM-ul la prima încărcare
4. EPDM 1,52 mm (60 mil) — 18 × 18 m, sudură executată în fabrică
5. Geotextil 300 g/m² sub talpă și sub pietriș
6. Pietriș spălat 16–32 mm, 40–50 cm

Ancorare: tranșee perimetrală 30 × 30 cm, umplută după ce membrana s-a așezat sub sarcina apei.

### Peretele despărțitor
Boltari 20 cm, H = 1,73 m, armătură Ø12 vertical la 50 cm în alveole betonate, centuri din 3 în 3 rânduri, talpă continuă 0,90 × 0,25 cu călcâi sub pietriș, contraforți 0,20 × 0,60 la interax 3,00 m pe fața dinspre regenerare.

> **Regulă de exploatare, de afișat la căminul tehnic:**
> Zona de înot nu se golește niciodată fără drenarea simultană a zonei de regenerare. Cu apă la același nivel pe ambele fețe, împingerea e ~4,8 kN/ml; la golire cu pietriș saturat, ~19 kN/ml. Contraforții din rev. B fac peretele stabil și în acest caz, dar regula rămâne ca a doua barieră.

Boltarii levigă var — pH > 9 în primul sezon. Tencuială cu adaos de silicat pe fața dinspre înot, sau un an de rodaj cu apă de sacrificiu înainte de plantare.

### Hidraulica (rev. C — airlift)
- 2 × coloană airlift DN110, imersate 1,5–1,8 m, difuzor la bază
- Suflantă de membrană 50–70 W, 60–80 L/min aer
- Debit 5–8 m³/h pe coloană → 10–15 m³/h total
- Skimmer ×2 pe peretele sudic (≈65% debit) + priză de fund DN110 (≈35%)
- Prefiltru cu site/perii înainte de pat, curățat săptămânal
- Distribuitor DN75 perforat la baza pietrișului, percolare ascendentă și centrifugă
- Robineți de reglaj pe fiecare coloană, pentru echilibrare
- Consum ≈ 250–300 kWh/sezon

---

## 8. De verificat înainte de prima cupă de excavator

1. **Test de percolație** — groapă 30 × 30 × 30 cm, saturare 4 h, reumplere, măsurarea scăderii pe oră. Dă cifra reală pentru teren, nu estimarea.
2. **Analiză puț** — P total, NO₃, duritate, conductivitate. Dacă P > 30 µg/L sau NO₃ > 25 mg/L, apa de ploaie nu mai e opțională, ci singura sursă de completare acceptabilă.
3. **Analiză de sol la OSPA Constanța** — pH, humus, N-P-K, textură. Utilă mai ales pentru plantațiile de arbori și eventualii pomi fructiferi.
4. **Test cu oțet** pe un bulgăre din stratul galben — efervescență puternică confirmă carbonatul abundent.
5. **Confirmarea distanței** iaz ↔ zonă de refulare pe teren, nu doar pe plan.

## 9. Decizii rămase deschise

- **Zid sub sau peste membrană.** Planșele arată varianta „peste liner, pe geotextil dublu + talpă". Varianta cu linerul drapat peste zid elimină riscul de perforare, dar solicită membrana pe muchii, care trebuie rotunjite.
- **Trepte de acces.** Adâncimea uniformă de 1,80 m nu are intrare gradată. PL-01 propune o treaptă la −0,40 și una la −1,00 pe latura deckului.
- **Poziția exactă a casei și anexei** pe parcelă — de care depinde traseul jgheaburilor spre tancul-tampon.
- **Dimensionarea PV-ului** pentru suflantă, dacă se merge pe alimentare autonomă.

---

## 10. Calendar realist

| Etapă | Termen |
|---|---|
| Execuție cuvetă, perete, instalații | 1 sezon (toamnă–primăvară) |
| Umplere și rodaj pH | 2–4 săptămâni |
| Plantare | primăvara, după stabilizarea nivelului |
| **Primul an** | apă tulbure, alge — comportament normal al unui sistem nematurat |
| **Maturare completă** | 2 sezoane |
| Ecran de arbori funcțional | an 4–5 |

Plantarea arborilor se face **numai toamna** (octombrie–noiembrie), niciodată primăvara. Mulci 15 cm permanent — pe expunere sudică, în loess, mulciul valorează mai mult decât dublarea irigării.

---

*Document generat ca sinteză a discuției de proiectare. Verificările de la punctul 8 sunt obligatorii înainte de execuție; dimensionările din prezentul memoriu sunt calculate pe date estimate pentru zona Crucea și trebuie confirmate cu măsurători la fața locului.*
