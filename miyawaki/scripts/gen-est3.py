# -*- coding: utf-8 -*-
"""Schema de plantare 3: caroiaj de 2 × 2 m cu 4 rețete (I1, I2, I3 în triunghi + S pe banda de sud).

Pornește de la geometria schemei 2 (poligon, alee, luminiș, caroiaj, fâșia de la gard) luată din
index-est2.html (cadrul rotit, nordul sus) și din plantare-miyawaki-est2.json (cadrul original, pentru x_pct/y_pct).
Scrie: plantare-miyawaki-est3.json, index-est3.html, plan-miyawaki-est3.md.

    python3 miyawaki/scripts/gen-est3.py
"""
import json, re, math, random, collections, html as H, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # miyawaki/
random.seed(3)

page = open(f'{R}/index-est2.html', encoding='utf-8').read()
D = json.loads(re.search(r'const D = (\{.*?\});\n', page, re.S).group(1))     # cadrul rotit
J = json.load(open(f'{R}/plantare-miyawaki-est2.json', encoding='utf-8'))   # cadrul original
SP = {s['cod']: s for s in D['specii']}
TPL = {p['nr']: (p['u'], p['v']) for p in D['caroiaj']['sablon']}
POZ = {'A': [3, 7], 'B': [12, 4, 8, 2], 'C': [1, 6, 11], 'D': [5, 9, 10]}
NUME_STRAT = {'A': 'arbore mare', 'B': 'arbore mic', 'C': 'subarboret', 'D': 'arbust'}
COL = {'A': '#1b5e20', 'B': '#43a047', 'C': '#9e9d24', 'D': '#e08a1e'}

# ── geometrie ──
POLY = D['poligon']; PATH = D['poteca']; SEAT = D['loc_stat']
def pip(x, y, P):
    ins = False
    for i in range(len(P)):
        a, b = P[i], P[(i + 1) % len(P)]
        if (a['y'] > y) != (b['y'] > y) and x < (b['x'] - a['x']) * (y - a['y']) / (b['y'] - a['y']) + a['x']: ins = not ins
    return ins
def dseg(x, y, a, b):
    dx, dy = b['x'] - a['x'], b['y'] - a['y']; L = dx * dx + dy * dy or 1e-9
    t = max(0, min(1, ((x - a['x']) * dx + (y - a['y']) * dy) / L)); return math.hypot(x - a['x'] - t * dx, y - a['y'] - t * dy)
def dpath(x, y): return min(dseg(x, y, PATH[i], PATH[i + 1]) for i in range(len(PATH) - 1))
cy0 = sum(p['y'] for p in POLY) / len(POLY)
SUD = [(POLY[i], POLY[(i + 1) % len(POLY)]) for i in range(len(POLY)) if (POLY[i]['y'] + POLY[(i + 1) % len(POLY)]['y']) / 2 < cy0]
def dsud(x, y): return min(dseg(x, y, a, b) for a, b in SUD)
def ok(x, y): return pip(x, y, POLY) and dpath(x, y) >= 0.65 and math.hypot(x - SEAT['x'], y - SEAT['y']) >= SEAT['r'] + 0.25

