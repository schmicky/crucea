# -*- coding: utf-8 -*-
"""Construiește index.html al unui studiu de caz de vegetație din date.py + assets/template.html.

    python3 build.py <director-studiu>        # ex. studiu-caz-tabacarie

<director-studiu>/date.py trebuie să definească META, TAXONI și PROBLEME (vezi references/schema.md).
Scrie <director-studiu>/index.html și afișează un rezumat. Nu atinge pozele.
"""
import importlib.util, json, os, re, sys

if len(sys.argv) != 2:
    sys.exit(__doc__)
D = os.path.abspath(sys.argv[1])
HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, '..', 'assets', 'template.html')

spec = importlib.util.spec_from_file_location('date', os.path.join(D, 'date.py'))
date = importlib.util.module_from_spec(spec); spec.loader.exec_module(date)
META, TAXONI, PROBLEME = date.META, date.TAXONI, date.PROBLEME

# ── verificări: aici cad greșelile ieftine, înainte să ajungă în pagină ──
TIP = {'arbore', 'arbust', 'conifer', 'spontan'}; LUM = {'soare', 'mixt', 'umbra'}
VERD = {'retine', 'neutru', 'evita'}
STARI = {'repaus', 'persistent', 'vegetatie', 'inflorire', 'fructificare'}
ids = [x['id'] for x in TAXONI]; assert len(ids) == len(set(ids)), 'id duplicat'
poze_dir = os.path.join(D, 'poze', 'thumb')
for x in TAXONI:
    for k in ('id', 'lat', 'ro', 'tip', 'en', 'poze', 'nota', 'lum', 'luni', 'verdict', 'crucea'):
        assert k in x and x[k] not in (None, '', []), f"{x.get('id')}: lipsește {k}"
    assert x['tip'] in TIP and x['lum'] in LUM and x['verdict'] in VERD, x['id']
    assert len(x['luni']) == 12 and set(x['luni']) <= STARI, f"{x['id']}: luni"
    if x['tip'] != 'spontan':
        for k in ('h2', 'h5', 'hm'): assert x.get(k), f"{x['id']}: lipsește {k}"
        assert x.get('apa') and {'l', 'f'} <= set(x['apa']), f"{x['id']}: apa=dict(l=litri, f=udări/săpt.)"
    else:
        x.setdefault('apa', None)
    for p in x['poze']:
        assert re.fullmatch(r'p\d\d', p), f"{x['id']}: poza {p} (format pNN)"
        assert os.path.exists(os.path.join(poze_dir, p + '.webp')), f"{x['id']}: lipsește poze/thumb/{p}.webp"
for p in PROBLEME:
    for k in ('titlu', 'unde', 'poza', 'text'): assert p.get(k), f"problemă fără {k}: {p}"
    assert os.path.exists(os.path.join(poze_dir, p['poza'] + '.webp')), f"problemă: lipsește poza {p['poza']}"
for k in ('titlu', 'eyebrow', 'h1', 'lead', 'concluzii_titlu', 'concluzii', 'nr_poze', 'footer', 'cache'):
    assert META.get(k), f'META: lipsește {k}'

n = lambda t: sum(1 for x in TAXONI if x['tip'] == t)
tax = [{k: v for k, v in x.items() if not (v is None and k != 'apa')} for x in TAXONI]
header = ['<header>', f'  <div class="eyebrow">{META["eyebrow"]}</div>', f'  <h1>{META["h1"]}</h1>']
header += [f'  <p class="lead">{p}</p>' for p in META['lead']]
header += ['  <div class="stats">']
for v, et in ((len(TAXONI), 'taxoni'), (n('arbore'), 'arbori'), (n('arbust'), 'arbuști'),
              (n('conifer'), 'conifere'), (META['nr_poze'], 'fotografii'), (len(PROBLEME), 'probleme')):
    header.append(f'    <div class="stat"><b>{v}</b><span>{et}</span></div>')
header += ['  </div>', '</header>']
concl = [f'<h2>{META["concluzii_titlu"]}</h2>', '<ul class="takeaways">'] + [f'  <li>{c}</li>' for c in META['concluzii']] + ['</ul>']
footer = ['<footer>', f'  {META["footer"]}', '</footer>']

out = open(TPL, encoding='utf-8').read()
rep = [('<!--TITLU-->', META['titlu']), ('<!--HEADER-->', '\n'.join(header)), ('<!--CONCLUZII-->', '\n'.join(concl)),
       ('/*TAXONI*/[]', json.dumps(tax, ensure_ascii=False, indent=1)),
       ('/*PROBLEME*/[]', json.dumps(PROBLEME, ensure_ascii=False, indent=1)),
       ('/*CACHE*/', META['cache']), ('<!--FOOTER-->', '\n'.join(footer))]
for a, b in rep:
    assert out.count(a) == 1, a
    out = out.replace(a, b)
open(os.path.join(D, 'index.html'), 'w', encoding='utf-8').write(out)
print(f"{os.path.join(D, 'index.html')}: {len(TAXONI)} taxoni ({', '.join(f'{t} {n(t)}' for t in ('arbore','arbust','conifer','spontan'))}), "
      f"{len(PROBLEME)} probleme, în plan {sum(1 for x in TAXONI if x.get('inPlan'))}, incerte {sum(1 for x in TAXONI if x.get('incert'))}, "
      f"verdict: " + ', '.join(f"{v} {sum(1 for x in TAXONI if x['verdict']==v)}" for v in ('retine','neutru','evita')))
