# Sistem de Irigare cu Picurare - Livadă

## 1. Descriere Generală

Sistem de irigare cu picurare pentru livadă, alimentat dintr-un puț forat, cu stocare intermediară în 4 bidoane IBC de 1000L (total 4000L). Putul alimentează bidoanele pe parcursul zilei, iar udarea se realizează a doua zi dimineața, pe secvențe, prin 6 trasee cu lungimi între 100m și 200m.

---

## 2. Schema Funcțională

```
                         ┌─────────────┐
                         │  PUȚ FORAT  │
                         └──────┬──────┘
                                │
                         ┌──────┴──────┐
                         │ POMPĂ PUȚĂ  │
                         │ submersibilă│
                         └──────┬──────┘
                                │
                    ┌───────────┴───────────┐
                    │   CONDUCTĂ UMPLERE    │
                    │   PE 32mm / PE 40mm   │
                    └───────────┬───────────┘
                                │
              ┌────────┬────────┼────────┬────────┐
              │        │        │        │        │
          ┌───┴───┐┌───┴───┐┌──┴────┐┌──┴────┐   │
          │ BIDON ││ BIDON ││ BIDON ││ BIDON │   │
          │ 1000L ││ 1000L ││ 1000L ││ 1000L │   │
          │  #1   ││  #2   ││  #3   ││  #4   │   │
          └───┬───┘└───┬───┘└───┬───┘└───┬───┘   │
              │        │        │        │        │
              └────────┴────────┼────────┘        │
                                │                 │
                    ┌───────────┴───────────┐     │
                    │  FILTRU DISC 120 mesh │     │
                    └───────────┬───────────┘     │
                                │                 │
                    ┌───────────┴───────────┐     │
                    │   POMPĂ IRIGARE       │     │
                    │   de suprafață        │     │
                    └───────────┬───────────┘     │
                                │                 │
                    ┌───────────┴───────────┐     │
                    │ COLECTOR DISTRIBUȚIE   │     │
                    │ cu 6 electroventile   │     │
                    └───┬──┬──┬──┬──┬──┬────┘     │
                        │  │  │  │  │  │          │
                       T1 T2 T3 T4 T5 T6         │
                                                  │
              T1 = Traseu 1 (200m)                │
              T2 = Traseu 2 (180m)          SUPAPĂ PLUTITOR
              T3 = Traseu 3 (150m)          (oprire automată
              T4 = Traseu 4 (150m)           la umplere)
              T5 = Traseu 5 (120m)
              T6 = Traseu 6 (100m)
```

---

## 3. Sistem de Pompe

### 3.1 Pompă Submersibilă Puț (Alimentare Bidoane)

| Parametru | Specificație |
|-----------|-------------|
| **Tip** | Pompă submersibilă 4" |
| **Debit recomandat** | 2-3 m³/h |
| **Înălțime refulare** | Depinde de adâncimea puțului + înălțimea bidoanelor (ex: 30-50m) |
| **Putere** | 0.75 - 1.5 kW (în funcție de adâncime) |
| **Alimentare** | 230V monofazat |
| **Exemplu model** | Pedrollo 4SR2/13, Grundfos SQ 2-55, sau echivalent |
| **Protecție** | Cu protecție la funcționare în gol (lipsa apei) |

**Notă:** Dimensionarea exactă depinde de adâncimea puțului și nivelul static/dinamic al apei. Se recomandă consultarea foii tehnice a puțului.

### 3.2 Pompă de Suprafață (Irigare din Bidoane)

| Parametru | Specificație |
|-----------|-------------|
| **Tip** | Pompă centrifugă de suprafață |
| **Debit recomandat** | 3-4 m³/h |
| **Presiune** | 2-3 bar (suficient pentru picurare) |
| **Putere** | 0.75 - 1.1 kW |
| **Alimentare** | 230V monofazat |
| **Exemplu model** | Pedrollo CPm 158, DAB Jet 102M, sau echivalent |
| **Caracteristici** | Auto-amorsare, corp fontă sau inox |

