# poienel.ro

Site-ul static publicat la <https://poienel.ro/>. Sursa de adevăr pentru specii este `specii.json`; din el, `build.mjs` generează tot ce trebuie să existe în pagină fără JavaScript, ca să fie citit de motoarele de căutare și de agenții AI.

## Cum se actualizează

1. Editează `specii.json` (adaugă, scoate sau corectează o specie). Câmpul `phenology` are 12 luni, fiecare `[udare, vegetație, înflorire]` cu 0 sau 1.
2. Rulează `node build.mjs` din acest folder. Scriptul rescrie regiunile marcate `<!-- BUILD:… -->` din `index.html` (tabelul, fișele, taburile, sumarul, datele inline pentru popup și JSON-LD) și regenerează `specii.csv` și `sitemap.xml`.
3. Verifică local (`.claude/http-server.ps1` sau orice server static) și publică cu `sync-to-ftp.ps1` (parola FTP se dă prin variabila de mediu `POIENEL_FTP_PASS` sau la prompt; nu se mai ține în script).

Restul paginii (`index.html` în afara regiunilor marcate, `robots.txt`, `llms.txt`) se editează direct.

## Ce există pentru crawlere și agenți AI

- tabelul și fișele celor 65 de specii direct în HTML (`<details>` per specie, cu ancore `#specie-COD`);
- `<title>`, meta description, canonical, Open Graph, favicon, `<h1>`;
- JSON-LD cu `WebSite`, `Place` (Crucea, Constanța), `WebPage`, `Dataset` (JSON + CSV) și `ItemList` cu toate speciile, fiecare cu nume latin și link Wikipedia;
- `robots.txt` (permite toate crawlerele, inclusiv cele AI, și indică sitemap-ul), `sitemap.xml`, `llms.txt`;
- `specii.json` și `specii.csv` ca date deschise, anunțate și prin `<link rel="alternate">`;
- linkuri către planurile de pe GitHub Pages și către repo.
