# -*- coding: utf-8 -*-
# Datele studiului de caz Peschiera del Garda (Italia), 23 octombrie 2026. Pagina se regenerează cu
# python3 .claude/skills/studiu-caz-vegetatie/scripts/build.py studiu-caz-peschiera
R, P, V, I, F = 'repaus', 'persistent', 'vegetatie', 'inflorire', 'fructificare'

META = dict(
    titlu='Studiu de caz — vegetația de la Peschiera del Garda',
    eyebrow='Studiu de caz · 23 octombrie 2026 · Peschiera del Garda, Italia',
    h1='Vegetația de la Peschiera del Garda',
    lead=['''Inventar botanic făcut din 19 fotografii, la fața locului, pe malul de sud al lacului Garda: parcul de pe
  bastioanele cetății din Peschiera, promenada de pe lac, străzile din jurul portului, jardinierele din fața restaurantelor
  și a băncii, plus poze din Sirmione și din parcul Gardaland, pe același mal al lacului. <b>23 de taxoni</b>, mulți mediteraneeni sau
  de climă blândă: chiparos de Italia, pin umbrelă, stejar verde, măslin, portocal, bougainvillea, leandru, iasomie stelată,
  feijoa, bambus, palmier, dafin, rozmarin, loropetalum, hortensie, abelia, dar și carpen, ienupăr târâtor, iederă și dracilă, care merg
  oriunde. Lacul ține iarna la câteva grade sub zero (zona 8b–9a),
  Crucea coboară din când în când la −20 °C (zona 7a).''',
          '''De aceea studiul răspunde la o întrebare pe care ți-o pui în fiecare vacanță: ce din peisajul italian trece
  de iernile Dobrogei și ce nu. Pentru fiecare specie fișa spune ce s-a văzut, cât rezistă la ger, dacă merită un loc la
  Crucea și cu ce specie de stepă se obține aceeași siluetă fără risc. Studiile pereche: <a href="../studiu-caz-kaufland/">banda
  de la Kaufland</a> (ce rezistă pe asfalt) și <a href="../studiu-caz-tabacarie/">Parcul Tăbăcărie</a> (cum arată după 40 de ani).'''],
    concluzii_titlu='Ce arată Peschiera',
    concluzii=['''<b>Lacul face clima, nu latitudinea.</b> Peschiera e mai la nord decât Crucea, dar Garda ține iarna la
      −3…−5 °C; Dobrogea are în iernile grele −18…−22 °C. Diferența de 15 °C la minimul absolut e singurul lucru care
      contează pentru lista de mai jos: nu vara, pe care Crucea o face la fel de bine.''',
               '''<b>Șapte specii trec, douăsprezece nu, patru sunt la limită.</b> Trec: carpenul (deja în pădurea Miyawaki), cedrul
      de Himalaya, arborele lui Iuda, teiul, ienupărul târâtor, iedera și dracila aurie. Nu trec: portocalul și bougainvillea
      (−3…−5 °C, mor în orice iarnă), pinul umbrelă, palmierul de Chusan, dafinul, loropetalum, leandrul, măslinul, feijoa și
      iasomia stelată — îngheață la −8…−15 °C,
      adică o dată la 5–10 ani la Crucea — plus hortensia și bambusul, care nu îngheață, dar mor de sete (bambusul din poza 18
      are aspersorul lui). La limită: chiparosul de Italia (soiuri rezistente, loc adăpostit), stejarul verde (experiment cu 1–2 exemplare),
      rozmarinul (soiuri rezistente, la zidul de sud al casei) și abelia (lângă casă, cu arsuri în iernile grele).''',
               '''<b>Silueta mediteraneană se obține cu specii de stepă.</b> Pinul negru din schemă face la 40 de ani aceeași
      coroană plată ca pinul umbrelă; ienupărul de Virginia (în stoc la Agigea) dă coloana chiparosului; stejarul pufos
      ține frunza brună toată iarna și dă același verde-închis ca stejarul verde din aprilie până în noiembrie.''',
               '''<b>Agigea are stejar verde în pepinieră</b> (confirmat la 21 octombrie). Asta face experimentul ieftin: două
      exemplare în colțul cel mai adăpostit, lângă casă, cu mulci gros, și vezi în 5 ierni dacă rămân. Nu în perdea și nu
      în pădure, unde o iarnă grea ar lăsa goluri.''',
               '''<b>Solul calcaros se vede și în Italia.</b> Loropetalum din jardinieră, plantă de sol acid, are frunzele
      îngălbenite cu nervurile roșii — cloroză de fier pe substrat calcaros, într-o jardinieră udată. Loessul din Crucea e
      la fel de calcaros: plantele acidofile (loropetalum, hortensie, rododendron, afin) nu intră în plan, oricât ar fi de
      frumoase în ghivecele din Italia.''',
               '''<b>Greșelile sunt aceleași ca la Constanța.</b> Chiparoși elagați până la 10 m ca să se vadă vila, pini de
      20 m în alveole de un metru pătrat, sol gol și bătătorit sub stejarii verzi, jardinieră cu plante de sol acid pe
      calcar. Clima e alta, deciziile proaste sunt la fel; la tine se evită toate de la plantare.''',
               '''<b>Gardurile vii de aici se fac la tine cu alte specii.</b> Leandrul de 3 m și iedera pe plasă dau la Peschiera
      ziduri verzi tot anul; la Crucea, zidul verde e laurul portughez cu photinia (deja alese pentru stradă și cârlige),
      iar pe gardul de plasă de 1,5 m iedera face același lucru ca aici, în 3–4 ani, gratis și cu flori pentru albine în
      octombrie. Ienupărul târâtor din poza 6 e acoperitorul de sol pentru taluzuri și margini, fără cosit și fără apă.''',
               '''<b>O singură specie din poze e deja în planurile Crucea, carpenul din pădure; șase ar merita:</b> cedrul de Himalaya ca arbore
      solitar pe pajiștea de sud (propus deja după Tăbăcărie), arborele lui Iuda ca arbore mic de secetă lângă casă,
      stejarul verde ca experiment de la Agigea, rozmarinul ca bordură aromatică la zidul de sud, ienupărul târâtor pe
      taluzuri și iedera pe gardul de plasă. Pinul umbrelă, măslinul, portocalul, bougainvillea, leandrul, palmierul și hortensia rămân în Italia; cățărătoarele
      înflorite de pe zidurile din Sirmione se fac la Crucea cu trompeta (Campsis), glicina și caprifoiul.'''],
    nr_poze=19,
    footer='''Determinările sunt făcute din fotografii, la nivel de specie acolo unde caracterele o permit
  și la nivel de gen sau grup acolo unde nu — cele nesigure sunt marcate ca atare în fișă. Înălțimile și dozele de
  udare sunt estimări pentru material de pepinieră obișnuit în clima Dobrogei, nu măsurători pe exemplarele din poze;
  rezistențele la ger sunt cele din literatura horticolă pentru exemplare mature, plantele tinere sunt mai sensibile.
  Fotografiile sunt proprii, făcute la Peschiera del Garda (Veneto, Italia) pe 23 octombrie 2026, în parcul de pe
  bastioane, pe promenada lacului, pe străzile din jurul portului, la jardinierele din fața restaurantelor și a băncii, iar p13–p15 în Sirmione și p16–p18 în parcul Gardaland, pe 25 octombrie, p19 pe 27 octombrie, într-un oraș din apropiere,
  pe aceeași latură a lacului; numerotarea p1–p19 urmează ordinea în care au fost trimise. Studiile pereche:
  <a href="../studiu-caz-kaufland/">banda plantată de la Kaufland</a> și <a href="../studiu-caz-tabacarie/">Parcul Tăbăcărie</a>.<br>
  Parte din proiectul de amenajare Poienel, Crucea — <a href="../">înapoi la proiect</a>.''',
    cache='peschiera-wiki')

