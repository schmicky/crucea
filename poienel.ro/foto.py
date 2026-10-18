#!/usr/bin/env python3
"""Pregătește fotografiile site-ului: orientare corectă (EXIF), lățime maximă 900 px,
miniatură pătrată de 300 × 300 px (decupată din centru) în subfolderul thumb/, nume după convenție.

Folosire (din folderul poienel.ro, cu Pillow instalat: pip install pillow):
  jurnal:   python foto.py 2026-10-17 trasare-ruleta "C:\\Poze\\IMG_1234.jpg"
            -> resurse/jurnal/2026-10-17-trasare-ruleta.jpg + resurse/jurnal/thumb/…
  atracții: python foto.py --atractii dealul-allah-bair "C:\\Poze\\deditei.jpg"
            -> resurse/atractii/dealul-allah-bair.jpg + resurse/atractii/thumb/…  (id-ul din atractii.json)
  fără argumente: regenerează doar miniaturile pentru toate pozele din resurse/jurnal/ și resurse/atractii/.
Apoi pune poza în JSON-ul paginii ("foto": {"src": "resurse/…/….jpg", "alt": "…"}) și rulează node build.mjs.
"""
import sys
from pathlib import Path
from PIL import Image, ImageOps

RESURSE = Path(__file__).resolve().parent / 'resurse'
LATIME_MARE, MINIATURA, CALITATE = 900, 300, 82


def mare(sursa, destinatie):
    im = ImageOps.exif_transpose(Image.open(sursa)).convert('RGB')
    w, h = im.size
    if w > LATIME_MARE:
        im = im.resize((LATIME_MARE, round(h * LATIME_MARE / w)), Image.LANCZOS)
    im.save(destinatie, 'JPEG', quality=CALITATE, optimize=True, progressive=True)
    print(f'{destinatie.relative_to(RESURSE.parent)} {im.size[0]}x{im.size[1]}')


def miniatura(cale_mare):
    """Pătrat de MINIATURA px, decupat din centru, ca toate miniaturile să aibă aceeași mărime."""
    thumb = cale_mare.parent / 'thumb'
    thumb.mkdir(exist_ok=True)
    im = ImageOps.exif_transpose(Image.open(cale_mare)).convert('RGB')
    im = ImageOps.fit(im, (MINIATURA, MINIATURA), Image.LANCZOS, centering=(0.5, 0.5))
    im.save(thumb / cale_mare.name, 'JPEG', quality=CALITATE, optimize=True, progressive=True)
    print(f'  thumb/{cale_mare.name} {im.size[0]}x{im.size[1]}')


def main(argv):
    if argv and argv[0] == '--atractii' and len(argv) == 3:
        folder, nume, sursa = RESURSE / 'atractii', f'{argv[1]}.jpg', Path(argv[2])
    elif len(argv) == 3:
        folder, nume, sursa = RESURSE / 'jurnal', f'{argv[0]}-{argv[1]}.jpg', Path(argv[2])
    elif not argv:
        for folder in (RESURSE / 'jurnal', RESURSE / 'atractii'):
            for f in sorted(folder.glob('*.jpg')):
                miniatura(f)
        return
    else:
        sys.exit(__doc__)
    folder.mkdir(exist_ok=True)
    mare(sursa, folder / nume)
    miniatura(folder / nume)
    print(f'În JSON: {{"src": "resurse/{folder.name}/{nume}", "alt": "..."}}')


if __name__ == '__main__':
    main(sys.argv[1:])
