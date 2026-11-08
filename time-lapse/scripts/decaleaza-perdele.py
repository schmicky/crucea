# -*- coding: utf-8 -*-
"""Decalează rândul din mijloc al perdelelor de est și de sud (frasin A24, dud alb F9, corn F21) cu jumătate de pas
de-a lungul gardului, ca rândurile să fie în șah (chincons), nu în fază. Sălcioara de pe hotar, pinii și perdeaua de nord
rămân pe loc. Rescrie pozitie-nord-miyawaki.json și copia înglobată din plan-amenajare-nord-miyawaki.html.

    python3 time-lapse/scripts/decaleaza-perdele.py [--pas 1.5]
"""
import json, math, re, sys, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAS = float(sys.argv[sys.argv.index('--pas') + 1]) if '--pas' in sys.argv else 1.5
CAL = json.load(open(f'{R}/masuratori-nord.json', encoding='utf-8'))['calibrare']
kx = CAL['m_per_procent_latime'] * CAL['factor_manual']; ky = CAL['m_per_procent_inaltime'] * CAL['factor_manual']
th = math.radians(59.6); ex, ey = math.sin(th), math.cos(th); nx, ny = -ey, ex      # axa lungă a lotului (ENE) și normala (NNV)
def uv(p): X, Y = p['x_pct'] * kx, -p['y_pct'] * ky; return X * ex + Y * ey, X * nx + Y * ny
def pct(u, v): X, Y = u * ex + v * nx, u * ey + v * ny; return round(X / kx, 3), round(-Y / ky, 3)
P = json.load(open(f'{R}/pozitie-nord-miyawaki.json', encoding='utf-8'))
U = [uv(p) for p in P]; umax = max(u for u, v in U); vmin = min(v for u, v in U)
MIJLOC = {'A24', 'F9', 'F21'}
def dmin(i, u, v): return min(math.hypot(u - U[j][0], v - U[j][1]) for j in range(len(P)) if j != i)
mutate = []
for i, p in enumerate(P):
    if p['code'] not in MIJLOC: continue
    u, v = U[i]
    if umax - u <= 13 and v > vmin + 13: axa = 'est'        # perdeaua de est: se mută de-a lungul gardului de est (direcția v)
    elif v - vmin <= 8: axa = 'sud'                          # perdeaua de sud: de-a lungul gardului de sud (direcția u)
    else: continue
    for semn in (1, -1):
        nu, nv = (u, v + semn * PAS) if axa == 'est' else (u + semn * PAS, v)
        if dmin(i, nu, nv) >= 1.0: break
    else:
        print('nu încape:', p['code'], round(u, 1), round(v, 1)); continue
    p['x_pct'], p['y_pct'] = pct(nu, nv); U[i] = (nu, nv); mutate.append((p['code'], axa, semn))
import collections
print(f'mutate {len(mutate)} de puncte cu {PAS} m:', dict(collections.Counter((c, a) for c, a, s in mutate)))
json.dump(P, open(f'{R}/pozitie-nord-miyawaki.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
h = open(f'{R}/plan-amenajare-nord-miyawaki.html', encoding='utf-8').read()
new = '[' + ',\n  '.join(json.dumps(p, ensure_ascii=False) for p in P) + ']'
h2, n = re.subn(r'(<script type="application/json" id="pozitie-embedded">\n)\[.*?\]', lambda m: m.group(1) + new, h, count=1, flags=re.S)
assert n == 1
open(f'{R}/plan-amenajare-nord-miyawaki.html', 'w', encoding='utf-8').write(h2)
print('scris pozitie-nord-miyawaki.json și copia din pagină')