def luni(*spec):
    """spec: perechi (stare, nr_luni) în ordine, total 12."""
    out = []
    for s, n in spec:
        out += [s] * n
    assert len(out) == 12, out
    return out

TAXONI = [
 dict(id='cupressus-sempervirens', lum='soare', lumd="Ramurile de jos se usucă la cea mai mică umbrire; de aceea coloana rămâne plină doar în soare din toate părțile.",
      lat='Cupressus sempervirens', ro='Chiparos de Italia', tip='conifer', en='Cupressus sempervirens', row='Chiparos',
      poze=['p19', 'p01'],
      nota="Cei doi arbori columnari din prim-planul pozei 1, de 20–25 m, cu trunchiul gol pe 8–10 m și coroana îngustă, verde-închis, pe jumătatea de sus. Ramurile au fost tăiate de jos în sus de-a lungul anilor ca să se vadă vila din spate; coroana rămasă e subțire, cu vârful stâng puțin rărit și brun. Solzii mărunți, lipiți de ramuri, și portul în fus sunt ale chiparosului de Italia, forma „stricta”. Poza 19, dintr-un oraș din apropiere, pe 27 octombrie, arată cum arată aceeași specie netăiată: aliniament de 15–20 m pe o stradă în pantă, lângă un zid vechi, cu coroana plină și deasă de la sol până la vârf, îngustă ca un fus, pe arbori de 60–80 de ani. Niciun vârf uscat, nicio ramură goală — asta e forma pe care o cumperi când cumperi un chiparos.",
      h2='1,5–2,0 m', h5='4,0–5,0 m', hm='20–25 m, coroană 1,5–3 m', apa=dict(l=10, f=1),
      luni=luni((P, 2), (I, 1), (P, 6), (F, 2), (P, 1)), verdict='neutru',
      problema="Elagat până la 8–10 m: trunchiul gol stă în vânt fără protecția ramurilor, coroana rămasă e prea mică pentru înălțime, iar vârful din stânga arată uscări — fie secetă pe un arbore dezechilibrat, fie cancerul de scoarță (Seiridium) care intră prin rănile de tăiere.",
      crucea="La limită la Crucea: exemplarele mature rezistă la −15 °C, iar soiurile selectate („Totem”, „Stricta” de pepinieră europeană) trec de −18…−20 °C cu arsuri; în Constanța și Mangalia există exemplare de 30 de ani, dar în stepă, la vânt, tinerii se usucă pe partea bătută de crivăț. Dacă vrei silueta: 2–3 exemplare pe latura de sud a casei, adăpostite de perdea, și nu înainte ca perdeaua să aibă 3 m. Ieftin și sigur: ienupăr de Virginia în formă columnară, în stoc la Agigea. Și, dacă îi plantezi, lecția pozei 19: nu se taie nimic din ei, niciodată; coloana plină de la sol e tot farmecul."),
 dict(id='cedrus-deodara', lum='soare', lat='Cedrus deodara', ro='Cedru de Himalaya', tip='conifer',
      en='Cedrus deodara', row='Cedru de Himalaya', poze=['p01', 'p02'],
      nota="Coniferul cu vârful aplecat și ramurile în etaje orizontale din mijlocul pozei 1, între chiparoși, și în colțul din dreapta-sus al pozei 2. Ace moi, verde-albăstrui, în smocuri; ramurile tinere atârnă la capete. Exemplar de 15–18 m, cu coroana plină până jos acolo unde are loc — semn că a fost plantat la distanță corectă de vecini.",
      h2='1,5–2,0 m', h5='4,0–5,0 m', hm='20–30 m, coroană 10–12 m', apa=dict(l=15, f=1),
      luni=luni((P, 9), (F, 2), (P, 1)), verdict='retine',
      crucea="Aceeași concluzie ca la Tăbăcărie, unde cedrii de 25 de ani arată la fel: rezistă la −20 °C odată prins, suportă vara dobrogeană și e singurul conifer mare care rămâne frumos fără udare. Un exemplar solitar pe pajiștea de sud, cu 12 m liberi de jur împrejur; se protejează de vânt în primele 3 ierni."),
 dict(id='pinus-pinea', lum='soare', lumd="Coroana în umbrelă se formează doar cu soare din toate părțile; în aliniament des, ca aici, trunchiurile se lungesc și coroanele se contopesc.",
      lat='Pinus pinea', ro='Pin umbrelă, pin de piatră', tip='conifer', en='Pinus pinea', row='Pin de piatră',
      poze=['p03', 'p01'],
      nota="Aliniamentul de pe promenada lacului din poza 3: zeci de arbori de 15–20 m, trunchi gol pe 6–8 m, scoarță roșcată în plăci, coroană plată, în umbrelă, cu conuri mari rotunde. Trunchiurile sunt înclinate spre lac, spre lumină și contra vântului de pe uscat; alveolele din pavaj au cam un metru pătrat. În poza 1, un exemplar în stânga, deasupra stejarilor verzi.",
      h2='0,8–1,2 m', h5='2,5–3,5 m', hm='15–25 m, coroană 12–15 m', apa=dict(l=10, f=1),
      luni=luni((P, 4), (I, 1), (P, 7)), verdict='evita',
      problema="Arbori de 20 m în alveole de 1 m², cu rădăcinile sub pavaj și carosabil; trunchiurile înclinate spre lac pun toată greutatea coroanei pe o parte. Un aliniament care arată superb și costă primăria pavajul ridicat în fiecare an.",
      crucea="Simbolul peisajului italian și tocmai de aceea tentant, dar îngheață la −12…−15 °C: iernile din 2012 și 2017 au omorât exemplarele plantate pe litoralul românesc, iar la Crucea, în interior, e și mai frig. Pinul negru din schema pădurii face la 40–50 de ani aceeași coroană plată și roșcată, pe un arbore care a trecut prin toate iernile Dobrogei."),
 dict(id='quercus-ilex', lum='soare', lumd="Tânăr suportă semiumbra; matur vrea soare, altfel coroana se răsfiră.",
      lat='Quercus ilex', ro='Stejar verde', tip='arbore', en='Quercus ilex', row='Stejar verde', poze=['p02', 'p01'],
      nota="Șirul de patru arbori de 10–12 m de lângă zidul de piatră din poza 2 și masa verde-închis din mijlocul pozei 1. Frunze mici, lanceolate, pieloase, verde-închis lucios pe față și cenușii-pâsloase pe dos, cu marginea întreagă sau ușor dințată la lăstarii tineri; scoarță neagră, crăpată mărunt. Coroana e densă și verde în octombrie, când teiul de alături a început să cadă. Sub ei nu crește nimic.",
      h2='1,0–1,5 m', h5='2,5–3,5 m', hm='15–20 m, coroană 10–15 m', apa=dict(l=15, f=1),
      luni=luni((P, 3), (V, 1), (I, 1), (P, 5), (F, 2)), verdict='neutru',
      crucea="Rezistă la −15 °C, pierde frunza la −18…−20 °C și se reface din lemn; în Constanța există exemplare mature, în Crucea nu știm. Pepiniera Agigea are puieți (confirmat la 21 octombrie), deci experimentul costă câțiva lei: 2 exemplare în colțul cel mai adăpostit de lângă casă, pe sud, cu mulci gros, și se judecă după 5 ierni. Nu în perdea și nu în pădure, unde o iarnă grea ar lăsa goluri; acolo stejarul pufos, care ține frunza brună toată iarna, e varianta sigură."),
 dict(id='trachycarpus', lum='mixt', lat='Trachycarpus fortunei', ro='Palmier de Chusan', tip='arbore',
      en='Trachycarpus fortunei', row='Trachycarpus fortunei', poze=['p02', 'p03'],
      nota="Palmierul cu frunze în evantai din fundalul pozei 2, în dreapta, lângă zid, și cel din stânga pozei 3, în spatele mașinilor. Trunchi subțire, îmbrăcat în fibre brune; frunze palmate rigide. Exemplare de 4–5 m, sănătoase, plantate ca accent exotic.",
      h2='0,6–0,8 m', h5='1,5–2,0 m', hm='8–12 m', apa=dict(l=15, f=1),
      luni=luni((P, 5), (I, 1), (P, 4), (F, 1), (P, 1)), verdict='evita',
      crucea="Cel mai rezistent palmier (−15 °C scurt, cu frunzele arse), dar în stepă e un obiect străin: nu dă umbră, nu hrănește nicio pasăre sau insectă de aici, trebuie învelit iarna și arată rupt după fiecare crivăț. Nu are ce căuta în proiect."),
 dict(id='laurus', lum='mixt', lumd="Se mulțumește cu semiumbra de sub arbori; în soare plin, pe secetă, frunza se arde.",
      lat='Laurus nobilis', ro='Dafin', tip='arbust', en='Laurus nobilis', row='Dafin', poze=['p01'], incert=True,
      nota="Tufa de 3–4 m din colțul din dreapta-jos al pozei 1, cu frunze lanceolate, pieloase, verde-deschis lucios, dese până la sol. Portul în tufă cu mai multe tulpini și frunza îngustă trimit la dafin; de la distanță poate fi și laur englezesc, care are frunza mai lată și mai închisă.",
      h2='0,8–1,2 m', h5='2,0–3,0 m', hm='5–10 m', apa=dict(l=10, f=2),
      luni=luni((P, 3), (I, 1), (P, 6), (F, 2)), verdict='evita',
      crucea="Îngheață la −10…−12 °C până la sol și pornește din nou din rădăcină, deci la Crucea ar fi un arbust de un metru refăcut la fiecare 3–4 ani, nu un arbore. Dacă vrei frunza de dafin la bucătărie, un exemplar în ghiveci mare, iernat în magazie. Pentru gardul viu persistent rămâne laurul portughez, ales deja pentru stradă și cârlige."),
 dict(id='cercis', lum='soare', lat='Cercis siliquastrum', ro='Arborele lui Iuda', tip='arbore',
      en='Cercis siliquastrum', row='Arborele lui Iuda', poze=['p01'], incert=True,
      nota="Arborele cu ramuri negre, noduroase, din dreapta pozei 1, lângă chiparosul din dreapta: coroană largă și rărită, frunze rotunde rămase puține, cu pete galben-roșcate, și păstăi brun-roșcate atârnând în ciorchini. Ramificația sinuoasă și păstăile sunt ale arborelui lui Iuda; fără flori în cadru, determinarea rămâne probabilă.",
      h2='1,5–2,0 m', h5='3,0–4,0 m', hm='6–10 m, coroană 6–8 m', apa=dict(l=15, f=1),
      luni=luni((R, 3), (I, 1), (V, 5), (F, 2), (R, 1)), verdict='retine',
      crucea="Trece de −20 °C: crește în București, Constanța, Iași, pe sol calcaros și uscat, fără boli. Arbore mic, înflorit roz pe lemn în aprilie, înainte de frunze, cu păstăi care hrănesc păsările iarna. Un exemplar în fața casei sau la intrare, în soare plin, și unul la marginea pajiștii; alături de clocotișul din Tăbăcărie, e al doilea arbore mic de secetă care merită să intre în plan."),
 dict(id='tilia', lum='mixt', lumd="Tânăr suportă semiumbra; matur vrea coroana în soare.",
      lat='Tilia', cv='probabil cordata sau × europaea', ro='Tei', tip='arbore', en='Tilia', row='Tei', poze=['p03', 'p02'], incert=True,
      nota="Arborele cu frunze late, galben-verzi, din stânga pozei 3, deasupra mașinilor, și, probabil, cel din stânga pozei 2. Frunzele cordate și coloritul galben de octombrie sunt de tei; specia nu se vede de la distanță. Pe promenadă, cu apa lacului la 20 m, teiul e încă verde-galben, nu rărit ca teii din Tăbăcărie.",
      h2='2,5–3,0 m', h5='5,0–6,0 m', hm='20–30 m, coroană 12–15 m', apa=dict(l=25, f=2),
      luni=luni((R, 3), (V, 2), (I, 1), (V, 3), (F, 2), (R, 1)), verdict='neutru',
      crucea="Teii pucios și cu frunza mică vor apă în adâncime și cad din august în stepă; singurul care rezistă la Crucea e teiul argintiu, deja în plan (A48 / Tt), cu dosul frunzei alb-pâslos. Exemplarul de aici arată ce face un tei cu apă la picior, nu ce face în Dobrogea."),
 dict(id='rosmarinus', lum='soare', lumd="Soare plin și sol uscat; la umbră sau în sol greu putrezește la rădăcină.",
      lat='Salvia rosmarinus', ro='Rozmarin', tip='arbust', en='Salvia rosmarinus', row='Rozmarin', poze=['p05'],
      nota="Bordura verde-închis din prim-planul pozei 5, în jardiniera din fața restaurantului: tufe dese, culcate, de 40–50 cm, cu frunze aciculare, verzi pe față și albicioase pe dos, mirositoare. Forma târâtoare („Prostratus”), sănătoasă, fără uscări, cu câteva buruieni (trifoi, oxalis) printre tufe.",
      h2='0,3–0,5 m', h5='0,5–0,8 m', hm='0,5–1,5 m, lățime 1–2 m', apa=dict(l=5, f=1),
      luni=luni((P, 2), (I, 3), (P, 4), (I, 2), (P, 1)), verdict='neutru',
      crucea="Forma târâtoare din poză îngheață la −10 °C; soiurile verticale rezistente („Arp”, „Hill Hardy”, „Madalene Hill”) trec de −18…−20 °C pe sol uscat și drenat. La Crucea merge ca bordură aromatică la zidul de sud al casei, cu pietriș la rădăcină și fără udare după primul an, nu în câmp deschis. Înflorește din martie, când albinele n-au altceva."),
 dict(id='loropetalum', lum='mixt', lumd="Frunza rămâne purpurie doar în soare; la umbră se face verde-bronz.",
      lat='Loropetalum chinense', cv="var. rubrum", ro='Loropetalum', tip='arbust', en='Loropetalum chinense', poze=['p04', 'p05'],
      nota="Arbustul cu frunze mici, ovale, purpurii-violet din jardiniera de pe zidul de piatră (poza 4) și din spatele rozmarinului (poza 5). Pe jumătatea de jos a tufei din poza 4, frunzele sunt galben-roz cu nervurile roșii și unele s-au uscat: cloroză de fier, tipică plantelor de sol acid puse pe substrat calcaros. Specie chinezească, înrudită cu hamamelisul, plantată pentru frunza colorată.",
      h2='0,6–0,8 m', h5='1,2–1,5 m', hm='2–3 m', apa=dict(l=10, f=2),
      luni=luni((P, 2), (I, 2), (P, 8)), verdict='evita',
      problema="Cloroză de fier pe frunzele de jos: galbene cu nervuri roșii, apoi uscate. Plantă de sol acid într-o jardinieră cu substrat calcaros și apă dură; și udată, și îngrășată, tot se îngălbenește.",
      crucea="Îngheață la −10…−12 °C și cere sol acid: în loessul calcaros din Crucea ar arăta ca jumătatea de jos a tufei din poză din primul an, apoi ar muri în prima iarnă grea. Frunza purpurie o dai cu corcodușul roșu (deja în plan) sau cu dracila purpurie (Berberis thunbergii „Atropurpurea”), care rezistă la −30 °C."),
 dict(id='hydrangea', lum='umbra', lumd="Semiumbră obligatorie; în soare de stepă se ofilește zilnic de la prânz.",
      lat='Hydrangea macrophylla', ro='Hortensie', tip='arbust', en='Hydrangea macrophylla', row='Hortensie', poze=['p10', 'p04', 'p13'],
      nota="Gardul viu de 1,5 m din fața băncii, în poza 10: tufe late, frunze mari, ovale, dințate, verde-închis, și zeci de inflorescențe sferice trecute, roz-brune, lăsate pe tufă ca decor de toamnă. În poza 4, aceleași tufe în fundal, deasupra loropetalumului. Pe partea umbrită a clădirilor și udate — altfel nu ar fi avut frunza întreagă în octombrie.",
      h2='0,6–0,8 m', h5='1,0–1,5 m', hm='1,5–2 m', apa=dict(l=15, f=3),
      luni=luni((R, 3), (V, 3), (I, 3), (V, 1), (R, 2)), verdict='evita',
      crucea="Rezistă la ger, dar nu la sete: cere 15–20 l pe săptămână toată vara, semiumbră și sol acid pentru culoarea albastră. La Crucea, fără om și cu apă drămuită, e planta care moare prima în iulie. Dacă vrei o tufă cu flori mari lângă casă: hortensia paniculată (Hydrangea paniculata), care suportă soarele și seceta de două ori mai bine, sau liliacul."),
 dict(id='juniperus-tarator', lum='soare', lumd="Soare plin; la umbră se răsfiră și se dezgolește la mijloc.",
      lat='Juniperus', cv='probabil horizontalis sau sabina, forme târâtoare', ro='Ienupăr târâtor', tip='conifer', en='Juniperus horizontalis', row='Ienupăr', poze=['p06'], incert=True,
      nota="Covorul verde de 30–40 cm de pe refugiul dintre carosabil și trotuar, în poza 6: tufe culcate, dese, cu frunze solziforme și aciculare, în două nuanțe (verde-închis și verde-gălbui, probabil două soiuri amestecate), închise complet peste sol. Câteva buruieni doar în golul de la stâlp. Specia exactă nu se vede de la distanță.",
      h2='0,2–0,3 m, lățime 0,8 m', h5='0,3–0,4 m, lățime 1,5–2 m', hm='0,3–0,5 m, lățime 2–3 m', apa=dict(l=5, f=1),
      luni=luni((P, 12)), verdict='retine',
      crucea="Rezistă la −30 °C, la secetă și la vânt, acoperă solul atât de des încât nu mai trebuie cosit sau plivit; e același ienupăr ca cel din jardinierele din Tăbăcărie, în forma culcată. La Crucea: pe taluzul dinspre iaz, pe marginile parcării și pe fâșia de la stradă, 1 plantă la metru pătrat, mulcit cu pietriș. Singura condiție: soare plin."),
 dict(id='hedera-gard', lum='mixt', lumd="Pe gardul dinspre sud, pe loess uscat, frunza se arde în iulie; pe laturile de nord și est merge fără apă.",
      lat='Hedera helix', ro='Iederă, pe gard', tip='arbust', en='Hedera helix', row='Iederă', poze=['p07'],
      nota="Gardul de plasă metalică de 1,8 m din poza 7, acoperit complet de iederă în forma adultă: frunze întregi, romboidale, nu lobate, și umbele de flori verzi-gălbui deschise în octombrie, pline de muște și albine. Câteva frunze uscate la bază, unde plasa e dublată de scânduri vechi. Dincolo de gard, un leandru de 4 m.",
      h2='1,0–1,5 m pe suport', h5='gardul acoperit', hm='10–20 m pe suport', apa=dict(l=10, f=1),
      luni=luni((P, 8), (I, 2), (F, 2)), verdict='retine',
      crucea="Aceeași plantă care la Tăbăcărie urca pe pin și îl sufoca; pe un gard de plasă e cel mai ieftin zid verde: 1 plantă la 2 m, 3–4 ani până închide, zero udare după primul an pe laturile de nord și est, flori în octombrie când albinele nu mai au nimic și fructe pentru păsări în martie. La Crucea: pe gardul de plasă de 1,5 m dinspre vecini, nu pe arbori, nu pe casă."),
 dict(id='nerium', lum='soare', lat='Nerium oleander', ro='Leandru', tip='arbust', en='Nerium oleander', row='Leandru', poze=['p08', 'p09', 'p07'],
      nota="Gardul viu de 3 m de pe trotuar din poza 8: tufe dese cu frunze lanceolate, pieloase, verde-închis, în verticile de trei, tunse plat pe fața dinspre stradă. În poza 9, un exemplar liber de 3–4 m, cu flori roz în octombrie, într-o jardinieră de beton la colțul unei case. În poza 7, un leandru în spatele gardului cu iederă. Fără urme de ger sau de boli.",
      h2='1,0–1,5 m', h5='2,5–3,0 m', hm='3–5 m', apa=dict(l=10, f=1),
      luni=luni((P, 5), (I, 5), (P, 2)), verdict='evita',
      problema="Gard viu de 3 m dintr-o plantă în care toate părțile sunt otrăvitoare, pe un trotuar cu copii și câini. În Italia e obișnuit; la căsuțele de închiriat de la Crucea, lângă iaz și pajiște, nicio plantă toxică la îndemână.",
      crucea="Îngheață la −8…−10 °C: în Constanța trăiește doar în ghiveci, dus iarna la adăpost. Pe deasupra e toxic de la frunză la rădăcină. Gardul viu dens și înflorit tot anul îl dai la Crucea cu laurul portughez și photinia, deja alese, iar florile roz de vară cu taula (Spiraea japonica) sau cu lavanda."),
 dict(id='olea', lum='soare', lat='Olea europaea', ro='Măslin', tip='arbore', en='Olea europaea', row='Măslin', poze=['p11', 'p12'],
      nota="Arbore de 7–8 m cu coroană largă, rotundă, din poza 11, într-o parcare lângă bancă: frunze lanceolate, verde-cenușii pe față și argintii pe dos, lăstari lungi, subțiri, atârnând; trunchi scurt, noduros, cu baza lățită — exemplar bătrân, de 60–80 de ani, adus probabil cu balot din sud, cum se face curent în Italia. Sub el, gard viu tuns. În poza 12, coroana lui în stânga.",
      h2='1,0–1,5 m', h5='2,5–3,0 m', hm='6–10 m, coroană 6–8 m', apa=dict(l=10, f=1),
      luni=luni((P, 4), (I, 2), (P, 4), (F, 2)), verdict='evita',
      crucea="Rezistă la −8…−10 °C, soiurile cele mai dure („Frantoio”, „Leccino”) la −12…−14 °C cu pagube; la −18 °C moare până la sol. La Crucea ar trăi 5–8 ani și ar muri în prima iarnă grea. Frunza argintie și coroana rotundă le dă sălcioara (Elaeagnus angustifolia), deja în perdelele planului nord și în stoc la Agigea; la 20 de ani un exemplar solitar de sălcioară se confundă cu un măslin."),
 dict(id='abelia', lum='soare', lumd="Înflorește bogat doar în soare; în semiumbră se întinde și face jumătate din flori.",
      lat='Abelia × grandiflora', ro='Abelia', tip='arbust', en='Abelia × grandiflora', poze=['p12'],
      nota="Tufa rotundă de 1,2 m din poza 12, în fața băncii: frunze mici, ovale, lucioase, flori albe, tubulare, și caliciile roșiatice rămase după flori, care dau tufei culoarea roz-brună. Înflorește încă în 23 octombrie, din iunie. În spate, garduri vii tunse de merișor sau pittosporum; în față, dracilă aurie.",
      h2='0,6–0,8 m', h5='1,2–1,5 m', hm='1,5–2,5 m', apa=dict(l=8, f=1),
      luni=luni((P, 5), (I, 5), (P, 2)), verdict='neutru',
      crucea="Rezistă la −15…−18 °C cu frunza pierdută și vârfurile arse; pornește din lemn primăvara. În București și Constanța trăiește în grădini adăpostite. La Crucea doar lângă casă, pe sud, în locul cel mai ferit de crivăț: patru luni de flori pentru albine și fluturi, când restul grădinii s-a terminat. Nu în câmp deschis."),
 dict(id='berberis-aurea', lum='soare', lumd="Frunza galbenă apare doar în soare plin; la umbră se face verde și tufa se rărește.",
      lat='Berberis thunbergii', cv="'Aurea'", ro='Dracilă aurie', tip='arbust', en='Berberis thunbergii', row='Dracilă', poze=['p12'],
      nota="Tufele joase cu frunze mici, rotunde, galben-verzui din prim-planul pozei 12, în fața abeliei: ramuri subțiri, spinoase, frunza începe să se coloreze portocaliu la vârfuri. Plantate ca bordură de 40–50 cm, sănătoase, fără arsuri.",
      h2='0,4–0,5 m', h5='0,8–1,0 m', hm='1,0–1,5 m', apa=dict(l=5, f=1),
      luni=luni((R, 3), (V, 1), (I, 1), (V, 4), (F, 2), (R, 1)), verdict='retine',
      crucea="Rezistă la −30 °C, la secetă și la sol calcaros, fără boli, spinoasă (păsările cuibăresc în ea). Forma aurie dă pata de culoare deschisă, forma purpurie („Atropurpurea”) înlocuiește loropetalum. La Crucea: bordură lângă casă și la parcare, 3 plante la metru, sau tufe izolate pe pajiște; nu în pădure, unde e deja dracila sălbatică."),
 dict(id='citrus', lum='soare', lat='Citrus', cv='probabil × aurantium sau sinensis', ro='Portocal', tip='arbore', en='Citrus × sinensis', row='Portocal', poze=['p13'], incert=True,
      nota="Arborele de 5–6 m cu coroană rotundă, deasă, din curtea din Sirmione (poza 13): frunze pieloase, lanceolate, verde-închis lucios, cu pețiol aripat, fructe rotunde, încă verzi și câteva portocalii, de 6–8 cm, în coroană. Trunchi drept, curățat până la 2 m. Dulce sau amar nu se vede din poză; portocalul amar e cel obișnuit pe străzile din nordul Italiei. La bază, hortensii și un gard de iasomie stelată.",
      h2='1,0–1,5 m', h5='2,0–2,5 m', hm='4–6 m', apa=dict(l=15, f=2),
      luni=luni((F, 2), (P, 2), (I, 1), (P, 5), (F, 2)), verdict='evita',
      crucea="Îngheață la −5…−7 °C, deci la Crucea moare în prima iarnă, nu într-una grea. Dacă vrei fructul: un portocal amar sau un kumquat în hârdău, afară din mai în octombrie, iarna în magazie sau în casă, cum se ține și la Constanța. În grădină, în locul lui, gutuiul: coroană rotundă, frunză mare, fruct galben în octombrie, −25 °C."),
 dict(id='trachelospermum', lum='mixt', lumd="Înflorește mai bogat în soare, dar suportă și semiumbra zidurilor.",
      lat='Trachelospermum jasminoides', ro='Iasomie stelată', tip='arbust', en='Trachelospermum jasminoides', poze=['p14', 'p13'],
      nota="Cele două arcade de 3 m de la intrarea în curte (poza 14): cățărătoare cu frunze mici, ovale, pieloase, verde-închis lucios, tunse pe schelet metalic până arată ca un gard viu în formă de boltă; câteva vârfuri de lăstari ies din tunsoare. Sub arcade, un portocal pe tulpină în jardinieră rotundă. În poza 13, aceeași plantă ca gard viu, în dreapta.",
      h2='1,0–1,5 m pe suport', h5='3–4 m', hm='5–8 m pe suport', apa=dict(l=10, f=1),
      luni=luni((P, 5), (I, 2), (P, 5)), verdict='evita',
      crucea="Rezistă la −12…−15 °C la adăpostul unui zid; la Crucea, în câmp deschis, ar pierde frunza în fiecare iarnă și ar muri la prima de −18 °C. Arcada parfumată de la intrare se face cu caprifoi (Lonicera periclymenum sau L. japonica „Halliana”), care rezistă la −25 °C, înflorește din mai până în septembrie și miroase seara la fel de tare; pe gard, iedera din poza 7."),
 dict(id='bougainvillea', lum='soare', lat='Bougainvillea', ro='Bougainvillea', tip='arbust', en='Bougainvillea', poze=['p15'],
      nota="Casa de piatră din Sirmione (poza 15), acoperită de la etaj până la acoperiș de o singură plantă, cu bractee purpurii la vârf și bractee uscate, bej, pe restul tufei — a înflorit tot anul și la 23 octombrie mai are vârfurile colorate. Trunchiul gros, de 15–20 cm, iese dintr-o alveolă de un metru la colțul casei, lângă un măslin în jardinieră; exemplar de 30–40 de ani, celebru în oraș.",
      h2='1,5–2,0 m pe suport', h5='4–5 m', hm='8–12 m pe suport', apa=dict(l=10, f=1),
      luni=luni((P, 4), (I, 6), (P, 2)), verdict='evita',
      crucea="Îngheață la −3…−5 °C: plantă de ghiveci la Constanța, moartă la Crucea în noiembrie. Zidul colorat de pe casă se face în Dobrogea cu trompeta (Campsis radicans, flori portocalii din iulie în septembrie, −25 °C, cere zid solid) sau cu glicina pentru mai; purpuriul din poză îl dă o clematită (Clematis „Jackmanii”) pe spalier, cu rădăcina la umbră."),
 dict(id='carpinus', lum='mixt', lumd="Una dintre puținele foioase care cresc bine și la umbra altora; de aceea e strat B în pădure.",
      lat='Carpinus betulus', ro='Carpen', tip='arbore', en='Carpinus betulus', row='Carpen', poze=['p16'], inPlan='Co · carpen în locul cărpiniței',
      nota="Aliniamentul din poza 16 (Gardaland, 25 octombrie): arbori de 8–10 m cu 2–4 tulpini din aceeași bază, scoarță netedă, cenușie, cu caneluri, frunze ovale, dublu dințate, cu nervuri paralele adâncite, verzi-gălbui și cu primele îngălbeniri. Plantați des, la 2–3 m, ca perdea tunsă pe o parte; sub ei frunzar, nu iarbă. Exemplare sănătoase, fără uscări.",
      h2='1,5–2,0 m', h5='4,0–5,0 m', hm='15–20 m, coroană 8–10 m', apa=dict(l=15, f=1),
      luni=luni((R, 3), (I, 1), (V, 5), (F, 2), (R, 1)), verdict='retine',
      crucea="Rezistă la −30 °C și e deja în schema pădurii Miyawaki, ca înlocuitor pentru jumătate din cărpinițe (de la Țuțora, Iași). Poza arată ce face în aliniament des: perdea opacă de la sol, suportă tunderea și ține frunza uscată pe ramuri până în martie — gard viu de 3–4 m pentru latura de nord, dacă vrei foioasă în loc de ulm. Cere mai multă apă decât cărpinița în primii ani; în Dobrogea merge pe loess doar cu mulci."),
 dict(id='feijoa', lum='soare', lat='Feijoa sellowiana', cv='(Acca sellowiana)', ro='Feijoa, guava de Brazilia', tip='arbust', en='Feijoa sellowiana', poze=['p17'],
      nota="Tufa de 3–4 m din poza 17 (Gardaland, 25 octombrie), lângă stâncile artificiale și palmierii parcului: frunze ovale, groase, verde-cenușiu pe față și alb-argintiu pâslos pe dos, ramuri deschise, scoarță brun-deschis. Fără fructe vizibile în cadru (se coc în octombrie–noiembrie). De la distanță se poate confunda cu măslinul sau cu sălcioara, dar frunza e mai lată și mai rotunjită.",
      h2='0,8–1,2 m', h5='2,0–2,5 m', hm='3–5 m', apa=dict(l=10, f=1),
      luni=luni((P, 5), (I, 2), (P, 3), (F, 2)), verdict='evita',
      crucea="Rezistă la −10…−12 °C, iar fructele au nevoie de o toamnă lungă și blândă: la Crucea ar îngheța în iernile grele și n-ar rodi în cele bune. Frunza argintie și fructul comestibil le dă cătina albă (Hippophae rhamnoides, −40 °C, deja în planul nord ca F26) sau sălcioara; florile roșii cu petale cărnoase nu au înlocuitor, rămân în Italia."),
 dict(id='phyllostachys', lum='mixt', lumd="Soare sau semiumbră; la soare plin și vânt uscat frunza se răsucește și se arde.",
      lat='Phyllostachys', cv='probabil aurea sau bissetii', ro='Bambus', tip='arbust', en='Phyllostachys', row='Bambus', poze=['p18'], incert=True,
      nota="Pâlc de bambus de 5–6 m din Gardaland (poza 18): tulpini galben-verzui de 2–3 cm, cu noduri inelate, drepte, dese, la 10–20 cm una de alta; frunze lanceolate, unele îngălbenite (schimbul normal de frunze al bambusului, în toamnă și în primăvară). Sub tulpini, un strat de 10 cm din propriile frunze uscate, prin care nu răsare nimic, și un aspersor cu impact montat în mijlocul pâlcului — plantația e udată. Specia nu se poate stabili din poză; culoarea tulpinilor trimite la Phyllostachys aurea, cel mai comun bambus de grădină din Italia.",
      h2='2,0–3,0 m', h5='5–6 m', hm='6–8 m; pâlcul se întinde 2–5 m pe an', apa=dict(l=20, f=2),
      luni=luni((P, 12)), verdict='evita',
      problema="Aspersor instalat în mijlocul pâlcului: bambusul de aici trăiește din udare permanentă, iar frunzele galbene arată că nici așa nu e tocmai mulțumit. O plantă care are nevoie de irigație ca să supraviețuiască într-un parc cu personal nu are ce căuta pe un teren unde nu stă nimeni.",
      crucea="Rezistă la ger (−18 °C pentru aurea, −25 °C pentru bissetii și aureosulcata), dar nu la vara dobrogeană fără apă: 20 l pe săptămână toată vara, altfel se usucă frunza în iulie. Și e cel mai invaziv lucru pe care îl poți planta: rizomii trec pe sub gardul vecinului, prin alei și prin fundație, 2–5 m pe an, și nu mai scapi de el fără barieră de 70 cm îngropată. Nu hrănește nimic de aici. Ecranul verde înalt și rapid îl faci la Crucea cu ulmul de Turkestan și sălcioara din perdea; lecția bună din poză e stratul de frunzar de 10 cm, care ține solul curat fără erbicid și fără sapă — asta copiezi, cu mulciul din plan."),
]

