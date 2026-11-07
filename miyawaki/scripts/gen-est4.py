# -*- coding: utf-8 -*-
"""Schema de plantare 4: caroiaj de 3 × 3 m cu 30 de poziții și O SINGURĂ rețetă de interior (fiecare specie o dată pe
pătrat, mojdreanul de două ori) + rețeta S pe banda de sud (aceeași, cu 3 pini în locul a 3 arbori mari).

Geometria (poligon, alee, luminiș, fâșia de la gard, originea caroiajului la 2 m de garduri) e cea a schemei 2/3, luată din
index-est2.html (cadrul rotit, nordul sus) și plantare-miyawaki-est2.json (cadrul original, pentru x_pct/y_pct).
Scrie: plantare-miyawaki-est4.json, index-est4.html, plan-miyawaki-est4.md, rama-3x3.svg.

    python3 miyawaki/scripts/gen-est4.py
"""
import json, re, math, random, collections, html as H, os, itertools
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
random.seed(4)
page = open(f'{R}/index-est2.html', encoding='utf-8').read()
D = json.loads(re.search(r'const D = (\{.*?\});\n', page, re.S).group(1))
J = json.load(open(f'{R}/plantare-miyawaki-est2.json', encoding='utf-8'))
SP = {s['cod']: s for s in D['specii']}
NUME_STRAT = {'A': 'arbore mare', 'B': 'arbore mic', 'C': 'subarboret', 'D': 'arbust'}
COL = {'A': '#1b5e20', 'B': '#43a047', 'C': '#9e9d24', 'D': '#e08a1e'}
L = 3.0
US = [0.3, 0.9, 1.5, 2.1, 2.7]; VS = [2.75, 2.25, 1.75, 1.25, 0.75, 0.25]       # 5 coloane × 6 rânduri = 30 de poziții
TPL = {i + 1: (u, v) for i, (v, u) in enumerate((v, u) for v in VS for u in US)}  # 1–5 rândul de nord, de la vest la est

# ── geometrie ──
POLY = D['poligon']; PATH = D['poteca']; SEAT = D['loc_stat']
def pip(x, y, P):
    ins = False
    for i in range(len(P)):
        a, b = P[i], P[(i + 1) % len(P)]
        if (a['y'] > y) != (b['y'] > y) and x < (b['x'] - a['x']) * (y - a['y']) / (b['y'] - a['y']) + a['x']: ins = not ins
    return ins
def dseg(x, y, a, b):
    dx, dy = b['x'] - a['x'], b['y'] - a['y']; Lq = dx * dx + dy * dy or 1e-9
    t = max(0, min(1, ((x - a['x']) * dx + (y - a['y']) * dy) / Lq)); return math.hypot(x - a['x'] - t * dx, y - a['y'] - t * dy)
def dpath(x, y): return min(dseg(x, y, PATH[i], PATH[i + 1]) for i in range(len(PATH) - 1))
cy0 = sum(p['y'] for p in POLY) / len(POLY)
SUD = [(POLY[i], POLY[(i + 1) % len(POLY)]) for i in range(len(POLY)) if (POLY[i]['y'] + POLY[(i + 1) % len(POLY)]['y']) / 2 < cy0]
def dsud(x, y): return min(dseg(x, y, a, b) for a, b in SUD)
def ok(x, y): return pip(x, y, POLY) and dpath(x, y) >= 0.65 and math.hypot(x - SEAT['x'], y - SEAT['y']) >= SEAT['r'] + 0.25

# ── pozițiile straturilor în șablon: 6 arbori mari cât mai departe unul de altul (și de cei din pătratele vecine, perioada 3 m) ──
def dtor(a, b): dx = abs(a[0] - b[0]); dy = abs(a[1] - b[1]); return math.hypot(min(dx, L - dx), min(dy, L - dy))
best = None
for comb in itertools.combinations(range(1, 31), 6):
    m = min(dtor(TPL[a], TPL[b]) for a, b in itertools.combinations(comb, 2))
    if best is None or m > best[0] + 1e-9: best = (m, comb)
A_POS = list(best[1]); print('arbori mari la', A_POS, 'distanța minimă (și între pătrate)', round(best[0], 2), 'm')
rest = [p for p in TPL if p not in A_POS]
# B (9: 8 specii + mojdrean dublu) cât mai departe între ele, apoi C (6), D (9) pe ce rămâne, amestecate
def pick(cands, n):
    bestc = None
    for _ in range(4000):
        c = random.sample(cands, n); m = min(dtor(TPL[a], TPL[b]) for a, b in itertools.combinations(c, 2))
        if bestc is None or m > bestc[0]: bestc = (m, c)
    return sorted(bestc[1])
B_POS = pick(rest, 9); rest = [p for p in rest if p not in B_POS]
C_POS = pick(rest, 6); D_POS = sorted(p for p in rest if p not in C_POS)
POZ = {'A': A_POS, 'B': B_POS, 'C': C_POS, 'D': D_POS}
STR = {s: [x['cod'] for x in D['specii'] if x['strat'] == s and x['cod'] != 'Pn'] for s in 'ABCD'}
STR['B'] = STR['B'] + ['Fo']                                   # al 9-lea slot B: mojdreanul, specia de bază a pădurilor Babadag
random.shuffle(STR['B']); random.shuffle(STR['C']); random.shuffle(STR['D'])
# dublura de mojdrean cât mai departe de prima
fo = [p for p, c in zip(B_POS, STR['B']) if c == 'Fo']
if dtor(TPL[fo[0]], TPL[fo[1]]) < 1.2:
    for i, p in enumerate(B_POS):
        if STR['B'][i] != 'Fo' and dtor(TPL[p], TPL[fo[0]]) >= 1.5:
            j = B_POS.index(fo[1]); STR['B'][i], STR['B'][j] = STR['B'][j], STR['B'][i]; break