**Calcul orientativ debit necesar:**
- Picurător standard: 2-4 L/h per picurător
- Distanță între picurători: 0.3-0.5m
- Traseu 200m cu picurători la 0.3m = ~666 picurători × 2L/h = ~1330 L/h per traseu
- Se irigă pe secvențe (un traseu pe rând), deci pompa trebuie să asigure debitul pentru cel mai lung traseu

---

## 4. Sistem de Senzori

### 4.1 Senzori Nivel Apă - Bidoane

| Senzor | Funcție | Tip Recomandat |
|--------|---------|----------------|
| **Senzor nivel maxim** | Oprește pompa puț la umplere | Plutitor electric (float switch) NC |
| **Senzor nivel minim** | Oprește pompa irigare la golire | Plutitor electric (float switch) NO |
| **Senzor nivel intermediar** (opțional) | Pornire reumplere | Plutitor electric (float switch) |

**Recomandare:** 2 senzori plutitor per bidon (nivel maxim + nivel minim) = **8 senzori plutitor** în total.

Alternativă avansată: senzor ultrasonic de nivel pentru monitorizare continuă (ex: HC-SR04 cu ESP32).

### 4.2 Senzor Presiune

| Senzor | Funcție | Amplasare |
|--------|---------|-----------|
| **Traductor presiune 0-6 bar** | Monitorizare presiune irigare | După pompa de suprafață |
| **Presostat** | Protecție pompă | Pe conducta de refulare |

### 4.3 Senzor Debit (Opțional)

| Senzor | Funcție | Amplasare |
|--------|---------|-----------|
| **Debitmetru cu pulsuri** | Monitorizare consum apă | Pe conducta principală, după pompă |
| **Exemplu** | YF-S201 (1-30 L/min) sau echivalent industrial | |

### 4.4 Senzori Umiditate Sol (Opțional)

| Senzor | Funcție | Amplasare |
|--------|---------|-----------|
| **Senzor umiditate sol capacitiv** | Determinare necesitate irigare | 1-2 per traseu, la adâncime 20-30cm |
| **Exemplu** | Senzor capacitiv v1.2 sau Watermark 200SS | |

### 4.5 Senzor Funcționare Puț

| Senzor | Funcție | Amplasare |
|--------|---------|-----------|
| **Senzor nivel puț** | Protecție funcționare în gol | În puțul forat |
| **Sondă electrode** | Detectare nivel minim apă | Sub pompa submersibilă |

---

## 5. Sistem de Automatizare

### 5.1 Varianta 1 - Controller Dedicat Irigații (Recomandat pentru simplitate)

| Echipament | Specificație |
|------------|-------------|
| **Controller irigații** | Hunter Pro-HC, Rain Bird ESP-TM2, sau Galcon AC-24 |
| **Nr. zone** | Minim 6 zone (pentru cele 6 trasee) + 1 zonă master |
| **Electroventile** | 6 × electroventil 1" sau 3/4" (24V AC sau 9V DC latch) |
| **Funcții** | Programare ore start, durată per zonă, zile |

### 5.2 Varianta 2 - Automatizare cu PLC / Microcontroller (Recomandat pentru control complet)

| Echipament | Specificație |
|------------|-------------|
| **Controller** | ESP32 / Arduino Mega + module releu |
| **Module releu** | 1 × modul 8 relee (230V/10A) |
| **Alimentare** | Sursă 24V DC pentru electroventile + 5V pentru controller |
| **Comunicare** | WiFi (ESP32) pentru monitorizare la distanță |
| **Interfață** | Aplicație mobilă (Blynk, Home Assistant, sau custom) |

### 5.3 Logica de Automatizare

