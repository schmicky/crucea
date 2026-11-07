# -*- coding: utf-8 -*-
"""Aliniază cantitățile din comenzi-miyawaki-est.md (și rândurile pădurii din comenzi-noiembrie-plan-nord.md) pe o schemă
de plantare a pădurii: rescrie coloanele „În schemă” și „De comandat”, totalurile pe furnizor și secțiunea Totaluri.
Textele (furnizori, observații, stări) rămân cum sunt.

    python3 resurse/oferte/scripts/aliniaza-comenzi.py miyawaki/plantare-miyawaki-est4.json
"""
import json, re, math, sys, collections
S = json.load(open(sys.argv[1], encoding='utf-8'))
buc = {s['cod']: s['buc'] for s in S['specii']}; var = S.get('varianta', '?'); tot = len(S['plante']); arie = S['arie_m2']
rez = lambda n: n + max(1, math.ceil(n * 0.1))
# înlocuitorii din schemă (speciile care nu se găsesc la pepiniere)
CO_CARPEN = math.ceil(buc['Co'] / 2); CO_SAMB = buc['Co'] - CO_CARPEN
RH_CALIN = round(buc['Rh'] * 0.6); RH_MACES = buc['Rh'] - RH_CALIN
N = dict(buc); N['Rc'] = buc['Rc'] + RH_MACES
SPECIAL = {('Co', 'Carpen comun'): CO_CARPEN, ('Co', 'Sâmbovină'): CO_SAMB, ('Rh', 'Călin'): RH_CALIN}

p = 'resurse/oferte/comenzi-miyawaki-est.md'; md = open(p, encoding='utf-8').read()
md = re.sub(r"Necesarul pentru schema `miyawaki/index-est\d*\.html`: \*\*\d+ de puieți din 30 de specii\*\* pe [\d.]+ m²",
            f"Necesarul pentru schema `miyawaki/index-est{var}.html`: **{tot} de puieți din 30 de specii** pe {arie} m²", md, count=1)
# tabelul înlocuitorilor
md = re.sub(r"\| Cărpiniță \(Carpinus orientalis\) \| \d+ \| \d+ carpen comun \(Țuțora Iași\) \+ \d+ sâmbovină", f"| Cărpiniță (Carpinus orientalis) | {buc['Co']} | {CO_CARPEN} carpen comun (Țuțora Iași) + {CO_SAMB} sâmbovină", md)
md = re.sub(r"\| Salbă râioasă \(Euonymus verrucosus\) \| \d+ \| \d+ salbă moale", f"| Salbă râioasă (Euonymus verrucosus) | {buc['Ev']} | {buc['Ev']} salbă moale", md)
md = re.sub(r"\| Verigar \(Rhamnus cathartica\) \| \d+ \| \d+ călin \(Mizil, 18,02 lei\) \+ \d+ măceș", f"| Verigar (Rhamnus cathartica) | {buc['Rh']} | {RH_CALIN} călin (Mizil, 18,02 lei) + {RH_MACES} măceș", md)
md = re.sub(r"\| Iasomie sălbatică \(Jasminum fruticans\) \| \d+ \| \d+ cătină roșie", f"| Iasomie sălbatică (Jasminum fruticans) | {buc['Jf']} | {buc['Jf']} cătină roșie", md)
md = re.sub(r"\| Bășicoasă \(Colutea arborescens\) \| \d+ \| \d+ arbore de mazăre", f"| Bășicoasă (Colutea arborescens) | {buc['Cl']} | {buc['Cl']} arbore de mazăre", md)
# rândurile pe specie și totalurile pe secțiune
out, sec_n, sec_r, cost, cost_by = [], 0, 0, 0.0, collections.OrderedDict()
sec = ''
for line in md.split('\n'):
    if line.startswith('## '): sec = line[3:]
    m = re.match(r"\| ([A-Z][a-z]) \| ([^|]+?) \| (\*[^|]+\*) \| (\d+) \| (\d+) \| ([^|]+) \|(.*)$", line)
    if m:
        cod, nume = m.group(1), m.group(2).strip(); n = N.get(cod, 0)
        for (c, pref), v in SPECIAL.items():
            if cod == c and nume.startswith(pref): n = v
        obs = m.group(7)
        obs = re.sub(r'strat D: \d+ din schemă \+ \d+ în locul verigarului', f'strat D: {buc["Rc"]} din schemă + {RH_MACES} în locul verigarului', obs)
        obs = re.sub(r'înlocuitor pentru \d+ din cele \d+ cărpinițe', f'înlocuitor pentru {n} din cele {buc["Co"]} cărpinițe', obs)
        obs = re.sub(r'înlocuitor pentru \d+ din cei \d+ verigari \(restul \d+ = măceș', f'înlocuitor pentru {RH_CALIN} din cei {buc["Rh"]} verigari (restul {RH_MACES} = măceș', obs)
        obs = re.sub(r'adică \d+ carpeni în total', f'adică {buc["Co"]} carpeni în total', obs)
        obs = re.sub(r'înlocuire cu \d+ păducel', f'înlocuire cu {buc["Cl"]} păducel', obs)
        line = f"| {cod} | {m.group(2)} | {m.group(3)} | {n} | {rez(n)} | {m.group(6)} |{obs}"
        sec_n += n; sec_r += rez(n)
        try: cost_by[sec] = cost_by.get(sec, 0) + rez(n) * float(m.group(6).strip().split()[0].replace(',', '.'))
        except ValueError: cost_by.setdefault(sec, cost_by.get(sec, 0))
    m2 = re.match(r"\| \| \*\*Total ([^*]+)\*\* \| \| \*\*\d+\*\* \| \*\*\d+\*\* \| \| \|", line)
    if m2: line = f"| | **Total {m2.group(1)}** | | **{sec_n}** | **{sec_r}** | | |"; sec_n = sec_r = 0
    out.append(line)
