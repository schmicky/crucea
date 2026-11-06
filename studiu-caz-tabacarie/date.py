# -*- coding: utf-8 -*-
# Datele studiului de caz Parc Tăbăcărie (Constanța), 10 octombrie 2026.
R, P, V, I, F = 'repaus', 'persistent', 'vegetatie', 'inflorire', 'fructificare'

# Textele paginii (antet, concluzii, subsol); fișele sunt în TAXONI, problemele în PROBLEME.
META = dict(
    titlu='Studiu de caz — vegetația din Parcul Tăbăcărie',
    eyebrow='Studiu de caz · 10 octombrie 2026',
    h1='Vegetația din Parcul Tăbăcărie',
    lead=['''Inventar botanic făcut din 15 fotografii, la fața locului, în zona dintre bulevard,
  blocuri și skate-park: <b>19 taxoni</b>, din trei epoci de plantare. Spre deosebire de
  banda de la Kaufland, aici sunt arbori de 40–50 de ani care au trecut prin toate verile
  Constanței fără nicio udare, lângă plantări de acum 5–10 ani în jardiniere și pe pavaj.''',
          '''De aceea parcul răspunde la altă întrebare decât Kaufland: nu „ce rezistă”, ci
  „cum arată ce rezistă după 40 de ani” — ce umbră dă, cât e de sănătos în octombrie, ce greșeli
  de plantare se văd abia la maturitate. Fiecare fișă spune ce s-a văzut în teren, cât crește
  planta, cât o uzi la început și dacă merită copiată sau ocolită la Crucea.'''],
    concluzii_titlu='Ce arată parcul',
    concluzii=['''<b>Trei epoci de plantare, una peste alta.</b> Plopii piramidali, pinii negri, salcâmii și
      catalpa sunt din anii '70–'80, cedrii și platanii de pe la 2000, iar arborele de ambră, teii,
      corcodușul roșu și ienupărul din jardiniere au venit cu skate-park-ul. Cele vechi arată ce
      rezistă 40 de ani fără îngrijire; cele noi, ce se plantează azi când nu te gândești la apă.''',
               '''<b>În 10 octombrie, fără udare, frunza e încă verde doar la unele specii.</b> Catalpa,
      sâmbovina, corcodușul roșu, cedrul, ienupărul și voscoviciul arată ca în iulie. Plopii, teii
      și platanii sunt galbeni și răriți de o lună: seceta de la sfârșitul verii se vede în ordinea
      în care lasă frunza.''',
               '''<b>Pinul negru pierde la umbră, nu la secetă.</b> Exemplarul din poza 3 are trunchi sănătos
      și coroană rară: foioasele plantate odată cu el l-au depășit. E argumentul direct pentru
      poziția pinilor din pădurea Miyawaki — pe margini, pe latura de sud și de vest.''',
               '''<b>Structura de iarnă o dau coniferele mari și acoperitorii.</b> Cedrul cu voscovici la
      bază și ienupărul în jardiniere sunt singurele pete verzi din decembrie până în martie —
      aceeași rețetă ca la Kaufland, la altă scară.''',
               '''<b>Greșelile se văd la maturitate, nu la plantare.</b> Plopul la 3 m de bloc, pinul între
      foioase, corcodușul cu bifurcație în V: toate au fost decizii de o zi, acum 40, 40 și 8 ani.
      Cele mai scumpe erori din planul tău sunt distanțele, nu speciile.''',
               '''<b>Întreținerea din parc e un catalog de ce să nu faci:</b> terasament aruncat peste
      rădăcinile chiparosului și nucului, jardinieră lăsată cu sol gol, tăieri de formare în
      octombrie. Niciuna nu costă bani de evitat, doar atenție.''',
               '''<b>Cinci specii din parc sunt deja în planurile tale</b> — pin negru, nuc, tei argintiu,
      corcoduș și lemn câinesc — și două ar merita să intre: sâmbovina, ca arbore de umbră, și
      clocotișul, ca arbore mic de secetă.'''],
    nr_poze=15,
    footer='''Determinările sunt făcute din fotografii, la nivel de specie acolo unde caracterele o permit
  și la nivel de gen sau grup acolo unde nu — cele nesigure sunt marcate ca atare în fișă.
  Înălțimile și dozele de udare sunt estimări pentru material de pepinieră obișnuit în clima
  Dobrogei, nu măsurători pe exemplarele din poze. Fotografiile sunt proprii, făcute în Parcul
  Tăbăcărie din Constanța pe 10 octombrie 2026; numerotarea p1–p15 urmează ordinea în care au
  fost trimise. Studiul pereche: <a href="../studiu-caz-kaufland/">banda plantată de la Kaufland</a>.<br>
  Parte din proiectul de amenajare Crucea — <a href="../">înapoi la proiect</a>.''',
    cache='tabacarie-wiki')