# ── pătratele: aceeași grilă ca în schema 2 (toate pătratele care au măcar o poziție plantabilă) ──
C2 = D['caroiaj']; q0 = next(q for q in C2['patrate'] if q['eticheta'] == 'A1')
X0 = max(p['x'] for p in q0['colturi']); Y0 = max(p['y'] for p in q0['colturi'])       # colțul de NE al caroiajului
L = C2['latura_m']; NCOL, NROW = C2['coloane'], C2['randuri']
SQ = []
for r in range(NROW):
    for c in range(NCOL):
        xe, yn = X0 - c * L, Y0 - r * L                              # marginea de est și de nord a pătratului
        pts = {nr: (xe - L + u, yn - L + v) for nr, (u, v) in TPL.items()}
        plant = [nr for nr, (x, y) in pts.items() if ok(x, y)]
        if not plant: continue
        sar = [nr for nr in TPL if nr not in plant]
        motiv = {}
        for nr in sar:
            x, y = pts[nr]
            motiv[nr] = 'pe alee' if pip(x, y, POLY) and dpath(x, y) < 0.65 else ('în luminiș' if pip(x, y, POLY) else 'dincolo de var')
        cx, cyy = xe - L / 2, yn - L / 2
        SQ.append(dict(eticheta=chr(65 + c) + str(r + 1), col=c, rand=r, pts=pts, plantate=plant, sarite=sar, motiv=motiv,
                       tip='S' if dsud(cx, cyy) < 3.0 else 'I', colturi=[dict(x=round(xe, 2), y=round(yn - L, 2)), dict(x=round(xe, 2), y=round(yn, 2)), dict(x=round(xe - L, 2), y=round(yn, 2)), dict(x=round(xe - L, 2), y=round(yn - L, 2))]))
for q in SQ: q['reteta'] = 'S' if q['tip'] == 'S' else 'I' + str((q['col'] + q['rand']) % 3 + 1)

# ── rețetele: sloturile celor 4 rețete, ponderate cu numărul de lăzi (S = I1 fără arborii mari, care sunt pini);
#    speciile primesc sloturi după ținta schemei aleatoare, fiecare cel puțin un slot, fără dubluri în aceeași rețetă ──
uses = collections.Counter(q['reteta'] for q in SQ)
RK = ('I1', 'I2', 'I3', 'S')
STR = {s: [x['cod'] for x in D['specii'] if x['strat'] == s and x['cod'] != 'Pn'] for s in 'ABCD'}
LAY = {k: {} for k in RK}
for s in 'ABCD':
    slots = [(k, p) for k in RK for p in POZ[s] if not (k == 'S' and s == 'A')]
    W = sum(uses[k] for k, _ in slots); tinta = {c: SP[c]['buc_tinta'] for c in STR[s]}; T = sum(tinta.values())
    quota = {c: tinta[c] * W / T for c in STR[s]}; got = {c: 0 for c in STR[s]}
    assert len(STR[s]) <= len(slots), s
    ordine = sorted(slots, key=lambda kp: -uses[kp[0]])
    # întâi câte un slot fiecărei specii (cele cu ținta mare primesc lăzile multe), apoi restul după deficit
    for (k, p), c in zip(ordine, sorted(STR[s], key=lambda c: -quota[c])): LAY[k][p] = c; got[c] += uses[k]
    for k, p in ordine[len(STR[s]):]:
        cand = [c for c in STR[s] if c not in LAY[k].values()]
        c = max(cand, key=lambda c: quota[c] - got[c]); LAY[k][p] = c; got[c] += uses[k]
LAY['S'][3] = LAY['S'][7] = 'Pn'
# ── căutare locală: cât mai puține perechi din aceeași specie prea apropiate, pe toată schema; fără dubluri în aceeași rețetă ──
PRAG = {'A': 1.4, 'B': 1.2, 'C': 1.0, 'D': 0.9}
def plante_din(LAY):
    out = []
    for q in SQ:
        for nr in q['plantate']:
            c = LAY[q['reteta']][nr]; x, y = q['pts'][nr]; out.append((x, y, c, SP[c]['strat']))
    return out
