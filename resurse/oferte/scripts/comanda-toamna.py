# -*- coding: utf-8 -*-
"""Excel de urmărire a comenzilor de toamnă (pădurea Miyawaki, schema 4 + planul nord), după livrarea lui Ionuț din
11 noiembrie 2026. Fără arbuștii ornamentali și gardurile vii de primăvară.
    python3 resurse/oferte/scripts/comanda-toamna.py  → resurse/oferte/comanda-toamna-2026.xlsx
"""
import json, math
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.comments import Comment
S = json.load(open('/home/user/crucea/miyawaki/plantare-miyawaki-est4.json', encoding='utf-8'))
buc = {s['cod']: s['buc'] for s in S['specii']}; ro = {s['cod']: s['ro'] for s in S['specii']}; lat = {s['cod']: s['lat'] for s in S['specii']}
rez = lambda n: n + max(1, math.ceil(n * 0.1))
# necesarul planului nord (toamnă), fără cele 34 de plante ale perdelei preluate de pădure
NORD = {'A21': 36, 'A24': 12, 'A52': 21, 'A34': 17, 'A48': 1, 'F28': 6, 'S5': 5, 'A5': 2, 'F11': 1, 'F9': 16, 'A40': 1, 'F1': 12, 'F21': 14, 'F6': 2, 'F26': 5, 'F44': 2, 'S4': 1}
NORD_RO = {'A21': 'Sălcioară', 'A24': 'Frasin comun', 'A52': 'Ulm de Turkestan', 'A34': 'Pin negru', 'A48': 'Tei argintiu', 'F28': 'Măceș', 'S5': 'Păducel', 'A5': 'Paltin de câmp', 'F11': 'Corcoduș', 'F9': 'Dud alb', 'A40': 'Stejar pufos', 'F1': 'Alun', 'F21': 'Corn', 'F6': 'Nuc', 'F26': 'Cătină albă', 'F44': 'Sânger', 'S4': 'Scumpie'}
# corespondența cod pădure → cod plan nord (aceeași specie)
LEG = {'Qp': 'A40', 'Tt': 'A48', 'Cr': 'S5', 'Rc': 'F28', 'Pc': 'F11', 'Cm': 'F21', 'Ca': 'F1', 'Cs': 'F44', 'Cc': 'S4', 'Pn': 'A34', 'Um': None}
# primit de la Ionuț, 11 noiembrie
PRIMIT = {'Ulm de Turkestan': 400, 'Pin negru': 55, 'Sălcioară': 40, 'Frasin comun': 15, 'Mojdrean': 50, 'Tei argintiu': 26, 'Măceș': 70, 'Păducel': 60, 'Lemn câinesc': 70}
CO_CARPEN = math.ceil(buc['Co'] / 2); CO_SAMB = buc['Co'] - CO_CARPEN; RH_CALIN = round(buc['Rh'] * 0.6); RH_MACES = buc['Rh'] - RH_CALIN
# (specie, nume latin, necesar pădure, necesar curte, furnizor, observație)
rows = [
 ('Stejar pufos', 'Quercus pubescens', buc['Qp'], NORD['A40'], 'Matto Medusa Galați', 'arborele-cheie; 1 leu'),
 ('Stejar brumăriu', 'Quercus pedunculiflora', buc['Qb'], 0, 'Agigea', '1 leu; are și Agigea (telefon 21 oct) și DS Tulcea/Galați (lista Romsilva, 1,5–2,5 lei)'),
 ('Cer', 'Quercus cerris', buc['Qc'], 0, 'Agigea', 'lista Romsilva toamna 2026: DS Constanța are cer, 1,5–2,0 lei; alternativ Foresta 1 leu'),
 ('Ulm de câmp', 'Ulmus minor', buc['Um'], 0, 'Agigea', 'au în stoc (12 noiembrie); preț de întrebat; alternativ Matto Medusa 1 leu'),
 ('Sorb', 'Sorbus torminalis', buc['St'], 0, 'de găsit (2biz.ro 15 lei)', 'dacă nu există, se înlocuiește cu cer'),
 ('Jugastru', 'Acer campestre', buc['Ac'], 0, 'Agigea', 'comandă fermă 13 nov (25 buc.)'),
 ('Arțar tătăresc', 'Acer tataricum', buc['At'], 0, 'Salcea Suceava', 'curier; preț de întrebat'),
 ('Cărpiniță → carpen comun', 'Carpinus betulus', CO_CARPEN, 0, 'Țuțora Iași', 'înlocuitor, 1,50 lei'),
 ('Cărpiniță → sâmbovină', 'Celtis australis', CO_SAMB, 0, 'de găsit (Cobadin 50 lei, scump)', 'altfel tot carpen'),
 ('Păr sălbatic', 'Pyrus pyraster', buc['Pp'], 0, 'de găsit (OLMA Iași 2,5 lei)', 'de întrebat și la Doi Cocoși'),
 ('Vișin turcesc', 'Prunus mahaleb', buc['Pm'], 0, 'Agigea', 'comandă fermă 13 nov (35 buc.)'),
 ('Cireș sălbatic', 'Prunus avium', buc['Pa'], 0, 'Doi Cocoși Brăila', 'preț de confirmat'),
 ('Măr pădureț', 'Malus sylvestris', buc['Ms'], 0, 'Doi Cocoși Brăila', 'preț de confirmat'),
 ('Corn', 'Cornus mas', buc['Cm'], NORD['F21'], 'de găsit (Tomești 1,40 lei; ICAS; Mizil 18,90)', ''),
 ('Alun', 'Corylus avellana', buc['Ca'], NORD['F1'], 'de găsit (Stejarul Galați; Ionuț 10 lei, 2 ani, confirmat 13 nov; Mizil 13,51)', ''),
 ('Sânger', 'Cornus sanguinea', buc['Cs'], NORD['F44'], 'Selficom Galați', '1,20 lei'),
 ('Scumpie', 'Cotinus coggygria', buc['Cc'], NORD['S4'], 'Agigea', 'în stoc; preț de întrebat'),
 ('Corcoduș', 'Prunus cerasifera', buc['Pc'], NORD['F11'], 'Agigea', 'comandă fermă 13 nov (25 buc.)'),
 ('Porumbar', 'Prunus spinosa', buc['Ps'], 0, 'Agigea', '0,50 lei + TVA'),
 ('Dârmox', 'Viburnum lantana', buc['Vl'], 0, 'de găsit (ICAS; GardenExpert 21,80)', 'de întrebat la Foresta și Doi Cocoși'),
 ('Verigar → călin', 'Viburnum opulus', RH_CALIN, 0, 'de găsit (planteieftine.ro 7,77; Mizil 18,02)', 'înlocuitor'),
 ('Verigar → măceș', 'Rosa canina', RH_MACES, 0, 'Ionuț Suceava (primit)', 'acoperit din cei 70 de măceși primiți (48 necesari la rândul „Măceș” + 20 aici = 68)'),
 ('Salbă râioasă → salbă moale', 'Euonymus europaeus', buc['Ev'], 0, 'de găsit (gardviuhibrid.ro 12,90; Mizil 9,91)', 'înlocuitor'),
 ('Iasomie sălbatică → cătină roșie', 'Tamarix ramosissima', buc['Jf'], 0, 'Cobadin', '15 lei; sau planteieftine.ro'),
 ('Soc', 'Sambucus nigra', buc['Sn'], 0, 'de găsit (planteieftine.ro 5 lei; Ionuț 10 lei, 2 ani, confirmat 13 nov)', ''),
 ('Bășicoasă → arbore de mazăre', 'Caragana arborescens', buc['Cl'], 0, 'de găsit (Pepiniera Roșie 35 lei)', 'altfel păducel din surplus'),
 ('Mojdrean', 'Fraxinus ornus', buc['Fo'], 0, 'Ionuț Suceava (primit)', ''),
 ('Tei argintiu', 'Tilia tomentosa', buc['Tt'], NORD['A48'], 'Ionuț Suceava (primit)', ''),
 ('Păducel', 'Crataegus monogyna', buc['Cr'], NORD['S5'], 'Ionuț Suceava (primit)', ''),
 ('Măceș', 'Rosa canina', buc['Rc'], NORD['F28'], 'Ionuț Suceava (primit)', 'plus cei de mai sus, în locul verigarului'),
 ('Lemn câinesc', 'Ligustrum vulgare', buc['Lv'], 0, 'Ionuț Suceava (primit)', ''),
 ('Pin negru', 'Pinus nigra', buc['Pn'], NORD['A34'], 'Ionuț Suceava (primit)', 'plantat 11 noiembrie'),
 ('Ulm de Turkestan', 'Ulmus pumila', 0, NORD['A52'], 'Ionuț Suceava (primit)', 'plantat 11 noiembrie; 400 cu gardul viu'),
 ('Sălcioară', 'Elaeagnus angustifolia', 0, NORD['A21'], 'Ionuț Suceava (primit)', 'plantat 11 noiembrie'),
 ('Frasin comun', 'Fraxinus excelsior', 0, NORD['A24'], 'Ionuț Suceava (primit)', 'plantat 11 noiembrie'),
 ('Paltin de câmp', 'Acer platanoides', 0, NORD['A5'], 'Foresta Brăila', '1 leu'),
 ('Dud alb', 'Morus alba', 0, NORD['F9'], 'Foresta Brăila', '1 leu; să fie Morus alba'),
 ('Nuc', 'Juglans regia', 0, NORD['F6'], 'pepinieră pomicolă / Mizil', 'puiet din sămânță'),
 ('Cătină albă', 'Hippophae rhamnoides', 0, NORD['F26'], 'pepinieră pomicolă (SCDP Constanța / Nalbant)', '4 femele + 1 mascul'),
]
FURN = [
 ('Ionuț, Suceava', 'WhatsApp (numărul la George)', 'Suceava', 'Suceava; livrare prin curier', 'livrat 11 noiembrie 2026: 786 puieți, 3 395 lei; 13 nov: mai are soc și alun de 2 ani la 10 lei, altceva nu'),
 ('Pepiniera Foresta SRL', '0766413310', 'Brăila', 'Brăila', 'puieți forestieri 1–2 ani, 1 leu; confirmat telefonic 6 octombrie; livrare după căderea frunzei'),
 ('Pepiniera Doi Cocoși SRL', '0766405638', 'Brăila', 'str. Doi Cocoși nr. 2, Brăila', 'confirmat telefonic 6 octombrie; prețuri de confirmat; același drum cu Foresta'),
 ('Pepiniera Matto Medusa SRL', '0767477472', 'Galați', 'Galați', 'confirmat telefonic 6 octombrie; 1 leu'),
 ('Pepiniera Selficom', '0765402805', 'Galați', 'Galați', 'sânger 1,20 lei; același drum cu Matto Medusa'),
 ('Pepiniera Stejarul', '0774609287', 'Galați', 'Galați', 'alun, de sunat'),
 ('Pepiniera Silvică Agigea (Romsilva)', '0241738043 / 0748143025 (ing. Orac)', 'Constanța', 'DN 38, Agigea, Constanța; pepiniera@constanta.rosilva.ro', 'stoc confirmat 21 octombrie; COMANDĂ FERMĂ 13 noiembrie: porumbar 65, scumpie 45, ulm de câmp 20, cer 20, stejar brumăriu 30, vișin turcesc 35, corcoduș 25, jugastru 25 (265); ridicare personală, preț de confirmat'),
 ('Direcția Silvică Tulcea (Romsilva)', 'de căutat', 'Tulcea', 'pepinierele DS Tulcea', 'lista Romsilva toamna 2026: stejar brumăriu 1,5–2,5, corcoduș 1,2–2,2, sălcioară; rezervă'),
 ('Pepiniera Silvică Salcea (Romsilva)', '0753156196 / 0751164370', 'Suceava', 'Salcea, Suceava; curier', 'arțar tătăresc, confirmat 21 octombrie'),
 ('Pepiniera Țuțora', '0722930780', 'Iași', 'Țuțora, Iași', 'carpen 1,50 lei (ofertă 2024)'),
 ('Pepiniera Cobadin', '0746037827', 'Constanța', 'DN3, la intrarea în Cobadin, Constanța; contact@pepinieracobadin.ro', 'cătină roșie 15 lei; 50 km'),
 ('Szabó Zsolt', '0746118273', 'Harghita', 'Tomești, Harghita; curier', 'corn 1,40 lei (anunț vechi), sânger'),
 ('ICAS, Pepiniera Ștefănești', '021 350 3240', 'Argeș', 'Ștefănești, Argeș; icas.ro', 'dârmox, corn'),
 ('SC OLMA', '0767806245', 'Iași', 'Iași', 'păr sălbatic 2,50 lei, măr pădureț 1,50'),
 ('Pepiniera Mizil (magazin online)', 'site', 'Prahova', 'Mizil, Prahova; livrare prin curier', 'ultimă variantă: corn 18,90, alun 13,51, salbă moale 9,91, călin 18,02'),
 ('SCDP Constanța / Pepiniera Pomicolă Nalbant', 'de căutat', 'Constanța / Tulcea', 'Valu lui Traian, Constanța / Nalbant, Tulcea', 'pomi altoiți, cătină albă, nuc'),
]
wb = Workbook(); ws = wb.active; ws.title = 'Comanda toamnă 2026'
F = 'Arial'; H = Font(name=F, bold=True, color='FFFFFF'); N = Font(name=F, size=10); B = Font(name=F, size=10, bold=True)
fill_h = PatternFill('solid', fgColor='1F4D33'); fill_in = PatternFill('solid', fgColor='FFF2CC'); fill_ok = PatternFill('solid', fgColor='E2EFDA')
thin = Side(style='thin', color='BFBFBF'); box = Border(left=thin, right=thin, top=thin, bottom=thin)
ws['A1'] = 'Comanda de puieți pentru toamna 2026 — pădurea Miyawaki (schema 4) și planul nord'; ws['A1'].font = Font(name=F, size=13, bold=True)
ws['A2'] = 'Necesarul include rezerva de 10 % (minimum 1). Fără arbuștii ornamentali și gardurile vii de laur/photinia, care se plantează primăvara. Coloanele galbene se completează pe măsură ce comanzi și primești.'; ws['A2'].font = Font(name=F, size=9, italic=True)
hdr = ['Specie', 'Nume latin', 'Necesar pădure', 'Necesar curte', 'Necesar total (+10 %)', 'Furnizor', 'Județ', 'Cantitate comandată', 'Cantitate recepționată', 'Rămâne de primit', 'Observații']
JUD = {'Ionuț': 'Suceava', 'Foresta': 'Brăila', 'Doi Cocoși': 'Brăila', 'Matto Medusa': 'Galați', 'Selficom': 'Galați', 'Stejarul': 'Galați', 'Agigea': 'Constanța', 'Salcea': 'Suceava', 'Țuțora': 'Iași', 'Cobadin': 'Constanța', 'Tomești': 'Harghita', 'OLMA': 'Iași', 'Mizil': 'Prahova', 'SCDP': 'Constanța / Tulcea', 'pomicolă': 'Constanța / Tulcea', 'ICAS': 'Argeș', '2biz': 'online', 'planteieftine': 'online', 'gardviuhibrid': 'online', 'Roșie': 'Teleorman', 'GardenExpert': 'online'}
def judet(fu): return next((j for k, j in JUD.items() if k in fu), '')
r0 = 4
for c, h in enumerate(hdr, 1):
    cell = ws.cell(r0, c, h); cell.font = H; cell.fill = fill_h; cell.alignment = Alignment(wrap_text=True, vertical='center'); cell.border = box