LAY = {}
for s in 'ABCD':
    for p, c in zip(POZ[s], STR[s]): LAY[p] = c
I_LAY = dict(LAY)
S_LAY = dict(LAY)
for p in [p for p in A_POS if LAY[p] in ('Qc', 'Um', 'St', 'Tt')]: S_LAY[p] = 'Pn'     # pe sud: cer, ulm, sorb și tei → pin negru
LAYS = {'I': I_LAY, 'S': S_LAY}

# ── pătratele ──
C2 = D['caroiaj']; q0 = next(q for q in C2['patrate'] if q['eticheta'] == 'A1')
X0 = max(p['x'] for p in q0['colturi']); Y0 = max(p['y'] for p in q0['colturi'])
NCOL = math.ceil((X0 - min(p['x'] for p in POLY)) / L); NROW = math.ceil((Y0 - min(p['y'] for p in POLY)) / L)
SQ = []
for r in range(NROW):
    for c in range(NCOL):
        xe, yn = X0 - c * L, Y0 - r * L
        pts = {nr: (xe - L + u, yn - L + v) for nr, (u, v) in TPL.items()}
        plant = [nr for nr, (x, y) in pts.items() if ok(x, y)]
        if not plant: continue
        sar = [nr for nr in TPL if nr not in plant]
        motiv = {nr: ('pe alee' if pip(*pts[nr], POLY) and dpath(*pts[nr]) < 0.65 else ('în luminiș' if pip(*pts[nr], POLY) else 'dincolo de var')) for nr in sar}
        tip = 'S' if dsud(xe - L / 2, yn - L / 2) < 3.0 else 'I'
        SQ.append(dict(eticheta=chr(65 + c) + str(r + 1), col=c, rand=r, pts=pts, plantate=plant, sarite=sar, motiv=motiv, tip=tip, reteta=tip,
                       colturi=[dict(x=round(xe, 2), y=round(yn - L, 2)), dict(x=round(xe, 2), y=round(yn, 2)), dict(x=round(xe - L, 2), y=round(yn, 2)), dict(x=round(xe - L, 2), y=round(yn - L, 2))]))
uses = collections.Counter(q['reteta'] for q in SQ)
RETETE = {k: [dict(poz=p, u=TPL[p][0], v=TPL[p][1], cod=LAYS[k][p], strat=SP[LAYS[k][p]]['strat']) for p in sorted(TPL)] for k in ('I', 'S')}

# ── plantele ──
fasie = [dict(p) for p in D['plante'] if str(p.get('patrat', '')).startswith('F-')]
plante = []
for q in SQ:
    for nr in q['plantate']:
        c = LAYS[q['reteta']][nr]; x, y = q['pts'][nr]
        plante.append(dict(x=round(x, 2), y=round(y, 2), cod=c, ro=SP[c]['ro'], lat=SP[c]['lat'], strat=SP[c]['strat'], patrat=q['eticheta'], poz=nr))
zp = [complex(p['x'], p['y']) for p in D['poligon']]; zj = [complex(p['x'], p['y']) for p in J['poligon']]
mp, mj = sum(zp) / len(zp), sum(zj) / len(zj)
rot = sum((b - mj) * (a - mp).conjugate() for a, b in zip(zp, zj)) / sum(abs(a - mp) ** 2 for a in zp); rot /= abs(rot)
def to_orig(x, y): z = rot * (complex(x, y) - mp) + mj; return z.real, z.imag
A_ = [(p['x'], p['y'], 1) for p in J['plante']]; bx = [p['x_pct'] for p in J['plante']]; by = [p['y_pct'] for p in J['plante']]
def lstsq(A, b):
    M = [[sum(a[i] * a[j] for a in A) for j in range(3)] for i in range(3)]; v = [sum(a[i] * bb for a, bb in zip(A, b)) for i in range(3)]
    for i in range(3):
        piv = M[i][i]; M[i] = [m / piv for m in M[i]]; v[i] /= piv
        for r in range(3):
            if r != i: f = M[r][i]; M[r] = [m - f * mi for m, mi in zip(M[r], M[i])]; v[r] -= f * v[i]
    return v
cx_, cy_ = lstsq(A_, bx), lstsq(A_, by)
for p in plante:
    ox, oy = to_orig(p['x'], p['y']); p['x_pct'] = round(cx_[0] * ox + cx_[1] * oy + cx_[2], 3); p['y_pct'] = round(cy_[0] * ox + cy_[1] * oy + cy_[2], 3)
plante = fasie + plante
for i, p in enumerate(plante, 1): p['nr'] = i
buc = collections.Counter(p['cod'] for p in plante)
specii = [dict(s, buc=buc[s['cod']]) for s in D['specii']]
tot = len(plante); n_str = collections.Counter(p['strat'] for p in plante)
# verificare: distanța minimă între doi din aceeași specie, pe toată schema
mind = 9
for a, b in itertools.combinations([p for p in plante if not str(p['patrat']).startswith('F-')], 2):
    if a['cod'] == b['cod']: mind = min(mind, math.hypot(a['x'] - b['x'], a['y'] - b['y']))
