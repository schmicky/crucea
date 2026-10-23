# -*- coding: utf-8 -*-
"""Aduce fotografiile unui studiu de caz în proiect: poze/thumb/pNN.webp (latura lungă 480 px)
și poze/mare/pNN.webp (latura lungă 1400 px), numerotate în ordinea dată.

    python3 poze.py <director-studiu> <poza1> <poza2> ...     # ordinea argumentelor = p01, p02, ...
    python3 poze.py <director-studiu> --dir <director-cu-poze> # ordinea = numele fișierelor, sortate

Rotește după EXIF, nu păstrează originalele (3000×4000 ar fi prea mari pentru GitHub Pages).
Scrie poze/origine.txt cu corespondența pNN → fișierul de origine, ca să se poată reface numerotarea.
"""
import os, sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit(__doc__)
D = os.path.abspath(sys.argv[1])
if sys.argv[2] == '--dir':
    src = sorted(os.path.join(sys.argv[3], f) for f in os.listdir(sys.argv[3])
                 if f.lower().rsplit('.', 1)[-1] in ('jpg', 'jpeg', 'png', 'webp', 'heic'))
else:
    src = sys.argv[2:]
assert src, 'nicio poză'
for sub in ('thumb', 'mare'):
    os.makedirs(os.path.join(D, 'poze', sub), exist_ok=True)
lines = []
for i, f in enumerate(src, 1):
    im = ImageOps.exif_transpose(Image.open(f)).convert('RGB')
    nr = f'p{i:02d}'
    for sub, side, q in (('thumb', 480, 80), ('mare', 1400, 82)):
        c = im.copy(); c.thumbnail((side, side), Image.LANCZOS)
        c.save(os.path.join(D, 'poze', sub, nr + '.webp'), 'WEBP', quality=q, method=6)
    lines.append(f'{nr}\t{os.path.basename(f)}\t{im.size[0]}×{im.size[1]}')
    print(nr, os.path.basename(f), im.size)
open(os.path.join(D, 'poze', 'origine.txt'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print(f'{len(src)} poze → {D}/poze/thumb și /mare')