md = '\n'.join(out)
tot_cmd = sum(rez(N[c]) if c not in ('Co', 'Rh') else 0 for c in N) + rez(CO_CARPEN) + rez(CO_SAMB) + rez(RH_CALIN)
silv = sum(v for k, v in cost_by.items() if not any(x in k for x in ('Cobadin', 'Mizil', 'fără furnizor', 'Ionuț')))
md = re.sub(r"- în schemă: \d+ de puieți; de comandat cu rezervă: \d+", f"- în schemă: {tot} de puieți; de comandat cu rezervă: {tot_cmd}", md)
md = re.sub(r"de la Cobadin: \d+ de cătini roșii la 15 lei → ≈ \d+ lei; de la Selficom \d+ sângeri → ≈ \d+ lei", f"de la Cobadin: {rez(buc['Jf'])} de cătini roșii la 15 lei → ≈ {rez(buc['Jf']) * 15:.0f} lei; de la Selficom {rez(buc['Cs'])} sângeri → ≈ {rez(buc['Cs']) * 1.2:.0f} lei", md)
mizil = rez(buc['Cm']) * 18.90 + rez(buc['Ca']) * 13.51 + rez(buc['Ev']) * 9.91 + rez(RH_CALIN) * 18.02
md = re.sub(r"de la Mizil: \d+ de puieți, după oferta primită ≈ [\d,.]+ lei", f"de la Mizil: {rez(buc['Cm']) + rez(buc['Ca']) + rez(buc['Ev']) + rez(RH_CALIN)} de puieți, după oferta primită ≈ {format(mizil, ',.0f').replace(',', ' ')} lei", md)
md = re.sub(r"\(Foresta, Matto Medusa, Doi Cocoși, Țuțora, Agigea, Selficom\): \d+ de puieți; cost cunoscut ≈ \d+ lei", f"(Foresta, Matto Medusa, Doi Cocoși, Țuțora, Agigea, Selficom): {sum(rez(N[c]) for c in ('Qb','Qc','Fo','Pm','Cr','Pc','Lv','Rc','Qp','Um','Ac','Ms','Pa','Tt','Ps','Cc','At','Cs')) + rez(CO_CARPEN)} de puieți; cost cunoscut ≈ {silv:.0f} lei", md)
md = md.replace('(_Fișier generat de `comenzi.py`', '(_Fișier generat de `comenzi.py`')
if '\n_Cantitățile aliniate' not in md: md = md.rstrip('\n') + '\n'
md = re.sub(r"\n_Cantitățile aliniate pe schema \d.*\n?", "\n", md)
md += f"\n_Cantitățile aliniate pe schema {var} (`plantare-miyawaki-est{var}.json`) cu `resurse/oferte/scripts/aliniaza-comenzi.py`._\n"
open(p, 'w', encoding='utf-8').write(md)
# ── lista pentru Ionuț (plan nord + pădure) ──
nord = {'A21': 36, 'A24': 12, 'A52': 21, 'A34': 17, 'A48': 1, 'F28': 6, 'S5': 5}
ion = dict(salcioara=rez(nord['A21']), frasin=rez(nord['A24']), mojdrean=rez(buc['Fo']), tei=rez(nord['A48'] + buc['Tt']), pin=rez(nord['A34'] + buc['Pn']),
           ulm=rez(nord['A52'] + buc['Um']), maces=rez(nord['F28'] + N['Rc']), paducel=rez(nord['S5'] + buc['Cr']), lemn=rez(buc['Lv']), alun=rez(buc['Ca']), soc=rez(buc['Sn']))
print(json.dumps(dict(varianta=var, total=tot, de_comandat=tot_cmd, cost_silvice=round(silv), mizil=round(mizil), ionut=ion, RH_MACES=RH_MACES, CO=(CO_CARPEN, CO_SAMB)), ensure_ascii=False))