print(f'{tot} puieți: ' + ', '.join(f'{k} {n_str[k]}' for k in 'ABCD') + f' | fâșie {len(fasie)} | pătrate {len(SQ)}: I {uses["I"]}, S {uses["S"]} | Pn {buc["Pn"]} | aceeași specie la cel puțin {mind:.2f} m în pătrate')

REG = 'Se plantează doar cuiele care cad în pădure: cuiul care cade pe alee, în luminiș sau dincolo de linia de var se sare, fără înlocuire. Aceeași rețetă pe toate pătratele; pe cele de sud, patru cuie de arbori mari primesc pin negru.'
CAR = dict(origine=C2['origine'], latura_m=L, coloane=NCOL, randuri=NROW, sablon=[dict(nr=n, u=u, v=v) for n, (u, v) in TPL.items()],
           patrate=[dict(eticheta=q['eticheta'], col=q['col'], rand=q['rand'], reteta=q['reteta'], tip=q['tip'], colturi=q['colturi'], plantate=q['plantate'], sarite=q['sarite']) for q in SQ], fasie=C2['fasie'])
D4 = dict(D); D4.update(plante=plante, specii=specii, caroiaj=CAR, retete=RETETE, regula_sarit=REG, varianta=4,
          nota_cadru='Coordonatele sunt în cadrul rotit al paginii (gardul de nord orizontal, sus); nord_grade_fata_de_sus dă rotirea față de nordul geografic.')
json.dump(D4, open(f'{R}/plantare-miyawaki-est4.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ── desenul ramei de 3 × 3 m cu cele 30 de cuie și fișa cui → specie ──
def rama_svg():
    W, Hh = 1800, 1000; S = 240; X0r, Y0r = 90, 120; t = 20; o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}" font-family="system-ui, Segoe UI, Helvetica, Arial, sans-serif"><rect width="{W}" height="{Hh}" fill="#fbfaf5"/>')
    o.append(f'<text x="40" y="52" font-size="28" font-weight="700" fill="#1f4d33">Rama de 3 × 3 m cu 30 de cuie — aceeași rețetă pe toate pătratele</text>')
    o.append(f'<rect x="{X0r - t}" y="{Y0r - t}" width="{3 * S + 2 * t}" height="{t}" fill="#c62828"/><rect x="{X0r - t}" y="{Y0r + 3 * S}" width="{3 * S + 2 * t}" height="{t}" fill="#b08a55"/><rect x="{X0r - t}" y="{Y0r}" width="{t}" height="{3 * S}" fill="#b08a55"/><rect x="{X0r + 3 * S}" y="{Y0r}" width="{t}" height="{3 * S}" fill="#b08a55"/><rect x="{X0r}" y="{Y0r}" width="{3 * S}" height="{3 * S}" fill="#efe9d8"/>')
    o.append(f'<text x="{X0r + 1.5 * S}" y="{Y0r - t - 8}" font-size="15" font-weight="700" fill="#c62828" text-anchor="middle">LATURA ROȘIE = SPRE GARDUL DE NORD</text>')
    for u in US:
        x = X0r + u * S; o.append(f'<line x1="{x:.0f}" y1="{Y0r}" x2="{x:.0f}" y2="{Y0r + 3 * S}" stroke="#555" stroke-width="2" stroke-dasharray="7 5"/><circle cx="{x:.0f}" cy="{Y0r - t / 2}" r="5" fill="#222"/><circle cx="{x:.0f}" cy="{Y0r + 3 * S + t / 2}" r="5" fill="#222"/><text x="{x:.0f}" y="{Y0r + 3 * S + t + 26}" font-size="14" text-anchor="middle" fill="#333">{u:.1f} m</text>'.replace('.', ','))
    for v in VS:
        y = Y0r + (3 - v) * S; o.append(f'<line x1="{X0r}" y1="{y:.0f}" x2="{X0r + 3 * S}" y2="{y:.0f}" stroke="#555" stroke-width="2" stroke-dasharray="7 5"/><circle cx="{X0r - t / 2}" cy="{y:.0f}" r="5" fill="#222"/><circle cx="{X0r + 3 * S + t / 2}" cy="{y:.0f}" r="5" fill="#222"/><text x="{X0r - t - 8}" y="{y + 5:.0f}" font-size="14" text-anchor="end" fill="#333">{v:.2f} m</text>'.replace('.', ','))
    for nr, (u, v) in TPL.items():
        x, y = X0r + u * S, Y0r + (3 - v) * S; c = I_LAY[nr]; st = SP[c]['strat']; r = 24 if st == 'A' else 19
        o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{COL[st]}" stroke="#fff" stroke-width="3"/><text x="{x:.0f}" y="{y + 5:.0f}" font-size="15" font-weight="700" fill="#fff" text-anchor="middle">{c}</text><text x="{x:.0f}" y="{y - r - 4:.0f}" font-size="13" font-weight="700" fill="#333" text-anchor="middle">{nr}</text>')
        if S_LAY[nr] == 'Pn': o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r + 5}" fill="none" stroke="#0b3d91" stroke-width="3" stroke-dasharray="4 3"/>')
    o.append(f'<text x="{X0r - t}" y="{Y0r + 3 * S + t + 56}" font-size="14" fill="#333">Cuie pe scânduri: 0,3 · 0,9 · 1,5 · 2,1 · 2,7 m (sus/jos) și 0,25 · 0,75 · 1,25 · 1,75 · 2,25 · 2,75 m (stânga/dreapta); sfori între cuiele opuse; numerotarea 1–30 de la nord spre sud, de la vest spre est.</text>')
    o.append(f'<text x="{X0r - t}" y="{Y0r + 3 * S + t + 78}" font-size="14" fill="#333">Cercul albastru punctat: pe pătratele de sud (S), la aceste cuie se pune pin negru în locul speciei scrise. Șipcă de 4,8 × 2,4 cm (4 bucăți de 3,05 m), diagonală, două mânere, doi oameni.</text>')
    # fișa cui → specie, două coloane
    fx, fy = X0r + 3 * S + t + 70, Y0r - 10
    o.append(f'<text x="{fx}" y="{fy}" font-size="20" font-weight="700" fill="#333">Fișa cui → specie (aceeași pentru toate pătratele)</text>')
    for i, nr in enumerate(sorted(TPL)):
        c = I_LAY[nr]; st = SP[c]['strat']; col = i // 15; row = i % 15; x = fx + col * 300; y = fy + 34 + row * 36
        o.append(f'<text x="{x}" y="{y}" font-size="16" font-weight="700" fill="#333">{nr}</text><rect x="{x + 34}" y="{y - 15}" width="38" height="21" rx="4" fill="{COL[st]}"/><text x="{x + 53}" y="{y}" font-size="13" font-weight="700" fill="#fff" text-anchor="middle">{c}</text><text x="{x + 82}" y="{y}" font-size="15" fill="#333">{H.escape(SP[c]["ro"])}' + (f' <tspan fill="#0b3d91" font-weight="700">· pe S: pin negru</tspan>' if S_LAY[nr] == 'Pn' else '') + '</text>')
    for i, ln in enumerate(['Fără lăzi: un singur set de 30 de saci numerotați, pe roabă, umplut dimineața din snopi;', 'alergătorul dă sacul cu numărul cuiului. Pe pătratele S, 4 saci în plus cu pin negru.', 'Cazmaua: despicătură, coletul la nivelul solului, închis apăsând cu palmele', '(niciodată cu piciorul), un smuls ușor de verificare.']):
        o.append(f'<text x="{fx}" y="{fy + 34 + 15 * 36 + 10 + i * 22}" font-size="14" fill="#333">{ln}</text>')
    return ''.join(o) + '</svg>'