```
PROGRAM ZILNIC:

═══ FAZA 1: UMPLERE BIDOANE (ziua) ═══

  06:00 - Verifică nivel bidoane
       │
       ├─ Nivel < MAXIM → Pornește pompă puț
       │                    Monitorizare continuă nivel
       │                    La nivel MAXIM → Oprește pompă puț
       │
       └─ Nivel = MAXIM → Pompă puț OPRITĂ (standby)

  Protecții umplere:
  • Timeout umplere: max 8h funcționare continuă
  • Senzor nivel puț: oprire la nivel minim
  • Supapă plutitor pe bidoane: protecție mecanică backup

═══ FAZA 2: IRIGARE SECVENȚIALĂ (dimineața devreme) ═══

  05:00 - Start ciclu irigare
       │
       ├─ Verifică nivel bidoane ≥ MINIM
       │
       ├─ Pornește pompă irigare
       │
       ├─ Secvența 1: Deschide electroventil T1 (200m)
       │               Durata: 45-60 min
       │               Închide T1
       │
       ├─ Secvența 2: Deschide electroventil T2 (180m)
       │               Durata: 40-55 min
       │               Închide T2
       │
       ├─ Secvența 3: Deschide electroventil T3 (150m)
       │               Durata: 35-45 min
       │               Închide T3
       │
       ├─ Secvența 4: Deschide electroventil T4 (150m)
       │               Durata: 35-45 min
       │               Închide T4
       │
       ├─ Secvența 5: Deschide electroventil T5 (120m)
       │               Durata: 30-40 min
       │               Închide T5
       │
       ├─ Secvența 6: Deschide electroventil T6 (100m)
       │               Durata: 25-35 min
       │               Închide T6
       │
       └─ Oprește pompă irigare
           Raport: volum total consumat, durate efective

  Protecții irigare:
  • Senzor nivel minim bidoane: oprire la golire
  • Presostat: oprire la pierdere presiune (conductă spartă)
  • Timeout per zonă: oprire la depășire durată maximă
```

---

## 6. Lista de Probleme Potențiale și Soluții

### 6.1 Probleme Hidraulice

| Nr. | Problemă | Cauză | Soluție | Prevenție |
|-----|----------|-------|---------|-----------|
| 1 | **Înfundare picurători** | Nisip, alge, calcar din apă de puț | Curățare cu acid citric, înlocuire | Filtru disc 120 mesh + filtru plasă la intrare bidon |
| 2 | **Presiune insuficientă la capăt de traseu** | Traseu prea lung, pierderi de sarcină | Verificare dimensionare conductă, reducere nr. picurători | Calcul hidraulic corect, PE 25mm pe traseele lungi |
| 3 | **Presiune neuniformă între trasee** | Lungimi diferite = pierderi diferite | Regulatoare de presiune per traseu | Montare regulatoare presiune 1.5-2 bar |
| 4 | **Spargeri conducte** | Îngheț, degradare UV, animal | Reparare cu fitinguri | Îngropare 30-40cm, protecție UV |
| 5 | **Pierderi apă la îmbinări** | Montaj defectuos, degradare | Strângere, înlocuire garnituri | Utilizare fitinguri de calitate, bandă teflon |
| 6 | **Cavitație pompă suprafață** | Aspirație prea lungă, conducta aspirație subdimensionată | Verificare NPSH, scurtare aspirație | Conducta aspirație min. 40mm, lungime max 3m |
| 7 | **Golire bidoane prea rapidă** | Scurgere, suprapunere zone | Verificare electroventile, verificare program | Senzori nivel + monitorizare debit |

### 6.2 Probleme Electrice și de Automatizare

| Nr. | Problemă | Cauză | Soluție | Prevenție |
|-----|----------|-------|---------|-----------|
| 8 | **Pompă puț nu pornește** | Protecție termică, lipsă apă, defect electric | Verificare tablou, reset protecție | Protecție suprasarcină, variator frecvență |
| 9 | **Electroventil blocat deschis** | Impurități pe membrană, defect solenoid | Demontare, curățare, înlocuire | Filtru înainte de electroventile |
| 10 | **Electroventil blocat închis** | Defect solenoid, lipsă tensiune | Verificare alimentare, înlocuire solenoid | Verificare periodică funcționare |
| 11 | **Senzor plutitor blocat** | Depuneri calcar, alge | Curățare, înlocuire | Curățare periodică bidoane |
| 12 | **Pană de curent** | Rețea electrică instabilă | UPS pentru controller, repornire automată | UPS minim pentru controller |
| 13 | **Controller defect** | Umiditate, furtună | Înlocuire, protecție la supratensiune | Carcasă IP65, descărcător supratensiune |
| 14 | **Comunicare WiFi pierdută** | Distanță, interferențe | Repetor WiFi, antenă externă | Funcționare autonomă offline |