def cost(LAY):
    P = plante_din(LAY); n = 0
    idx = collections.defaultdict(list)
    for i, (x, y, c, s) in enumerate(P): idx[(int(x // 2), int(y // 2))].append(i)
    for (gx, gy), li in idx.items():
        cand = [j for dx in (-1, 0, 1) for dy in (-1, 0, 1) for j in idx.get((gx + dx, gy + dy), [])]
        for i in li:
            for j in cand:
                if j <= i: continue
                if P[i][2] == P[j][2] and math.hypot(P[i][0] - P[j][0], P[i][1] - P[j][1]) < PRAG[P[i][3]]: n += 1
    return n
def dubluri(k): v = [c for c in LAY[k].values() if c != 'Pn']; return len(v) != len(set(v))
best = cost(LAY)
for it in range(4000):
    s = random.choice('ABCD'); k = random.choice([x for x in RK if not (x == 'S' and s == 'A')])
    if random.random() < 0.5:                      # schimb două poziții în aceeași rețetă și strat
        a, b = random.sample(POZ[s], 2); k2 = k
    else:                                            # schimb o specie între două rețete (același strat)
        k2 = random.choice([x for x in RK if x != k and not (x == 'S' and s == 'A')]); a, b = random.choice(POZ[s]), random.choice(POZ[s])
    LAY[k][a], LAY[k2][b] = LAY[k2][b], LAY[k][a]
    cst = cost(LAY)
    if cst <= best and not dubluri(k) and not dubluri(k2): best = cst
    else: LAY[k][a], LAY[k2][b] = LAY[k2][b], LAY[k][a]
print('perechi prea apropiate rămase:', best)
RETETE = {k: [dict(poz=p, u=TPL[p][0], v=TPL[p][1], cod=LAY[k][p], strat=SP[LAY[k][p]]['strat']) for p in sorted(TPL)] for k in RK}

# ── plantele: fâșia de la gard (neschimbată din schema 2) + pătratele ──
fasie = [dict(p) for p in D['plante'] if str(p.get('patrat', '')).startswith('F-')]
plante = []
for q in SQ:
    for nr in q['plantate']:
        c = LAY[q['reteta']][nr]; x, y = q['pts'][nr]
        plante.append(dict(x=round(x, 2), y=round(y, 2), cod=c, ro=SP[c]['ro'], lat=SP[c]['lat'], strat=SP[c]['strat'], patrat=q['eticheta'], poz=nr))
# x_pct / y_pct: transformarea rigidă cadru rotit → cadru original (din vârfurile poligonului), apoi afinitatea original → procente (din plantele schemei 2)
import cmath
zp = [complex(p['x'], p['y']) for p in D['poligon']]; zj = [complex(p['x'], p['y']) for p in J['poligon']]
mp, mj = sum(zp) / len(zp), sum(zj) / len(zj)
rot = sum((b - mj) * (a - mp).conjugate() for a, b in zip(zp, zj)) / sum(abs(a - mp) ** 2 for a in zp); rot /= abs(rot)
def to_orig(x, y): z = rot * (complex(x, y) - mp) + mj; return z.real, z.imag
assert max(abs(rot * (a - mp) + mj - b) for a, b in zip(zp, zj)) < 0.05, 'poligoanele nu se suprapun'
A = [(p['x'], p['y'], 1) for p in J['plante']]; bx = [p['x_pct'] for p in J['plante']]; by = [p['y_pct'] for p in J['plante']]
def lstsq(A, b):
    M = [[sum(a[i] * a[j] for a in A) for j in range(3)] for i in range(3)]; v = [sum(a[i] * bb for a, bb in zip(A, b)) for i in range(3)]
    for i in range(3):
        piv = M[i][i]; M[i] = [m / piv for m in M[i]]; v[i] /= piv
        for r in range(3):
            if r != i: f = M[r][i]; M[r] = [m - f * mi for m, mi in zip(M[r], M[i])]; v[r] -= f * v[i]
    return v
cx_, cy_ = lstsq(A, bx), lstsq(A, by)
for p in plante:
    ox, oy = to_orig(p['x'], p['y']); p['x_pct'] = round(cx_[0] * ox + cx_[1] * oy + cx_[2], 3); p['y_pct'] = round(cy_[0] * ox + cy_[1] * oy + cy_[2], 3)
plante = fasie + plante
for i, p in enumerate(plante, 1): p['nr'] = i
buc = collections.Counter(p['cod'] for p in plante)
specii = [dict(s, buc=buc[s['cod']]) for s in D['specii']]
tot = len(plante); n_str = collections.Counter(p['strat'] for p in plante)
print(f'{tot} puieți: ' + ', '.join(f'{k} {n_str[k]}' for k in 'ABCD') + f' | fâșie {len(fasie)} | pătrate {len(SQ)}: ' + ', '.join(f'{k} {uses[k]}' for k in ('I1', 'I2', 'I3', 'S')) + f' | Pn {buc["Pn"]}')

# ── JSON (cadrul rotit, ca pagina; cheia nord_grade_fata_de_sus spune cât e rotit) ──
CAR = dict(origine=C2['origine'], latura_m=L, coloane=NCOL, randuri=NROW, sablon=C2['sablon'],
           patrate=[dict(eticheta=q['eticheta'], col=q['col'], rand=q['rand'], reteta=q['reteta'], tip=q['tip'], colturi=q['colturi'], plantate=q['plantate'], sarite=q['sarite']) for q in SQ],
           fasie=C2['fasie'])
REG = 'Se plantează doar cuiele care cad în pădure: cuiul care cade pe alee, în luminiș sau dincolo de linia de var se sare, fără înlocuire. Nu există altă regulă: aceeași ladă pe tot pătratul, oricât e de tăiat.'
D3 = dict(D); D3.update(plante=plante, specii=specii, caroiaj=CAR, retete=RETETE, regula_sarit=REG, varianta=3,
          nota_cadru='Coordonatele sunt în cadrul rotit al paginii (gardul de nord orizontal, sus); nord_grade_fata_de_sus dă rotirea față de nordul geografic.')
json.dump(D3, open(f'{R}/plantare-miyawaki-est3.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ── HTML ──
def rt_svg(k, size=170):
    m = 11.1; w = size - 2 * m; px = lambda u: m + u * w / 2; py = lambda v: m + (2 - v) * w / 2
    o = [f'<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg"><rect x="{m}" y="{m}" width="{w:.1f}" height="{w:.1f}" fill="#efe9d8" stroke="#6b5f3a" stroke-width="2"/>',
         f'<line x1="{m}" y1="{m}" x2="{size - m:.1f}" y2="{m}" stroke="#c62828" stroke-width="5"/><text x="{size / 2}" y="{m - 3}" font-size="8" text-anchor="middle" fill="#c62828" font-family="system-ui">latura roșie = spre gardul de nord</text>']
    for u in (0.5, 1.0, 1.5): o.append(f'<line x1="{px(u):.1f}" y1="{m}" x2="{px(u):.1f}" y2="{size - m:.1f}" stroke="#bbb" stroke-width=".6" stroke-dasharray="3 3"/><line x1="{m}" y1="{px(u):.1f}" x2="{size - m:.1f}" y2="{px(u):.1f}" stroke="#bbb" stroke-width=".6" stroke-dasharray="3 3"/>')
    for p in RETETE[k]:
        r = {'A': 9, 'B': 8, 'C': 7, 'D': 6}[p['strat']]
        o.append(f'<circle cx="{px(p["u"]):.1f}" cy="{py(p["v"]):.1f}" r="{r}" fill="{COL[p["strat"]]}" stroke="#fff" stroke-width="1.2"/><text x="{px(p["u"]):.1f}" y="{py(p["v"]) + 2.5:.1f}" font-size="7" font-weight="700" text-anchor="middle" fill="#fff" font-family="system-ui">{p["cod"]}</text><text x="{px(p["u"]):.1f}" y="{py(p["v"]) - r - 1.5:.1f}" font-size="6" text-anchor="middle" fill="#555" font-family="system-ui">{p["poz"]}</text>')
    return ''.join(o) + '</svg>'
def rt_block(k):
    desc = {'I1': 'interior, rețeta 1', 'I2': 'interior, rețeta 2', 'I3': 'interior, rețeta 3', 'S': 'banda de sud: pin negru la pozițiile 3 și 7, restul specii proprii'}[k]
    rows = ''.join(f'<tr><td>{p["poz"]}</td><td><span class="cod" style="background:{COL[p["strat"]]}">{p["cod"]}</span></td><td>{H.escape(SP[p["cod"]]["ro"])}</td><td><i>{H.escape(SP[p["cod"]]["lat"])}</i></td><td>{NUME_STRAT[p["strat"]]}</td></tr>' for p in RETETE[k])
    npl = sum(len(q['plantate']) for q in SQ if q['reteta'] == k)
    return (f'<div class="rt">{rt_svg(k)}<div><b>Rețeta {k}</b> — {desc}; <b>{uses[k]} lăzi</b> (pătrate), {npl} puieți<table><thead><tr><th>Poz.</th><th>Cod</th><th>Specie</th><th>Nume latin</th><th>Strat</th></tr></thead><tbody>{rows}</tbody></table></div></div>')
F = C2['fasie']
sablon = ('<p><b>Rama și șablonul:</b> ramă de 2 × 2 m din șipcă, cu latura de nord vopsită roșu, ținută mereu spre gardul de nord; în ramă, 12 poziții fixe, pe 4 rânduri de câte 3 (de la nord: 1–3, 4–6, 7–9, 10–12; de la vest spre est), '
          'la 0,5 m de margini și 0,5 m între ele, marcate cu sfori între cuie numerotate. Cele două poziții de arbori mari (3 și 7) formează pe tot terenul o rețea cu 1,41 m între arbori. '
          f'Caroiajul pornește de la 2 m de gardul de est și 2 m de gardul de nord; coloanele A, B, C… merg spre vest, rândurile 1, 2, 3… spre sud; {len(SQ)} de pătrate. '
          f'<b>Patru rețete</b>: I1, I2, I3 se rotesc în triunghi pe interior (pătratul de la est și cel de la nord au mereu altă rețetă), S pe banda de sud, cu pin negru la 3 și 7. Lăzile se marchează cu bandă colorată: I1 roșu, I2 galben, I3 albastru, S verde.</p>'
          '<p class="rama-img"><a href="rama-si-lada.png"><img src="rama-si-lada.svg" alt="Rama de 2 × 2 m și lada cu 12 pahare numerotate" style="width:100%;max-width:1100px;display:block;border:1px solid #ddd;border-radius:6px"></a></p>')
regula = f'<p><b>Regula de sărit (singura):</b> {H.escape(REG)} Plantele cu spini care ajung lângă alee (păducel, porumbar, măceș) se taie la sol în anul 2, când se redeschide aleea.</p>'
fasie_txt = (f'<p><b>Fâșia de la gard (F), {len(fasie)} puieți, se plantează prima, pe linie, fără ramă:</b> {H.escape(F["descriere"])} Rotația speciilor pe fiecare rând: '
             + ' → '.join(f'<span class="cod" style="background:{COL[SP[c]["strat"]]}">{c}</span>' for c in F['rotatie']) + ' și de la capăt.</p>')
def lazi_rows():
    return ''.join(f'<tr><td><b>{q["eticheta"]}</b></td><td>{q["reteta"]}</td><td class="n">{len(q["plantate"])}</td><td>{"; ".join(f"{nr} ({q["motiv"][nr]})" for nr in q["sarite"]) or "—"}</td><td>☐</td></tr>' for q in SQ)
lazi_sum = '<p><b>Lăzi de pregătit:</b> ' + ', '.join(f'{k}: {uses[k]}' for k in ('I1', 'I2', 'I3', 'S')) + f' — {len(SQ)} de lăzi în total; sortatorul le umple din snopi după fișa rețetei, cu numărul pătratului pe etichetă. În ordinea plantării: rândul 1 de la A spre J, apoi rândul 2 …</p>'
def cant_rows():
    o = []
    for s in 'ABCD':
        for sp in [x for x in specii if x['strat'] == s]:
            n_f = sum(1 for p in fasie if p['cod'] == sp['cod']); n_q = sp['buc'] - n_f; rez = sp['buc'] + max(1, math.ceil(sp['buc'] * 0.1))
            o.append(f'<tr><td><span class="cod" style="background:{COL[s]}">{sp["cod"]}</span></td><td>{H.escape(sp["ro"])}<br><i style="color:#666">{H.escape(sp["lat"])}</i></td><td>{NUME_STRAT[s]}</td><td class="n">{n_q}</td><td class="n">{n_f}</td><td class="n"><b>{sp["buc"]}</b></td><td class="n">{rez}</td><td class="n" style="color:#777">{sp["buc_tinta"]}</td></tr>')
    rez_tot = sum(x['buc'] + max(1, math.ceil(x['buc'] * 0.1)) for x in specii)
    o.append(f'<tr><td></td><td><b>Total</b></td><td></td><td class="n"><b>{tot - len(fasie)}</b></td><td class="n"><b>{len(fasie)}</b></td><td class="n"><b>{tot}</b></td><td class="n"><b>{rez_tot}</b></td><td class="n" style="color:#777">{sum(x["buc_tinta"] for x in specii)}</td></tr>')
    return ''.join(o)
cant = ('<h2>Cantități — ce se comandă</h2><div class="lazi"><table><thead><tr><th>Cod</th><th>Specie</th><th>Strat</th><th class="n">În pătrate</th><th class="n">În fâșie</th><th class="n">În schemă</th><th class="n">De comandat (+10 %)</th><th class="n">Ținta aleatoare</th></tr></thead><tbody>'
        + cant_rows() + '</tbody></table></div>')
screen = ('<div class="retete retete-screen"><h2>Caroiaj de 2 × 2 m și cele 4 rețete</h2>' + sablon + regula + fasie_txt
          + ''.join(rt_block(k) for k in ('I1', 'I2', 'I3', 'S'))
          + '<h2>Lista lăzilor — pătratele în ordinea plantării</h2>' + lazi_sum + '<div class="lazi"><table><thead><tr><th>Pătrat</th><th>Rețetă</th><th class="n">Puieți</th><th>Poziții sărite</th><th>Plantat</th></tr></thead><tbody>' + lazi_rows() + '</tbody></table></div>'
          + cant + '</div>')
printp = ('<div id="rt-pages"><section class="rt-page"><h2>Rama de 2 × 2 m, regula de sărit și fâșia de la gard</h2>' + sablon + regula + fasie_txt + '</section>'
          + ''.join(f'<section class="rt-page"><h2>Rețeta {k}</h2>{rt_block(k)}</section>' for k in ('I1', 'I2', 'I3', 'S'))
          + '<section class="rt-page"><h2>Lista lăzilor — pătratele în ordinea plantării</h2>' + lazi_sum + '<div class="lazi"><table><thead><tr><th>Pătrat</th><th>Rețetă</th><th class="n">Puieți</th><th>Poziții sărite</th><th>Plantat</th></tr></thead><tbody>' + lazi_rows() + '</tbody></table></div></section>'
          + '<section class="rt-page">' + cant + '</section></div>')
out = page
out = out.replace('schema de plantare2', 'schema de plantare3')
out = re.sub(r'<div class="sub">.*?</div>', lambda m: f'<div class="sub">{D["arie_m2"]:.0f} m², poligonul măsurat în planul nord, pe perdeaua de est · {tot} de puieți din 30 de specii autohtone de silvostepă dobrogeană (inclusiv pin negru) · {tot / D["arie_m2"]:.1f} plante/m² · <b>4 rețete</b> (I1, I2, I3 în triunghi, S cu pini pe banda de sud) și o singură regulă de sărit · fâșia de la gard de {len(fasie)} puieți pe trei rânduri · alee de 80 cm până la luminișul central, care rămâne umbrit · pe 2 m de la gardul de est și de nord doar arbuști (Cod civil art. 613). Apasă pe o plantă sau pe o specie ca s-o evidențiezi. Nordul e sus.</div>', out, count=1, flags=re.S)
strat_names = {'A': 'Arbori mari (coronament, 15–25 m)', 'B': 'Arbori mici (8–15 m)', 'C': 'Subarboret (3–8 m)', 'D': 'Arbuști, manta (1–4 m)'}
out = re.sub(r'(<h2>Straturi</h2>\n).*?(\n    <h2>Specii)', lambda m: m.group(1) + ''.join(f'<div class="strat" onclick="onlyLayer(&quot;{s}&quot;)"><span class="sw" style="background:{COL[s]}"></span>{strat_names[s]} — <b>{n_str[s]}</b></div>' for s in 'ABCD') + m.group(2), out, count=1, flags=re.S)
out = re.sub(r'(<tbody>\n).*?(\n    </tbody>)', lambda m: m.group(1) + ''.join(f'<tr class="sp" data-cod="{s["cod"]}" onclick="onlySpecies(&quot;{s["cod"]}&quot;)"><td><span class="cod" style="background:{COL[s["strat"]]}">{s["cod"]}</span></td><td>{H.escape(s["ro"])}<br><i style="color:#666">{H.escape(s["lat"])}</i></td><td class="n">{s["buc"]}</td></tr>' for s in specii) + m.group(2), out, count=1, flags=re.S)
out = re.sub(r'<div id="rt-pages">.*?</div>\n<div class="retete retete-screen">.*?</div>\n<div id="sp-pages">', lambda m: printp + '\n' + screen + '\n<div id="sp-pages">', out, count=1, flags=re.S)
out = re.sub(r'const D = \{.*?\};\n', lambda m: 'const D = ' + json.dumps(D3, ensure_ascii=False) + ';\n', out, count=1, flags=re.S)
out = out.replace('plantare-miyawaki-est2', 'plantare-miyawaki-est3').replace('plan-miyawaki-est2.md', 'plan-miyawaki-est3.md')
assert 'est2' not in out.replace('index-est2', ''), [l[:80] for l in out.split('\n') if 'est2' in l][:3]
open(f'{R}/index-est3.html', 'w', encoding='utf-8').write(out)

# ── MD ──
md = open(f'{R}/plan-miyawaki-est2.md', encoding='utf-8').read()
md = re.sub(r'^> \*\*Varianta 2, de lucru\*\*.*?\n', '> **Varianta 3, de lucru** — schema 2 refăcută pe 7 noiembrie 2026 cu **4 rețete** în loc de 9 și fără rețeta pentru pătratele tăiate: aceeași ladă pe tot pătratul, o singură regulă de sărit, luminișul rămâne umbrit. Schemele 1 și 2 rămân ca referință.\n', md, count=1, flags=re.M)
md = md.replace('schema de plantare2', 'schema de plantare3').replace('index-est2.html', 'index-est3.html').replace('plantare-miyawaki-est2', 'plantare-miyawaki-est3')
sec6 = f'''## 6. Caroiaj de 2 × 2 m și cele 4 rețete (varianta 3, 7 noiembrie 2026)

Plantarea se face cu o **ramă de 2 × 2 m** mutată pe teren, cu 12 poziții fixe (4 rânduri de câte 3, de la nord: 1–3, 4–6, 7–9, 10–12, de la vest spre est, la 0,5 m de margini și între ele); latura de nord a ramei e roșie și stă mereu spre gardul de nord. Arborii mari sunt la pozițiile 3 și 7, în rețea de 1,41 m pe tot terenul.

![Rama de 2 × 2 m și lada cu 12 pahare numerotate](rama-si-lada.svg)

**Patru rețete, nu nouă:** I1, I2, I3 pe interior, rotite în triunghi (pătratul de la est și cel de la nord au mereu altă rețetă), și S pe banda de sud, cu pin negru la pozițiile 3 și 7 și specii proprii în rest. Fiecare rețetă are 2 arbori mari, 4 arbori mici, 3 arbuști mari și 3 arbuști; cele 29 de specii (fără pin) sunt împărțite pe sloturile celor 4 rețete, ponderat cu numărul de lăzi al fiecăreia, după ținta schemei aleatoare, fiecare specie cel puțin o dată, fără dubluri în aceeași rețetă. Lăzile au bandă colorată: I1 roșu, I2 galben, I3 albastru, S verde.

**Regula de sărit, singura:** {REG} Nu mai există rețeta pentru pătratele tăiate de alee sau de luminiș: se folosește aceeași ladă și se sar pozițiile care nu cad în pădure. Plantele cu spini care ajung lângă alee se taie la sol în anul 2. Luminișul rămâne umbrit (arborii mari pot sta pe marginea lui).

**Fâșia de la gard (F), {len(fasie)} puieți, se plantează prima, pe linie, fără ramă:** {F["descriere"]} Rotația speciilor: {" → ".join(F["rotatie"])}, și de la capăt.

Totaluri: {tot} de puieți ({", ".join(f"{k} {n_str[k]}" for k in "ABCD")}), față de 836 în schema 2 și 937 în schema aleatoare; {len(SQ)} de pătrate ({", ".join(f"{k} {uses[k]}" for k in ("I1", "I2", "I3", "S"))}), {buc["Pn"]} pini pe banda de sud. Coloana „Buc.” din tabelele de mai sus e numărul real din schema pe rețete; ținta din schema aleatoare e în `buc_tinta` din JSON.

''' + ''.join(f'**Rețeta {k}** — {uses[k]} lăzi\n\n| Poz. | Cod | Specie | Strat |\n|---|---|---|---|\n' + ''.join(f'| {p["poz"]} | {p["cod"]} | {SP[p["cod"]]["ro"]} | {NUME_STRAT[p["strat"]]} |\n' for p in RETETE[k]) + '\n' for k in ('I1', 'I2', 'I3', 'S')) + '''### Lista lăzilor — pătratele în ordinea plantării

| Pătrat | Rețetă | Puieți | Poziții sărite |
|---|---|---:|---|
''' + ''.join(f'| {q["eticheta"]} | {q["reteta"]} | {len(q["plantate"])} | {"; ".join(f"{nr} ({q["motiv"][nr]})" for nr in q["sarite"]) or "—"} |\n' for q in SQ) + '''
### Cantități — ce se comandă

| Cod | Specie | Strat | În pătrate | În fâșie | În schemă | De comandat (+10 %) |
|---|---|---|---:|---:|---:|---:|
''' + ''.join(f'| {s["cod"]} | {s["ro"]} | {NUME_STRAT[s["strat"]]} | {s["buc"] - sum(1 for p in fasie if p["cod"] == s["cod"])} | {sum(1 for p in fasie if p["cod"] == s["cod"])} | {s["buc"]} | {s["buc"] + max(1, math.ceil(s["buc"] * 0.1))} |\n' for s in specii) + f'| | **Total** | | {tot - len(fasie)} | {len(fasie)} | **{tot}** | **{sum(x["buc"] + max(1, math.ceil(x["buc"] * 0.1)) for x in specii)}** |\n'
md = re.sub(r'## 6\. Caroiaj.*', sec6, md, count=1, flags=re.S)
md = re.sub(r'\| puieți \| \d+ \|', f'| puieți | {tot} |', md, count=1)
open(f'{R}/plan-miyawaki-est3.md', 'w', encoding='utf-8').write(md)
print('scris: plantare-miyawaki-est3.json, index-est3.html, plan-miyawaki-est3.md')