open(f'{R}/rama-3x3.svg', 'w', encoding='utf-8').write(rama_svg())

# ── HTML ──
def rt_svg(k, size=230):
    m = 11; w = size - 2 * m; px = lambda u: m + u * w / 3; py = lambda v: m + (3 - v) * w / 3
    o = [f'<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg"><rect x="{m}" y="{m}" width="{w}" height="{w}" fill="#efe9d8" stroke="#6b5f3a" stroke-width="2"/><line x1="{m}" y1="{m}" x2="{size - m}" y2="{m}" stroke="#c62828" stroke-width="5"/><text x="{size / 2}" y="{m - 3}" font-size="8" text-anchor="middle" fill="#c62828" font-family="system-ui">latura roșie = spre gardul de nord</text>']
    for u in US: o.append(f'<line x1="{px(u):.1f}" y1="{m}" x2="{px(u):.1f}" y2="{size - m}" stroke="#bbb" stroke-width=".6" stroke-dasharray="3 3"/>')
    for v in VS: o.append(f'<line x1="{m}" y1="{py(v):.1f}" x2="{size - m}" y2="{py(v):.1f}" stroke="#bbb" stroke-width=".6" stroke-dasharray="3 3"/>')
    for p in RETETE[k]:
        r = {'A': 9, 'B': 8, 'C': 7, 'D': 6}[p['strat']]
        o.append(f'<circle cx="{px(p["u"]):.1f}" cy="{py(p["v"]):.1f}" r="{r}" fill="{COL[p["strat"]]}" stroke="#fff" stroke-width="1.2"/><text x="{px(p["u"]):.1f}" y="{py(p["v"]) + 2.5:.1f}" font-size="6.5" font-weight="700" text-anchor="middle" fill="#fff" font-family="system-ui">{p["cod"]}</text><text x="{px(p["u"]):.1f}" y="{py(p["v"]) - r - 1.5:.1f}" font-size="6" text-anchor="middle" fill="#555" font-family="system-ui">{p["poz"]}</text>')
    return ''.join(o) + '</svg>'
def rt_block(k):
    desc = {'I': 'interior: fiecare specie o dată pe pătrat (mojdreanul de două ori)', 'S': 'banda de sud: aceeași rețetă, cu pin negru la cuiele ' + ', '.join(str(p) for p in sorted(TPL) if S_LAY[p] == 'Pn') + ' în locul cerului, ulmului, sorbului și teiului'}[k]
    rows = ''.join(f'<tr><td>{p["poz"]}</td><td><span class="cod" style="background:{COL[p["strat"]]}">{p["cod"]}</span></td><td>{H.escape(SP[p["cod"]]["ro"])}</td><td><i>{H.escape(SP[p["cod"]]["lat"])}</i></td><td>{NUME_STRAT[p["strat"]]}</td></tr>' for p in RETETE[k])
    npl = sum(len(q['plantate']) for q in SQ if q['reteta'] == k)
    return f'<div class="rt">{rt_svg(k)}<div><b>Rețeta {k}</b> — {desc}; <b>{uses[k]} pătrate</b>, {npl} puieți<table style="column-count:1"><thead><tr><th>Cui</th><th>Cod</th><th>Specie</th><th>Nume latin</th><th>Strat</th></tr></thead><tbody>{rows}</tbody></table></div></div>'
