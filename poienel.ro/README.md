# poienel.ro

Site-ul static publicat la <https://poienel.ro/>: trei pagini (`index.html` grădina și speciile, `atractii.html` atracțiile turistice din jur, `jurnal.html` jurnalul), cu aceeași bară de meniu și același `resurse/site.css`. Sursele de adevăr sunt `specii.json`, `atractii.json` și `jurnal.json`; din ele, `build.mjs` generează tot ce trebuie să existe în pagini fără JavaScript, ca să fie citit de motoarele de căutare și de agenții AI.

## Cum se actualizează

1. Editează JSON-ul paginii: `specii.json` (o specie; `phenology` are 12 luni, fiecare `[udare, vegetație, înflorire]` cu 0 sau 1), `atractii.json` (un obiectiv) sau `jurnal.json` (o însemnare, cu `data` ISO, `titlu`, `text`, `foto`, `linkuri`; pozele se pregătesc cu `python foto.py <data> <subiect> <poza>`, care face fișierul de 900 px și miniatura de 300 px).
2. Rulează `node build.mjs` din acest folder. Scriptul rescrie regiunile marcate `<!-- BUILD:… -->` din cele trei pagini (meniul, tabelul, fișele, lista de obiective, însemnările, JSON-LD) și regenerează `specii.csv` și `sitemap.xml`.
3. Verifică local (`.claude/http-server.ps1` sau orice server static) și publică cu `sync-to-ftp.ps1` (parola FTP se dă prin variabila de mediu `POIENEL_FTP_PASS` sau la prompt; nu se mai ține în script).

Deciziile luate și regulile pentru actualizările viitoare sunt în `CLAUDE.md`.

Restul paginii (`index.html` în afara regiunilor marcate, `robots.txt`, `llms.txt`) se editează direct.

## Ce există pentru crawlere și agenți AI

- tabelul și fișele celor 65 de specii direct în HTML (`<details>` per specie, cu ancore `#specie-COD`);
- `<title>`, meta description, canonical, Open Graph, favicon, `<h1>`;
- JSON-LD cu `WebSite`, `Place` (Crucea, Constanța), `WebPage`, `Dataset` (JSON + CSV) și `ItemList` cu toate speciile, fiecare cu nume latin și link Wikipedia;
- `robots.txt` (permite toate crawlerele, inclusiv cele AI, și indică sitemap-ul), `sitemap.xml`, `llms.txt`;
- `specii.json` și `specii.csv` ca date deschise, anunțate și prin `<link rel="alternate">`;
- linkuri către planurile de pe GitHub Pages și către repo.