def luni(*spec):
    """spec: perechi (stare, nr_luni) în ordine, total 12."""
    out = []
    for s, n in spec:
        out += [s] * n
    assert len(out) == 12, out
    return out

TAXONI = [
 dict(id='populus-italica', lum='soare', lat="Populus nigra", cv="'Italica'", ro='Plop piramidal',
      tip='arbore', en='Lombardy poplar', row='Plop negru', poze=['p01', 'p08'],
      nota="Aliniament vechi, de 40–50 de ani, la 3–4 m de calcanul blocului. Coroană columnară, trunchi cu scoarță adânc brăzdată. În 10 octombrie frunzișul e deja pătat de galben și rărit la vârf — cade devreme la secetă.",
      h2='4,0–5,0 m', h5='9,0–12 m', hm='25–30 m, coroană 3–5 m', apa=dict(l=30, f=2),
      luni=luni((R, 2), (I, 1), (V, 7), (R, 2)), verdict='neutru',
      problema="Plantat la 3–4 m de bloc: rădăcini superficiale care caută apa de sub fundație, lemn casant la vânt și o coroană care în 10 octombrie e deja galbenă și rărită.",
      crucea="Cel mai rapid ecran vertical care există — 1,5–2 m pe an — dar trăiește 40–60 de ani, rupe la furtună și dă puf în mai. Doar ca ecran provizoriu la peste 15 m de orice construcție, nu lângă casă."),
 dict(id='populus-alba', lum='soare', lat='Populus alba', ro='Plop alb', tip='arbore', en='Populus alba',
      row='Plop alb', poze=['p08'], incert=True,
      nota="Exemplarul cu coroană largă din mijlocul pozei 8, între doi plopi piramidali. Frunzele cu dos alb-pâslos și coroana neregulată îl deosebesc de vecini; de la distanță poate fi și plop cenușiu.",
      h2='3,0–4,0 m', h5='7,0–9,0 m', hm='20–25 m', apa=dict(l=20, f=1),
      luni=luni((R, 2), (I, 1), (V, 7), (R, 2)), verdict='evita',
      crucea="Specie de luncă, dar rezistă bine și pe stepă. Problema e că drajonează la 10–15 m de trunchi: într-o grădină cu pajiște și alei răsare peste tot. Pentru perdea există plopul cenușiu sau, mai bine, speciile din planul tău."),
 dict(id='celtis', lum='soare', lumd="Suportă căldura reflectată de asfalt mai bine decât teiul sau platanul.",
      lat='Celtis australis', ro='Sâmbovină', tip='arbore', en='Celtis australis', row='Sâmbovină',
      poze=['p02'], incert=True,
      nota="Arbore de aliniament pe bulevard, la marginea parcului. Frunze lanceolate, dințate, aspre, cu baza asimetrică și vârf prelung; coroană deasă și încă verde în octombrie, când platanii de peste drum sunt deja galbeni. Fără fructe vizibile în cadru, de aceea determinarea rămâne probabilă (ar putea fi și Celtis occidentalis).",
      h2='2,5–3,0 m', h5='5,0–6,0 m', hm='15–20 m, coroană 10–12 m', apa=dict(l=20, f=2),
      luni=luni((R, 3), (I, 1), (V, 5), (F, 2), (R, 1)), verdict='retine',
      crucea="Arborele de umbră al Dobrogei: rădăcină adâncă, zero boli, frunza rămâne verde până în noiembrie fără apă. Un exemplar solitar pe pajiște sau la parcare dă mai multă umbră decât orice tei, cu jumătate din apă."),
 dict(id='pinus-nigra', lum='soare', lumd="Specie de lumină plină: ramurile de jos mor de îndată ce le umbrește ceva.",
      lat='Pinus nigra', ro='Pin negru', tip='conifer', en='Pinus nigra', row='Pin negru', poze=['p03'],
      inPlan='A34 · Pn',
      nota="Exemplar de 10–12 m, înghesuit între foioase cu frunze compuse. Coroana e rară, cu ace doar la vârfurile ramurilor, multe conuri și partea de jos complet uscată; o iederă urcă pe trunchi. Trunchiul e drept și sănătos — pinul a pierdut lupta pentru lumină, nu cu seceta.",
      h2='1,0–1,5 m', h5='2,5–4,0 m', hm='20–30 m', apa=dict(l=10, f=1),
      luni=luni((P, 4), (I, 1), (P, 4), (F, 2), (P, 1)), verdict='retine',
      problema="Coroană rară și baza uscată pe 5–6 m: foioasele vecine l-au ajuns din urmă și l-au umbrit. Iedera de pe trunchi mai ia din puțina lumină rămasă.",
      crucea="Lecția cea mai directă pentru pădurea Miyawaki: pinul negru rezistă la orice secetă, dar nu rezistă la umbră. Cele 33 de exemplare din schemă trebuie să stea pe margini, pe latura de sud și de vest, unde nu le ajunge din urmă stejarul sau teiul; schema a fost refăcută după acest studiu: toate cele 33 stau acum pe banda de sud, la 1,2–4 m de marginea dinspre grădină; înainte, 8 dintre ele erau în interior, la peste 4 m, și în 15 ani ar fi arătat ca acesta."),
 dict(id='ailanthus', lum='soare', lat='Ailanthus altissima', ro='Cenușer, fals oțetar', tip='arbore',
      en='Ailanthus altissima', row='Cenușer', poze=['p03'], incert=True,
      nota="Arborii cu frunze mari, penate, din stânga și din dreapta pinului din poza 3. Foliolele late, ramurile groase și portul deschis sunt ale cenușerului; de la distanță se poate confunda cu salcâmul, care are foliole mici și rotunjite.",
      h2='3,0–4,0 m', h5='7,0–9,0 m', hm='15–25 m', apa=dict(l=10, f=1),
      luni=luni((R, 4), (V, 2), (I, 1), (V, 1), (F, 2), (R, 2)), verdict='evita',
      crucea="Cea mai invazivă specie de arbore din România: drajonează la 20 m, răsare din semințe peste tot și otrăvește solul din jur. Dacă apare în pădurea ta sau în perdea, se scoate cu rădăcină în primul an, înainte să drajoneze."),
 dict(id='robinia', lum='soare', lat='Robinia pseudoacacia', ro='Salcâm', tip='arbore',
      en='Robinia pseudoacacia', row='Salcâm', poze=['p04', 'p13'], incert=True,
      nota="Frunze penate cu foliole mici, ovale, în dreapta chiparosului din poza 4 și în colțul din stânga-sus al pozei 13. Arbore din vechile plantări ale parcului, probabil însămânțat de la sine.",
      h2='3,0–4,0 m', h5='7,0–9,0 m', hm='20–25 m', apa=dict(l=10, f=1),
      luni=luni((R, 4), (I, 2), (V, 3), (F, 1), (R, 2)), verdict='neutru',
      crucea="Specia perdelelor clasice din Dobrogea: fixează azot, crește pe orice, dă miere. Dar drajonează, are spini și scapă de sub control. În perdeaua ta sunt deja specii mai cuminți; salcâmul rămâne o opțiune doar pentru lemn de foc pe o parcelă separată."),
 dict(id='juglans', lum='soare', lat='Juglans regia', ro='Nuc', tip='arbore', en='Juglans regia',
      row='Nuc', poze=['p04'], incert=True, inPlan='F6',
      nota="Arborele cu frunze mari, compuse din 5–7 foliole late, îngălbenite, din dreapta chiparosului. Crește pe un taluz peste care s-a aruncat recent pământ cu pietre.",
      h2='2,0–2,5 m', h5='4,0–6,0 m', hm='20–25 m, coroană 15 m', apa=dict(l=30, f=2),
      luni=luni((R, 3), (I, 1), (V, 4), (F, 2), (R, 2)), verdict='retine',
      crucea="E deja în plan (F6). Confirmarea de aici: suportă solul sărac și seceta odată prins. De reținut că sub coroana lui nu crește aproape nimic — juglona din frunze și rădăcini inhibă vecinii — deci rămâne la cel puțin 15 m de pădurea Miyawaki și de straturile de legume."),
 dict(id='leyland', lum='soare', lat='× Cuprocyparis leylandii', ro='Chiparos Leyland', tip='conifer',
      en='Leyland cypress', poze=['p04'], incert=True,
      nota="Conifer dens, larg-piramidal, de 7–8 m, cu frunze solzoase verzi și ramuri care pornesc de jos. Portul și culoarea sunt de Leyland; dacă frunzișul ar fi fost albăstrui, ar fi fost chiparos de Arizona, care merge chiar mai bine pe secetă.",
      h2='2,0–3,0 m', h5='5,0–7,0 m', hm='20–25 m, coroană 5–6 m', apa=dict(l=20, f=2),
      luni=luni((P, 12)), verdict='neutru',
      problema="Terasament proaspăt aruncat peste jumătate din zona rădăcinilor, cu pietre și moloz; coletul îngropat sub 30–40 cm de pământ e cea mai sigură cale de a usca un conifer în 2–3 ani.",
      crucea="Cel mai rapid gard viu veșnic verde, 1 m pe an, dar bea mult, se usucă pe interior și la 10 ani cere tuns cu platforma. Pentru ecran de iarnă rapid, chiparosul de Arizona sau pinul negru rezistă mai bine la vara dobrogeană."),
 dict(id='catalpa', lum='soare', lat='Catalpa bignonioides', ro='Catalpă', tip='arbore',
      en='Catalpa bignonioides', row='Catalpa bignonioides', poze=['p07', 'p12'],
      nota="Exemplar bătrân, cu ramuri orizontale lungi de 6–7 m peste alee, frunze mari cordate încă verzi și păstăi lungi atârnate. Din toți foioșii parcului, e cel cu frunzișul cel mai sănătos în 10 octombrie.",
      h2='2,5–3,0 m', h5='5,0–6,0 m', hm='12–15 m, coroană 10–12 m', apa=dict(l=20, f=2),
      luni=luni((R, 4), (V, 1), (I, 1), (V, 2), (F, 2), (R, 2)), verdict='retine',
      crucea="La Kaufland era forma globulară; aici e forma naturală, și arată ce dă în 40 de ani: cea mai lată umbră pe metru de trunchi, flori albe în iunie, frunza verde până la brumă fără udare. Un singur exemplar lângă masa de picnic ajunge."),
 dict(id='platanus', lum='soare', lat='Platanus × acerifolia', ro='Platan', tip='arbore', en='London plane',
      row='Platan', poze=['p06', 'p12'],
      nota="Frunze palmat-lobate cu pete galben-brune mărunte pe toată suprafața și margini arse; multe frunze deja brune în coroană. Trunchi cu scoarța exfoliată în plăci. Pe bulevard, platanii sunt galbeni de la jumătatea lui septembrie.",
      h2='3,0–3,5 m', h5='6,0–7,0 m', hm='25–30 m', apa=dict(l=30, f=2),
      luni=luni((R, 3), (I, 1), (V, 5), (F, 2), (R, 1)), verdict='evita',
      problema="Pete decolorate mărunte pe fața superioară a frunzelor și puncte negre pe dos — ploșnița platanului (Corythucha ciliata), prezentă pe toți platanii din Constanța; peste ea, marginile arse de secetă. Nu există tratament practic pentru un arbore de 20 m.",
      crucea="Arbore de bulevard: cere 15 m de coroană și apă în adâncime, iar în Dobrogea vine la pachet cu ploșnița care îl îngălbenește din august. Nu."),
 dict(id='tilia', lum='mixt', lumd="Tânăr suportă semiumbra; matur vrea coroana în soare.",
      lat='Tilia tomentosa', ro='Tei argintiu', tip='arbore', en='Tilia tomentosa', row='Tei argintiu',
      poze=['p09', 'p13'], incert=True, inPlan='A48 · Tt',
      nota="Doi tei tineri, de 5–6 m, cu frunze cordate, dințate, deja galbene în 10 octombrie — unul într-o insulă pavată lângă skate-park, altul pe gazon lângă alee. Dosul palid al frunzelor indică teiul argintiu, dar fără flori sau fructe în cadru poate fi și tei cu frunză mică.",
      h2='2,5–3,0 m', h5='5,0–6,0 m', hm='20–30 m', apa=dict(l=30, f=2),
      luni=luni((R, 3), (V, 2), (I, 2), (V, 1), (F, 2), (R, 2)), verdict='retine',
      crucea="E în ambele planuri (A48 în nord, Tt în pădure). Aici se vede și limita lui: pe pavaj, fără udare, lasă frunza cu o lună mai devreme decât catalpa și sâmbovina. În pădurea Miyawaki, cu picurare în primii 3 ani, nu e o problemă; ca arbore solitar la parcare e."),
 dict(id='liquidambar', lum='soare', lumd="Coloritul de toamnă apare doar în soare plin; la umbră rămâne verde-galben.",
      lat='Liquidambar styraciflua', ro='Arbore de ambră', tip='arbore', en='Liquidambar styraciflua',
      row='Liquidambar styraciflua', poze=['p10'],
      nota="Arbore tânăr, 7–8 m, cu frunze stelate în cinci lobi, în același timp verzi, galbene, portocalii și vișinii — cel mai spectaculos colorit din parc. Scoarță brăzdată, trunchi drept, plantat lângă gardul skate-park-ului.",
      h2='2,0–2,5 m', h5='4,0–5,0 m', hm='20–25 m', apa=dict(l=30, f=2),
      luni=luni((R, 3), (I, 1), (V, 5), (F, 2), (R, 1)), verdict='neutru',
      crucea="Cel mai frumos arbore de toamnă care crește în România, dar vrea sol reavăn, ușor acid; pe calcarul și seceta din Crucea face cloroză fără picurare permanentă. Dacă îl vrei, unul singur, la vedere, pe linia de picurare, nu în pădure."),
 dict(id='cedrus', lum='soare', lat='Cedrus deodara', ro='Cedru de Himalaya', tip='conifer',
      en='Cedrus deodara', row='Cedru de Himalaya', poze=['p11', 'p09', 'p08'],
      nota="Ace moi, verde-albăstrui, în smocuri, ramuri cu vârful aplecat; trunchi gros, cu scoarța în plăci, în poza 11. Un exemplar lângă tei, altul la marginea din dreapta a pozei 8. Toate cu frunzișul des și sănătos.",
      h2='1,5–2,0 m', h5='4,0–5,0 m', hm='20–30 m, coroană 10–12 m', apa=dict(l=15, f=1),
      luni=luni((P, 9), (F, 2), (P, 1)), verdict='retine',
      crucea="Dintre coniferele mari e cel care suportă cel mai bine vara dobrogeană, odată prins. Un singur exemplar pe pajiștea de sud ar da la 20 de ani umbră și adăpost de iarnă pe 100 m²; cere însă 12 m liberi de jur împrejur și pierde vârful la vânt puternic când e tânăr."),
 dict(id='prunus-pissardii', lum='soare', lumd="La umbră frunza devine verde-brună, nu vișinie.",
      lat='Prunus cerasifera', cv="'Pissardii'", ro='Corcoduș roșu', tip='arbore', en='Prunus cerasifera',
      row='Corcoduș', poze=['p15', 'p14'], inPlan='F11 · Pc',
      nota="Exemplar de 5–6 m, cu frunze vișinii-închise pe toată coroana, în plină sănătate în octombrie, lângă gardul skate-park-ului. Trunchiul se bifurcă de la 1 m în două brațe aproape egale; pe unul dintre ele e o tăietură recentă, de 5–6 cm.",
      h2='2,0–2,5 m', h5='4,0–5,0 m', hm='6–8 m', apa=dict(l=15, f=2),
      luni=luni((R, 2), (I, 2), (V, 3), (F, 2), (V, 1), (R, 2)), verdict='retine',
      problema="Bifurcație în V, cu scoarță inclusă între brațe — punctul în care se despică la furtună. Tăietura recentă e corectă ca unghi, dar făcută în octombrie, când rana nu mai apucă să se închidă înainte de iarnă.",
      crucea="Specia e deja în plan (F11 și Pc). Forma roșie e același arbore, doar că frunza vișinie ține din aprilie până în noiembrie fără nicio udare, cum se vede aici. Ca accent de culoare lângă alee, unul sau doi; la formare, alege un singur ax de la început."),
 dict(id='juniperus-pfitzeriana', lum='soare', lumd="La umbră se răsfiră și pierde ramurile de jos.",
      lat='Juniperus × pfitzeriana', cv='sau sabina', ro='Ienupăr Pfitzer', tip='conifer',
      en='Juniperus × pfitzeriana', row='Ienupăr', poze=['p05', 'p08'], incert=True,
      nota="Tufe late, de 0,8–1 m înălțime și 2–3 m lățime, cu ramuri arcuite și frunziș verde-deschis, în jardiniere de beton lângă clădirea de la intrare; același ienupăr formează gardul viu de-a lungul gardului din poza 8.",
      h2='0,5–0,7 m', h5='1,0–1,2 m', hm='1,5 m înălțime, 3–4 m lățime', apa=dict(l=8, f=1),
      luni=luni((P, 3), (V, 4), (P, 5)), verdict='retine',
      problema="Jardiniera e pe jumătate goală: pământ bătătorit, pir și iarbă uscată. Fără mulci și cu ienupărul plantat prea rar, suprafața neacoperită se umple de buruieni.",
      crucea="Aceeași concluzie ca la Kaufland: zero întreținere, acoperă solul în 3 ani, rămâne verde iarna. Se plantează la 1,2–1,5 m unul de altul și se mulcește între ei până se închid. Nu lângă păr sau păducel, dacă e J. sabina (rugina părului)."),
 dict(id='cotoneaster-horizontalis', lum='mixt', lumd="Fructifică mai bogat în soare, dar acoperă solul și sub coroana cedrului.",
      lat='Cotoneaster horizontalis', ro='Voscovici târâtor', tip='arbust', en='Cotoneaster horizontalis',
      row='Cotoneaster', poze=['p11', 'p09'],
      nota="Tufă culcată, cu ramuri în „os de pește”, frunze mici rotunde și fructe roșii dese, la baza cedrului; ramurile ies peste capacul de canal și peste bordură. Lemnul gros de la bază arată 10–15 ani de vârstă.",
      h2='0,4–0,5 m', h5='0,7–0,9 m', hm='1 m înălțime, 2–3 m lățime', apa=dict(l=5, f=1),
      luni=luni((P, 3), (V, 1), (I, 2), (V, 2), (F, 4)), verdict='retine',
      crucea="A treia confirmare, după Kaufland: cel mai bun acoperitor de sol pentru Dobrogea — merge sub conifere, pe pavaj, fără udare, și ține fructe roșii din septembrie până în ianuarie. Pentru taluzuri, marginea aleilor și sub arborii solitari."),
 dict(id='hedera', lum='umbra', lat='Hedera helix', ro='Iederă', tip='spontan', en='Hedera helix',
      row='Iederă', poze=['p03'],
      nota="Urcă pe trunchiul pinului negru până la 3–4 m. Probabil venită din vechile plantări de la baza blocurilor, nu plantată acolo.",
      h2='—', h5='—', hm='20–30 m pe suport', apa=None,
      luni=luni((P, 8), (I, 2), (F, 2)), verdict='neutru',
      crucea="Acoperitor de sol la umbră deasă, unde nu merge nimic altceva, și hrană pentru albine în octombrie. Pe trunchiuri însă ia lumina ramurilor de jos și ține umezeala pe scoarță — în pădurea Miyawaki, dacă apare, se taie la bază."),
 dict(id='ligustrum', lum='mixt', lat='Ligustrum', cv='probabil ovalifolium', ro='Lemn câinesc, gard viu tuns',
      tip='arbust', en='Ligustrum ovalifolium', row='Lemn câinesc', poze=['p01', 'p03'], incert=True,
      inPlan='Lv',
      nota="Gardul viu scund, tuns, de la baza blocului din poza 1 și din spatele pinului din poza 3. Frunze mici, ovale, lucioase, încă verzi; determinarea e după port și frunziș, de la distanță.",
      h2='0,8–1,0 m', h5='1,5–2,0 m', hm='3–4 m netuns', apa=dict(l=8, f=2),
      luni=luni((P, 4), (V, 1), (I, 1), (V, 2), (F, 4)), verdict='retine',
      crucea="Cea mai ieftină bordură tunsă și singura care suportă umbra de sub arbori. În pădure ai deja ruda lui sălbatică, lemnul câinesc (Lv), în inelul din jurul luminișului — aici se vede că rezistă 40 de ani fără nimic."),
 dict(id='koelreuteria', lum='soare', lat='Koelreuteria paniculata', ro='Clocotiș, copacul lampion',
      tip='arbore', en='Koelreuteria paniculata', row='Koelreuteria paniculata', poze=['p05'], incert=True,
      nota="Arborii din planul îndepărtat al pozei 5, cu ciorchini de capsule gălbui-brune, ca niște lampioane de hârtie, atârnate în coroană. De la distanță, portul rotunjit și fructele sunt ale clocotișului.",
      h2='2,0–2,5 m', h5='4,0–5,0 m', hm='8–12 m, coroană 8 m', apa=dict(l=10, f=1),
      luni=luni((R, 4), (V, 2), (I, 1), (F, 3), (R, 2)), verdict='retine',
      crucea="Arbore mic, de secetă, cu flori galbene în iulie când nu mai înflorește nimic și lampioane până în octombrie. Nu e în niciunul dintre planuri și ar merita: lângă terasă sau în locul unui tei la parcare, cu o treime din apa acestuia."),
]