F = C2['fasie']
sablon = (f'<p><b>Rama de 3 × 3 m și cele 30 de cuie:</b> ramă din șipcă cu latura de nord vopsită roșu, ținută mereu spre gardul de nord; cuie la 0,3 · 0,9 · 1,5 · 2,1 · 2,7 m pe laturile de nord și de sud și la 0,25 · 0,75 · 1,25 · 1,75 · 2,25 · 2,75 m pe laturile de est și de vest; sforile între cuiele opuse dau cele 30 de poziții, numerotate 1–30 de la nord spre sud și de la vest spre est. '
          f'<b>O singură rețetă</b>: fiecare specie are mereu același cui, în orice pătrat; pe pătratele de sud, patru cuie de arbori mari primesc pin negru. Caroiajul pornește de la 2 m de gardul de est și 2 m de gardul de nord; coloanele A, B, C… merg spre vest, rândurile 1, 2, 3… spre sud; {len(SQ)} de pătrate. '
          f'<b>Fără lăzi</b>: un singur set de 30 de saci numerotați pe o roabă, umplut dimineața din snopi; fișa cui → specie e una pentru toată pădurea.</p>'
          '<p><b>De tipărit:</b> <a href="retete-est4.pdf">cele două rețete pe A4 orizontal, cu numele complet al speciei la fiecare cui (PDF)</a> · <a href="retete-est4.html">varianta HTML</a> · <a href="rama-3x3.png">desenul ramei cu fișa cui → specie (PNG)</a>.</p>'
          '<p class="rama-img"><a href="rama-3x3.svg"><img src="rama-3x3.svg" alt="Rama de 3 × 3 m cu 30 de cuie și fișa cui → specie" style="width:100%;max-width:1100px;display:block;border:1px solid #ddd;border-radius:6px"></a></p>')
regula = f'<p><b>Regula de sărit (singura):</b> {H.escape(REG)} Plantele cu spini care ajung lângă alee (păducel, porumbar, măceș) se taie la sol în anul 2, când se redeschide aleea.</p>'
fasie_txt = (f'<p><b>Fâșia de la gard (F), {len(fasie)} puieți, se plantează prima, pe linie, fără ramă:</b> {H.escape(F["descriere"])} Rotația speciilor pe fiecare rând: ' + ' → '.join(f'<span class="cod" style="background:{COL[SP[c]["strat"]]}">{c}</span>' for c in F['rotatie']) + ' și de la capăt.</p>')
def lazi_rows(): return ''.join(f'<tr><td><b>{q["eticheta"]}</b></td><td>{q["reteta"]}</td><td class="n">{len(q["plantate"])}</td><td>{"; ".join(f"{nr} ({q["motiv"][nr]})" for nr in q["sarite"]) or "—"}</td><td>☐</td></tr>' for q in SQ)
lazi_sum = f'<p><b>{len(SQ)} de pătrate</b> ({uses["I"]} de interior, {uses["S"]} pe banda de sud), în ordinea plantării: rândul 1 de la A spre vest, apoi rândul 2 … Un pătrat întreg are 30 de puieți; cele tăiate de alee, de luminiș sau de linia de var au mai puțini, cuiele sărite sunt în tabel.</p>'
def cant_rows():
    o = []
    for s in 'ABCD':
        for sp in [x for x in specii if x['strat'] == s]:
            n_f = sum(1 for p in fasie if p['cod'] == sp['cod']); n_q = sp['buc'] - n_f; rez = sp['buc'] + max(1, math.ceil(sp['buc'] * 0.1))
            o.append(f'<tr><td><span class="cod" style="background:{COL[s]}">{sp["cod"]}</span></td><td>{H.escape(sp["ro"])}<br><i style="color:#666">{H.escape(sp["lat"])}</i></td><td>{NUME_STRAT[s]}</td><td class="n">{n_q}</td><td class="n">{n_f}</td><td class="n"><b>{sp["buc"]}</b></td><td class="n">{rez}</td><td class="n" style="color:#777">{sp["buc_tinta"]}</td></tr>')
    rez_tot = sum(x['buc'] + max(1, math.ceil(x['buc'] * 0.1)) for x in specii)
    o.append(f'<tr><td></td><td><b>Total</b></td><td></td><td class="n"><b>{tot - len(fasie)}</b></td><td class="n"><b>{len(fasie)}</b></td><td class="n"><b>{tot}</b></td><td class="n"><b>{rez_tot}</b></td><td class="n" style="color:#777">{sum(x["buc_tinta"] for x in specii)}</td></tr>')
    return ''.join(o)