### 6.3 Probleme de Exploatare

| Nr. | Problemă | Cauză | Soluție | Prevenție |
|-----|----------|-------|---------|-----------|
| 15 | **Dezvoltare alge în bidoane** | Lumină + apă stătută | Tratare cu hipoclorit de sodiu, vopsire bidoane negru | Bidoane opace, tratament periodic |
| 16 | **Depuneri calcar** | Apă dură din puț | Tratare cu acid, dedurizare | Analiză chimică apă, tratament preventiv |
| 17 | **Irigare insuficientă** | Debit mic, timp scurt, înfundări | Ajustare program, curățare sistem | Monitorizare umiditate sol, inspecție vizuală |
| 18 | **Irigare excesivă** | Program greșit, electroventil blocat deschis | Corectare program, reparare ventil | Senzori umiditate sol, limită volum |
| 19 | **Scădere debit puț** | Colmatare, scădere nivel freatic | Regenerare puț, pompare testare | Monitorizare debit periodic |
| 20 | **Deteriorare în sezonul rece** | Îngheț apă în conducte și bidoane | Golire completă sistem | Procedură de iernare (golire, suflare cu aer) |
| 21 | **Rozătoare rod conducte** | Șoareci, șobolani | Înlocuire secțiuni, protecție | Îngropare conducte, plasă protecție |
| 22 | **Furt echipamente** | Amplasare izolată | Înlocuire | Împrejmuire, cameră supraveghere |

---

## 7. Necesar de Materiale și Echipamente

### 7.1 Stocare Apă

| Nr. | Material | Cantitate | Specificație | Preț Estimativ (RON) |
|-----|----------|-----------|-------------|----------------------|
| 1 | Bidon IBC 1000L | 4 buc | Recondiționat sau nou, cu suport metalic | 4 × 400-800 |
| 2 | Supapă plutitor 1" | 4 buc | Oprire automată umplere | 4 × 50-80 |
| 3 | Racord bidon IBC 2" la 1" | 4 buc | Adaptor S60x6 la filet 1" | 4 × 30-50 |
| 4 | Racord interconectare bidoane | 3 buc | Teu + racorduri PE 40mm | 3 × 40-60 |
| 5 | Suport / platformă bidoane | 1 set | Beton sau cadru metalic, înălțat 30-50cm | 500-1000 |

### 7.2 Pompe și Accesorii

| Nr. | Material | Cantitate | Specificație | Preț Estimativ (RON) |
|-----|----------|-----------|-------------|----------------------|
| 6 | Pompă submersibilă puț 4" | 1 buc | 0.75-1.5 kW, 2-3 m³/h | 1500-3000 |
| 7 | Cablu pompă submersibilă | 1 buc | 3×1.5mm², lungime = adâncime puț + 10m | 5-10 RON/m |
| 8 | Coardă de siguranță inox | 1 buc | Ø4mm, lungime = adâncime puț | 3-5 RON/m |
| 9 | Pompă suprafață irigare | 1 buc | 0.75-1.1 kW, auto-amorsare, 3-4 m³/h | 800-1500 |
| 10 | Vas expansiune 24L | 1 buc | Pentru pompă suprafață | 150-250 |
| 11 | Presostat | 1 buc | 1-3 bar, reglabil | 50-100 |

### 7.3 Filtrare

| Nr. | Material | Cantitate | Specificație | Preț Estimativ (RON) |
|-----|----------|-----------|-------------|----------------------|
| 12 | Filtru disc 3/4" sau 1" | 1 buc | 120 mesh (130 microni) | 80-200 |
| 13 | Filtru plasă intrare bidoane | 4 buc | Plasă inox, montaj pe gura de umplere | 4 × 20-40 |