PROBLEME = [
 dict(titlu='Ploșnița platanului', unde='pozele 6 și 12', poza='p06',
      text="Pete decolorate mărunte pe toată fața frunzei, margini arse, frunze brune în coroană din septembrie. Corythucha ciliata e pe toți platanii din oraș și nu se tratează practic la un arbore matur. Lecția: nu alegi o specie care în Dobrogea vine cu dăunătorul la pachet."),
 dict(titlu='Pin negru sufocat de foioase', unde='poza 3', poza='p03',
      text="Coroană rară, 5–6 m de trunchi gol la bază, iederă pe trunchi. Pinul a fost plantat deodată cu foioasele, care l-au depășit și l-au umbrit. În pădurea Miyawaki pinii se pun pe margine, pe latura de sud și vest, niciodată în interior."),
 dict(titlu='Terasament peste rădăcini', unde='poza 4', poza='p04',
      text="Pământ cu pietre și moloz aruncat peste zona rădăcinilor chiparosului și nucului, cu coletul îngropat. Rădăcinile rămân fără aer și scoarța de la bază putrezește: coniferul se usucă în 2–3 ani. La tine: pământul din șanțuri și grămezile de materiale nu se depozitează niciodată sub coroana unui arbore."),
 dict(titlu='Jardinieră cu sol gol', unde='poza 5', poza='p05',
      text="Jumătate din jardinieră e pământ bătătorit, cu pir și iarbă uscată. Ienupărul e plantat prea rar și nu s-a mulcit între tufe. Orice suprafață de sol lăsată goală se umple de buruieni — se mulcește de la plantare, până se închid plantele."),
 dict(titlu='Bifurcație în V cu scoarță inclusă', unde='poza 14', poza='p14',
      text="Corcodușul se desparte de la 1 m în două brațe egale, cu scoarță prinsă între ele: la furtună se despică exact acolo. Tăietura recentă e corect făcută, dar în octombrie; tăierile de formare se fac la sfârșit de iarnă, când rana se închide în primul sezon."),
 dict(titlu='Plop piramidal la 3 m de clădire', unde='poza 1', poza='p01',
      text="Plopii stau la 3–4 m de calcanul blocului, cu rădăcini superficiale care caută apa de sub fundație și ramuri casante peste acoperiș. Frunzișul deja galben și rărit în octombrie arată stresul hidric. La Crucea, plopul rămâne la peste 15 m de orice construcție."),
]