cant = '<h2>Cantități — ce se comandă</h2><div class="lazi"><table><thead><tr><th>Cod</th><th>Specie</th><th>Strat</th><th class="n">În pătrate</th><th class="n">În fâșie</th><th class="n">În schemă</th><th class="n">De comandat (+10 %)</th><th class="n">Ținta aleatoare</th></tr></thead><tbody>' + cant_rows() + '</tbody></table></div>'
LT = '<h2>Lista pătratelor — în ordinea plantării</h2>'
TBL = '<div class="lazi"><table><thead><tr><th>Pătrat</th><th>Rețetă</th><th class="n">Puieți</th><th>Cuie sărite</th><th>Plantat</th></tr></thead><tbody>' + lazi_rows() + '</tbody></table></div>'
screen = '<div class="retete retete-screen"><h2>Caroiaj de 3 × 3 m, o singură rețetă</h2>' + sablon + regula + fasie_txt + rt_block('I') + rt_block('S') + LT + lazi_sum + TBL + cant + '</div>'
printp = ('<div id="rt-pages"><section class="rt-page"><h2>Rama de 3 × 3 m, regula de sărit și fâșia de la gard</h2>' + sablon + regula + fasie_txt + '</section>'
          + ''.join(f'<section class="rt-page"><h2>Rețeta {k}</h2>{rt_block(k)}</section>' for k in ('I', 'S'))
          + '<section class="rt-page">' + LT + lazi_sum + TBL + '</section><section class="rt-page">' + cant + '</section></div>')
out = page
out = out.replace('schema de plantare2', 'schema de plantare4')
out = out.replace('.rt-page .rt svg { width:230px; height:230px; }', '.rt-page .rt svg { width:300px; height:300px; }').replace('.rt svg { width:170px; height:170px; flex:0 0 auto; }', '.rt svg { width:260px; height:260px; flex:0 0 auto; }')
out = re.sub(r'<div class="sub">.*?</div>', lambda m: f'<div class="sub">{D["arie_m2"]:.0f} m², poligonul măsurat în planul nord, pe perdeaua de est · {tot} de puieți din 30 de specii autohtone de silvostepă dobrogeană (inclusiv pin negru) · {tot / D["arie_m2"]:.1f} plante/m² · <b>caroiaj de 3 × 3 m cu 30 de cuie și o singură rețetă</b> (fiecare specie are mereu același cui; pe banda de sud 4 cuie primesc pin negru), fără lăzi, o singură regulă de sărit · fâșia de la gard de {len(fasie)} puieți pe trei rânduri · alee de 80 cm până la luminișul central, care rămâne umbrit · pe 2 m de la gardul de est și de nord doar arbuști (Cod civil art. 613). Apasă pe o plantă sau pe o specie ca s-o evidențiezi. Nordul e sus.</div>', out, count=1, flags=re.S)
strat_names = {'A': 'Arbori mari (coronament, 15–25 m)', 'B': 'Arbori mici (8–15 m)', 'C': 'Subarboret (3–8 m)', 'D': 'Arbuști, manta (1–4 m)'}
out = re.sub(r'(<h2>Straturi</h2>\n).*?(\n    <h2>Specii)', lambda m: m.group(1) + ''.join(f'<div class="strat" onclick="onlyLayer(&quot;{s}&quot;)"><span class="sw" style="background:{COL[s]}"></span>{strat_names[s]} — <b>{n_str[s]}</b></div>' for s in 'ABCD') + m.group(2), out, count=1, flags=re.S)
out = re.sub(r'(<tbody>\n).*?(\n    </tbody>)', lambda m: m.group(1) + ''.join(f'<tr class="sp" data-cod="{s["cod"]}" onclick="onlySpecies(&quot;{s["cod"]}&quot;)"><td><span class="cod" style="background:{COL[s["strat"]]}">{s["cod"]}</span></td><td>{H.escape(s["ro"])}<br><i style="color:#666">{H.escape(s["lat"])}</i></td><td class="n">{s["buc"]}</td></tr>' for s in specii) + m.group(2), out, count=1, flags=re.S)
out = re.sub(r'<div id="rt-pages">.*?</div>\n<div class="retete retete-screen">.*?</div>\n<div id="sp-pages">', lambda m: printp + '\n' + screen + '\n<div id="sp-pages">', out, count=1, flags=re.S)
out = re.sub(r'const D = \{.*?\};\n', lambda m: 'const D = ' + json.dumps(D4, ensure_ascii=False) + ';\n', out, count=1, flags=re.S)
out = out.replace('plantare-miyawaki-est2', 'plantare-miyawaki-est4').replace('plan-miyawaki-est2.md', 'plan-miyawaki-est4.md').replace("'Pătrate 2 m", "'Pătrate 3 m").replace('>Pătrate 2 m ✓<', '>Pătrate 3 m ✓<')
out = out.replace("bg.setAttribute('width', 52)", "bg.setAttribute('width', 44)")
assert 'est2' not in out.replace('index-est2', ''), [l[:80] for l in out.split('\n') if 'est2' in l][:3]
open(f'{R}/index-est4.html', 'w', encoding='utf-8').write(out)