### 7.4 Conducte și Fitinguri - Alimentare Bidoane

| Nr. | Material | Cantitate | Specificație | Preț Estimativ (RON) |
|-----|----------|-----------|-------------|----------------------|
| 14 | Conductă PE 32mm sau 40mm | ~50-100m | PN10, pentru alimentare de la puț | 3-5 RON/m |
| 15 | Fitinguri PE compresie 32/40mm | 1 set | Coturi, teuri, racorduri, mufe | 200-400 |
| 16 | Robinet sferic 1" | 6 buc | Pentru izolare secțiuni | 6 × 25-50 |

### 7.5 Conducte și Fitinguri - Distribuție Irigare

| Nr. | Material | Cantitate | Specificație | Preț Estimativ (RON) |
|-----|----------|-----------|-------------|----------------------|
| 17 | Conductă PE 32mm | ~20-30m | PN10, colector distribuție | 3-5 RON/m |
| 18 | Conductă PE 25mm | ~50m | PN10, conducte secundare la trasee | 2-4 RON/m |
| 19 | Fitinguri PE compresie 32/25mm | 1 set | Reducții, teuri, coturi | 200-400 |

### 7.6 Trasee Picurare

| Nr. | Material | Cantitate | Specificație | Preț Estimativ (RON) |
|-----|----------|-----------|-------------|----------------------|
| 20 | Bandă sau tub picurare 16mm | ~950m total | Cu picurători integrați la 30-50cm, debit 2-4 L/h | 0.5-1.5 RON/m |
| | - Traseu 1 | 200m | | |
| | - Traseu 2 | 180m | | |
| | - Traseu 3 | 150m | | |
| | - Traseu 4 | 150m | | |
| | - Traseu 5 | 120m | | |
| | - Traseu 6 | 100m | | |
| 21 | Conector tub picurare 16mm | 12 buc | Start connector cu garnitură | 12 × 3-5 |
| 22 | Capăt de linie 16mm | 6 buc | Dop sau inel pliere | 6 × 2-3 |
| 23 | Regulatoare presiune | 6 buc | 1.5 bar sau 2 bar, montaj per traseu | 6 × 30-60 |

### 7.7 Electroventile și Automatizare

| Nr. | Material | Cantitate | Specificație | Preț Estimativ (RON) |
|-----|----------|-----------|-------------|----------------------|
| 24 | Electroventil irigații 1" | 6 buc | 24V AC, tip Hunter PGV sau Rain Bird 100-DV | 6 × 80-150 |
| 25 | Controller irigații | 1 buc | 8 zone, Hunter Pro-HC / Rain Bird ESP-TM2 | 400-800 |
| 26 | Cablu electric pentru electroventile | ~200m | Cablu 7×0.8mm² (multiconductor irigații) | 3-5 RON/m |
| 27 | Cutie conexiuni IP65 | 2 buc | Pentru joncțiuni cablu în teren | 2 × 30-50 |

### 7.8 Senzori

| Nr. | Material | Cantitate | Specificație | Preț Estimativ (RON) |
|-----|----------|-----------|-------------|----------------------|
| 28 | Senzor plutitor nivel | 8 buc | 4× nivel max + 4× nivel min | 8 × 20-40 |
| 29 | Senzor presiune analogic | 1 buc | 0-6 bar, ieșire 4-20mA sau 0-5V | 80-150 |
| 30 | Debitmetru cu pulsuri | 1 buc | DN25, 1-60 L/min | 100-200 |
| 31 | Senzor umiditate sol | 2-4 buc | Capacitiv, rezistent la coroziune | 2-4 × 50-100 |

### 7.9 Tablou Electric și Protecții

