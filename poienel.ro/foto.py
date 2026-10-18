#!/usr/bin/env python3
"""Pregătește fotografiile pentru jurnal: orientare corectă (EXIF), lățime maximă 900 px,
miniatură pătrată de 300 × 300 px (decupată din centru) în resurse/jurnal/thumb/, nume după dată și subiect.

Folosire (din folderul poienel.ro, cu Pillow instalat: pip install pillow):
  python foto.py 2026-10-17 trasare-ruleta "C:\\Poze\\IMG_1234.jpg"
  python foto.py 2026-10-17 echipa poza.jpeg --nume-ca-atare   # păstrează numele existent
Fără argumente, regenerează doar miniaturile pentru toate pozele din resurse/jurnal/.
Apoi pune poza în jurnal.json la "foto" ({"src": "resurse/jurnal/2026-10-17-trasare-ruleta.jpg", "alt": "..."})
și rulează node build.mjs.
"""
import sys, os
from pathlib import Path
from PIL import Image, ImageOps

DIR = Path(__file__).resolve().parent / 'resurse' / 'jurnal'
THUMB = DIR / 'thumb'
LATIME_MARE, MINIATURA, CALITATE = 900, 300, 82


def salveaza(im, cale, latime):
    im = im.convert('RGB')
    w, h = im.size
    if w > latime:
        im = im.resize((latime, round(h * latime / w)), Image.LANCZOS)
    im.save(cale, 'JPEG', quality=CALITATE, optimize=True, progressive=True)
    return im.size


def miniatura(cale_mare):
    """Pătrat de MINIATURA px, decupat din centru, ca toate miniaturile să aibă aceeași mărime."""
    THUMB.mkdir(exist_ok=True)
    im = ImageOps.exif_transpose(Image.open(cale_mare)).convert('RGB')
    im = ImageOps.fit(im, (MINIATURA, MINIATURA), Image.LANCZOS, centering=(0.5, 0.5))
    im.save(THUMB / cale_mare.name, 'JPEG', quality=CALITATE, optimize=True, progressive=True)
    print(f'  thumb/{cale_mare.name} {im.size[0]}x{im.size[1]}')


def main(argv):
    if len(argv) >= 3:
        data, subiect, sursa = argv[0], argv[1], Path(argv[2])
        nume = f'{data}-{subiect}.jpg'
        im = ImageOps.exif_transpose(Image.open(sursa))
        dim = salveaza(im, DIR / nume, LATIME_MARE)
        print(f'{nume} {dim[0]}x{dim[1]}')
        miniatura(DIR / nume)
        print(f'În jurnal.json: {{"src": "resurse/jurnal/{nume}", "alt": "..."}}')
    else:
        for f in sorted(DIR.glob('*.jpg')):
            miniatura(f)


if __name__ == '__main__':
    main(sys.argv[1:])