# ── MD ──
md = open(f'{R}/plan-miyawaki-est2.md', encoding='utf-8').read()
md = re.sub(r'^> \*\*Varianta 2, de lucru\*\*.*?\n', '> **Varianta 4, de lucru** — caroiaj de 3 × 3 m cu 30 de cuie și o singură rețetă (8 noiembrie 2026), fără lăzi: fiecare specie are mereu același cui; pe banda de sud, 4 cuie de arbori mari primesc pin negru. Schemele 1–3 rămân ca referință.\n', md, count=1, flags=re.M)
md = md.replace('schema de plantare2', 'schema de plantare4').replace('index-est2.html', 'index-est4.html').replace('plantare-miyawaki-est2', 'plantare-miyawaki-est4')
sec6 = f'''## 6. Caroiaj de 3 × 3 m, o singură rețetă (varianta 4, 8 noiembrie 2026)

Plantarea se face cu o **ramă de 3 × 3 m** mutată pe teren, cu **30 de poziții** fixe (5 coloane la 0,6 m × 6 rânduri la 0,5 m, numerotate 1–30 de la nord spre sud și de la vest spre est); latura de nord a ramei e roșie și stă mereu spre gardul de nord. Arborii mari sunt la cuiele {", ".join(map(str, A_POS))}, la cel puțin {best[0]:.1f} m unul de altul, și în pătratele vecine.

![Rama de 3 × 3 m cu 30 de cuie și fișa cui → specie](rama-3x3.svg)

**O singură rețetă**: fiecare dintre cele 29 de specii (fără pin) are mereu același cui, în orice pătrat; mojdreanul are două. Pe pătratele de sud (S), cuiele {", ".join(str(p) for p in sorted(TPL) if S_LAY[p] == 'Pn')} primesc pin negru în locul cerului, ulmului, sorbului și teiului. Un pătrat are 30 de puieți, 3,3/m²; aceeași specie se repetă la 3 m. **Fără lăzi**: un singur set de 30 de saci numerotați pe roabă, umplut dimineața din snopi; alergătorul dă sacul cu numărul cuiului.

**Regula de sărit, singura:** {REG} Plantele cu spini care ajung lângă alee se taie la sol în anul 2. Luminișul rămâne umbrit.

**Fâșia de la gard (F), {len(fasie)} puieți, se plantează prima, pe linie, fără ramă:** {F["descriere"]} Rotația speciilor: {" → ".join(F["rotatie"])}, și de la capăt.

Totaluri: {tot} de puieți ({", ".join(f"{k} {n_str[k]}" for k in "ABCD")}); {len(SQ)} de pătrate (I {uses["I"]}, S {uses["S"]}), {buc["Pn"]} pini pe banda de sud. Trasarea: conturul cu alb, caroiajul de 3 m cu roșu ({NCOL + NROW + 2} linii), eticheta pătratului în colțul de nord-vest.

**Fișa cui → specie** (rețeta I; pe S, cuiele marcate primesc pin negru)

| Cui | Cod | Specie | Strat |
|---|---|---|---|
''' + ''.join(f'| {p["poz"]} | {p["cod"]} | {SP[p["cod"]]["ro"]}{" — pe S: pin negru" if S_LAY[p["poz"]] == "Pn" else ""} | {NUME_STRAT[p["strat"]]} |\n' for p in RETETE['I']) + '''
### Lista pătratelor — în ordinea plantării

| Pătrat | Rețetă | Puieți | Cuie sărite |
|---|---|---:|---|
''' + ''.join(f'| {q["eticheta"]} | {q["reteta"]} | {len(q["plantate"])} | {"; ".join(f"{nr} ({q["motiv"][nr]})" for nr in q["sarite"]) or "—"} |\n' for q in SQ) + '''
### Cantități — ce se comandă

| Cod | Specie | Strat | În pătrate | În fâșie | În schemă | De comandat (+10 %) |
|---|---|---|---:|---:|---:|---:|
''' + ''.join(f'| {s["cod"]} | {s["ro"]} | {NUME_STRAT[s["strat"]]} | {s["buc"] - sum(1 for p in fasie if p["cod"] == s["cod"])} | {sum(1 for p in fasie if p["cod"] == s["cod"])} | {s["buc"]} | {s["buc"] + max(1, math.ceil(s["buc"] * 0.1))} |\n' for s in specii) + f'| | **Total** | | {tot - len(fasie)} | {len(fasie)} | **{tot}** | **{sum(x["buc"] + max(1, math.ceil(x["buc"] * 0.1)) for x in specii)}** |\n'
md = re.sub(r'## 6\. Caroiaj.*', sec6, md, count=1, flags=re.S)
md = re.sub(r'\| puieți \| \d+ \|', f'| puieți | {tot} |', md, count=1)
open(f'{R}/plan-miyawaki-est4.md', 'w', encoding='utf-8').write(md)
print('scris: plantare-miyawaki-est4.json, index-est4.html, plan-miyawaki-est4.md, rama-3x3.svg')