| Nr. | Material | Cantitate | Specificație | Preț Estimativ (RON) |
|-----|----------|-----------|-------------|----------------------|
| 32 | Tablou electric exterior | 1 buc | IP65, minim 24 module | 150-300 |
| 33 | Întrerupător diferențial 30mA | 1 buc | 25A, 2P | 100-150 |
| 34 | Disjunctor pompă puț | 1 buc | C10 sau C16, 2P | 30-50 |
| 35 | Disjunctor pompă suprafață | 1 buc | C10 sau C16, 2P | 30-50 |
| 36 | Contactor pompă puț | 1 buc | 230V, 10-16A | 50-80 |
| 37 | Contactor pompă suprafață | 1 buc | 230V, 10-16A | 50-80 |
| 38 | Releu termic pompă puț | 1 buc | Reglabil, potrivit puterii | 60-100 |
| 39 | Descărcător supratensiune | 1 buc | Tip 2, 230V | 100-200 |
| 40 | Cablu electric alimentare | ~50-100m | CYY-F 3×2.5mm² | 5-8 RON/m |
| 41 | Priză + întreruptor extern IP65 | 2 buc | Pentru pompe | 2 × 30-50 |

### 7.10 Diverse

| Nr. | Material | Cantitate | Specificație | Preț Estimativ (RON) |
|-----|----------|-----------|-------------|----------------------|
| 42 | Bandă teflon | 5 buc | 12mm × 12m | 5 × 3-5 |
| 43 | Coliere inox | 20 buc | Diverse dimensiuni | 20 × 3-5 |
| 44 | Manometru 0-6 bar | 1 buc | Montaj pe colector | 30-50 |
| 45 | Supapă unidirecțională (clapetă) | 2 buc | 1", pentru pompe | 2 × 30-50 |
| 46 | Ventil aerisire/dezaerisire | 2-3 buc | Pentru capetele de traseu | 3 × 15-25 |
| 47 | Săpun / lubrifiant montaj PE | 1 buc | Pentru inserare tub în fitinguri | 15-25 |

---

## 8. Estimare Buget Total

| Categorie | Estimare (RON) |
|-----------|---------------|
| Stocare apă (bidoane, accesorii) | 2.500 - 4.500 |
| Pompe și accesorii | 2.800 - 5.200 |
| Filtrare | 200 - 400 |
| Conducte alimentare | 500 - 1.000 |
| Conducte distribuție | 300 - 600 |
| Trasee picurare | 700 - 1.800 |
| Electroventile și automatizare | 1.500 - 2.800 |
| Senzori | 500 - 1.000 |
| Tablou electric și protecții | 800 - 1.500 |
| Diverse | 200 - 400 |
| **TOTAL ESTIMAT** | **10.000 - 19.200** |

**Notă:** Prețurile sunt estimative (2024-2025) și pot varia în funcție de furnizor, brand și disponibilitate. Nu includ manopera de montaj și săpăturile.

---

## 9. Recomandări de Montaj

1. **Bidoanele** se montează pe o platformă de beton nivelată, interconectate la bază cu PE 40mm pentru echilibrare nivel
2. **Pompa de suprafață** se montează cât mai aproape de bidoane, pe o platformă antivibratii, cu aspirație scurtă (max 2-3m) și PE 40mm
3. **Filtrul disc** se montează obligatoriu după pompă, înainte de colectorul de distribuție
4. **Electroventilele** se montează în cămin de vizitare, protejate de intemperii
5. **Tubul de picurare** se montează cu picurătorii în sus pentru a evita înfundarea cu pământ
6. **Cablurile electrice** se introduc în tub PVC copex sau se îngropă în tub PE de protecție
7. **Conductele** se îngropă la minim 30-40cm pentru protecție la îngheț și UV

---

## 10. Program de Întreținere

| Frecvență | Acțiune |
|-----------|---------|
| **Săptămânal** | Verificare vizuală funcționare, verificare presiune, verificare nivel bidoane |
| **Lunar** | Curățare filtru disc, verificare picurători (debit uniform), verificare electroventile |
| **Trimestrial** | Spălare trasee picurare (deschidere capete de linie), verificare senzori |
| **Anual** | Tratament anti-calcar (acid citric/fosforic), curățare bidoane, verificare pompă |
| **La iernare** | Golire completă sistem, suflare cu compresor, protecție pompă suprafață |
| **La pornire primăvară** | Verificare completă sistem, test presiune, verificare etanșeitate |