PROBLEME = [
 dict(titlu='Chiparoși elagați până la 10 m', unde='poza 1', poza='p01',
      text="Cei doi chiparoși au trunchiul gol pe 8–10 m, cu ramurile tăiate de jos în sus ca să rămână vederea spre vilă. Coroana rămasă e prea mică pentru un arbore de 25 m, trunchiul stă în vânt fără sprijin și fiecare rană de tăiere e o poartă pentru cancerul de scoarță; vârful din stânga are deja uscări. La tine: coniferele columnare nu se elaghează niciodată; dacă vrei vedere printre ele, se plantează mai rar, nu se taie."),
 dict(titlu='Pini de 20 m în alveole de un metru', unde='poza 3', poza='p03',
      text="Pinii umbrelă de pe promenadă au rădăcinile sub dale și sub carosabil, în alveole de circa 1 m², și trunchiurile înclinate spre lac. Pavajul se ridică, rădăcinile se taie la fiecare reparație și arborii dezechilibrați se rup la furtună. La tine: arborii mari la cel puțin 3 m de alei, parcare și fundații, cu solul liber pe toată proiecția coroanei; alveola de un metru e bună doar pentru un arbust."),
 dict(titlu='Plante de sol acid pe substrat calcaros', unde='poza 4', poza='p04',
      text="Loropetalum și hortensia sunt plante de sol acid; jardiniera e pe calcar, cu apă dură din rețea. Rezultatul se vede pe jumătatea de jos a tufei: frunze galbene cu nervurile roșii, apoi uscate, oricât e udată. La tine: loessul din Crucea e calcaros (pH 7,5–8), deci nicio plantă acidofilă — loropetalum, hortensie cu flori albastre, rododendron, afin, camelie — nu intră în plan; pentru frunză purpurie, corcoduș roșu sau dracilă."),
 dict(titlu='Gard viu otrăvitor pe trotuar', unde='pozele 8 și 9', poza='p08',
      text="Leandrul face garduri de 3 m, dense și înflorite, dar toate părțile lui sunt otrăvitoare: frunze, flori, lemn, fum. La Peschiera stă pe trotuar, la înălțimea copiilor. La tine: la căsuțele de închiriat, lângă iaz și pajiște, nicio plantă toxică la îndemână; lista din plan e deja curată (laur portughez, photinia, lemn câinesc), ține-o așa și când adaugi ornamentale lângă casă."),
 dict(titlu='Sol gol și bătătorit sub stejarii verzi', unde='poza 2', poza='p02',
      text="Sub șirul de stejari verzi nu crește nimic: umbră densă tot anul, frunzar pielos care se descompune greu și pietriș bătătorit de pași. Solul fără acoperire se tasează și se spală la ploaie. La tine: sub persistentele dese nu se plănuiește pajiște; se lasă frunzarul și se completează cu mulci, sau se pune un acoperitor de umbră (iederă, voscovici) de la plantare."),
]