r = r0 + 1
for sp, la, np_, nc, fu, obs in rows:
    tot = rez(np_ + nc)
    primit = PRIMIT.get(sp.split(' → ')[-1] if '→' in sp else sp, 0) if 'primit' in fu else 0
    COMANDAT = {'Porumbar': 65, 'Scumpie': 45, 'Ulm de câmp': 20, 'Cer': 20, 'Stejar brumăriu': 30, 'Vișin turcesc': 35, 'Corcoduș': 25, 'Jugastru': 25}   # Agigea, comandă fermă 13 nov
    comandat = COMANDAT.get(sp, 0) if fu == 'Agigea' else 0
    vals = [sp, la, np_, nc, f'=ROUNDUP((C{r}+D{r})*1.1,0)', fu, judet(fu), (primit or comandat) or None, primit if primit else None, f'=H{r}-I{r}', obs]
    for c, v in enumerate(vals, 1):
        cell = ws.cell(r, c, v); cell.font = N; cell.border = box
        if c in (8, 9): cell.fill = fill_in
        if c == 2: cell.font = Font(name=F, size=10, italic=True)
    if 'primit' in fu:
        for c in range(1, 12): ws.cell(r, c).fill = fill_ok
    r += 1
last = r - 1
ws.cell(r, 1, 'Total').font = B
for col in 'CDEHIJ': ws[f'{col}{r}'] = f'=SUM({col}{r0 + 1}:{col}{last})'; ws[f'{col}{r}'].font = B; ws[f'{col}{r}'].border = box
ws.cell(r0 + 1 + len(rows) + 1, 1, 'Legendă: verde = primit de la Ionuț pe 11 noiembrie (cantitatea e trecută deja); galben = de completat la comandă și la recepție; „Rămâne de primit” = comandat − recepționat.').font = Font(name=F, size=9, italic=True)
ws['E4'].comment = Comment('Necesar pădure + curte, +10 % rezervă, rotunjit în sus. Sursa: plantare-miyawaki-est4.json și pozitie-nord-miyawaki.json.', 'Poienel')
# furnizorii
rf = r + 4
ws.cell(rf, 1, 'Furnizori — date de contact').font = Font(name=F, size=12, bold=True)
for c, h in enumerate(['Furnizor', 'Telefon', 'Județ', 'Adresă', 'Observații'], 1):
    cell = ws.cell(rf + 1, c, h); cell.font = H; cell.fill = fill_h; cell.border = box
for i, (n, t, j, a, o) in enumerate(FURN):
    for c, v in enumerate((n, t, j, a, o), 1):
        cell = ws.cell(rf + 2 + i, c, v); cell.font = N; cell.border = box; cell.alignment = Alignment(wrap_text=True, vertical='top')
for col, w in zip('ABCDEFGHIJK', (30, 26, 10, 10, 12, 42, 14, 12, 13, 12, 44)): ws.column_dimensions[col].width = w
ws.row_dimensions[r0].height = 32; ws.freeze_panes = 'A5'
ws.page_setup.orientation = 'landscape'; ws.page_setup.fitToWidth = 1; ws.sheet_properties.pageSetUpPr.fitToPage = True
out = '/home/user/crucea/resurse/oferte/comanda-toamna-2026.xlsx'; wb.save(out); print('scris', out, len(rows), 'specii')