# ── retete-est4.html: cele două rețete pe A4 orizontal, cu numele complet al speciei la fiecare cui ──
def rt_full_svg(k):
    Wm = 170.0; m = 10.0; w = Wm - 2 * m; px = lambda u: m + u * w / 3; py = lambda v: m + (3 - v) * w / 3
    o = [f'<svg viewBox="0 0 {Wm} {Wm + 4}" width="{Wm}mm" height="{Wm + 4}mm" xmlns="http://www.w3.org/2000/svg" font-family="system-ui, Segoe UI, Helvetica, Arial, sans-serif">',
         f'<rect x="{m}" y="{m}" width="{w}" height="{w}" fill="#efe9d8" stroke="#6b5f3a" stroke-width="0.6"/>',
         f'<rect x="{m - 2}" y="{m - 2.2}" width="{w + 4}" height="2.2" fill="#c62828"/><text x="{Wm / 2}" y="{m - 3.5}" font-size="3.2" font-weight="700" text-anchor="middle" fill="#c62828">LATURA ROȘIE = SPRE GARDUL DE NORD</text>']
    for u in US: o.append(f'<line x1="{px(u):.1f}" y1="{m}" x2="{px(u):.1f}" y2="{Wm - m}" stroke="#999" stroke-width="0.25" stroke-dasharray="1 1"/><text x="{px(u):.1f}" y="{Wm - m + 4}" font-size="2.8" text-anchor="middle" fill="#444">{str(u).replace(".", ",")} m</text>')
    for v in VS: o.append(f'<line x1="{m}" y1="{py(v):.1f}" x2="{Wm - m}" y2="{py(v):.1f}" stroke="#999" stroke-width="0.25" stroke-dasharray="1 1"/><text x="{m - 1.5}" y="{py(v) + 1:.1f}" font-size="2.8" text-anchor="end" fill="#444">{f"{v:.2f}".replace(".", ",")}</text>')
    for p in RETETE[k]:
        x, y = px(p['u']), py(p['v']); r = 4.2 if p['strat'] == 'A' else 3.4; nume = SP[p['cod']]['ro']
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{COL[p["strat"]]}" stroke="#fff" stroke-width="0.6"/><text x="{x:.1f}" y="{y + 1.4:.1f}" font-size="4" font-weight="700" text-anchor="middle" fill="#fff">{p["poz"]}</text>')
        if k == 'S' and p['cod'] == 'Pn': o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r + 1}" fill="none" stroke="#0b3d91" stroke-width="0.5" stroke-dasharray="1 0.7"/>')
        parts = nume.split(', ')[0].split(' ')
        if len(nume) > 13 and len(parts) > 1:
            o.append(f'<text x="{x:.1f}" y="{y + r + 3.2:.1f}" font-size="2.9" text-anchor="middle" fill="#222">{H.escape(" ".join(parts[:-1]))}</text><text x="{x:.1f}" y="{y + r + 6.2:.1f}" font-size="2.9" text-anchor="middle" fill="#222">{H.escape(parts[-1])}</text>')
        else:
            o.append(f'<text x="{x:.1f}" y="{y + r + 3.2:.1f}" font-size="2.9" text-anchor="middle" fill="#222">{H.escape(nume)}</text>')
    return ''.join(o) + '</svg>'
def rt_full_page(k):
    desc = {'I': f'rețeta de interior — {uses["I"]} pătrate; fiecare specie o dată, mojdreanul de două ori (cuiele 4 și 22)',
            'S': f'rețeta benzii de sud — {uses["S"]} pătrate; aceeași așezare, cu pin negru la cuiele ' + ', '.join(str(p) for p in sorted(TPL) if S_LAY[p] == 'Pn') + ' (cerc albastru) în locul teiului, cerului, ulmului și sorbului'}[k]
    rows = ''.join(f'<tr><td class="n">{p["poz"]}</td><td><span class="sw" style="background:{COL[p["strat"]]}"></span>{H.escape(SP[p["cod"]]["ro"])}</td><td><i>{H.escape(SP[p["cod"]]["lat"])}</i></td><td>{NUME_STRAT[p["strat"]]}</td></tr>' for p in RETETE[k])
    return (f'<section class="pg"><h1>Rețeta {k} <small>— {desc}</small></h1><div class="row">{rt_full_svg(k)}<div class="tbl"><table><thead><tr><th>Cui</th><th>Specie</th><th>Nume latin</th><th>Strat</th></tr></thead><tbody>{rows}</tbody></table>'
            f'<p class="foot">Rama de 3 × 3 m, cuie la 0,3 · 0,9 · 1,5 · 2,1 · 2,7 m (nord/sud) și 0,25 … 2,75 m din 0,5 în 0,5 (est/vest); numerotarea 1–30 de la nord spre sud, de la vest spre est. Regula de sărit: cuiul care cade pe alee, în luminiș sau dincolo de var se sare. Despicătura se închide cu palmele, nu cu piciorul. Pădurea Miyawaki Poienel, Crucea — schema de plantare 4, {len(SQ)} de pătrate.</p></div></div></section>')
html = f'''<!doctype html><html lang="ro"><head><meta charset="utf-8"><title>Rețetele schemei 4 — rama de 3 × 3 m</title>
<style>
@page {{ size: A4 landscape; margin: 9mm; }}
body {{ margin: 0; font-family: system-ui, "Segoe UI", Helvetica, Arial, sans-serif; color: #222; background: #fff; }}
.pg {{ width: 279mm; height: 190mm; page-break-after: always; break-after: page; overflow: hidden; }}
.pg:last-child {{ page-break-after: auto; }}
h1 {{ font-size: 15px; margin: 0 0 3mm; color: #1f4d33; }} h1 small {{ font-weight: 400; color: #444; font-size: 11px; }}
.row {{ display: flex; gap: 6mm; align-items: flex-start; }}
.tbl {{ flex: 1; }} table {{ border-collapse: collapse; font-size: 9.5px; width: 100%; }}
td, th {{ padding: 0.6mm 1.5mm; border-bottom: 0.2mm solid #e3ddcc; text-align: left; }} td.n {{ font-weight: 700; width: 6mm; }}
.sw {{ display: inline-block; width: 3mm; height: 3mm; border-radius: 50%; vertical-align: middle; margin-right: 1.5mm; }}
.foot {{ font-size: 8.5px; color: #444; margin: 3mm 0 0; line-height: 1.35; }}
@media screen {{ body {{ background: #888; }} .pg {{ background: #fff; margin: 6mm auto; padding: 9mm; box-shadow: 0 2px 10px rgba(0,0,0,.4); }} }}
</style></head><body>{rt_full_page('I')}{rt_full_page('S')}</body></html>'''
open(f'{R}/retete-est4.html', 'w', encoding='utf-8').write(html)
print('scris: retete-est4.html')
