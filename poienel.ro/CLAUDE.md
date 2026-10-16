# poienel.ro — reguli pentru actualizări

Acest folder este site-ul static publicat la https://poienel.ro/ (hosting cu FTP, `public_html`). Nu are legătură cu GitHub Pages: acolo se publică restul repo-ului (`schmicky.github.io/crucea`), iar acest folder ajunge pe server doar prin `sync-to-ftp.ps1`.

## Principiul de bază

Tot ce trebuie să citească un motor de căutare sau un agent AI există **în HTML, fără JavaScript**. JavaScript-ul doar filtrează rânduri deja existente și deschide popup-ul. Nu reintroduce conținut generat exclusiv în browser (`innerHTML` din date JS, `fetch` la încărcare etc.). Testul: pagina deschisă cu JS dezactivat trebuie să arate titlul, h1, tabelul complet și toate fișele.

## Sursa de adevăr și fluxul de lucru

- **`specii.json`** este singura sursă pentru specii. Nu edita manual tabelul, fișele, taburile, JSON-LD sau `<script id="specii-data">` din `index.html`: sunt regenerate și orice modificare de mână se pierde.
- După orice schimbare în `specii.json`: `node build.mjs` (din acest folder, Node ≥ 18, fără dependențe). Scriptul rescrie regiunile dintre `<!-- BUILD:nume -->` și `<!-- /BUILD:nume -->` din `index.html` și regenerează `specii.csv` și `sitemap.xml` (cu `lastmod` = data rulării).
- Regiunile generate: `jsonld` (în head), `sumar`, `tabs`, `tabel`, `fise`, `date`. Dacă adaugi o regiune nouă, pune marcajele în `index.html` și intrarea în obiectul `regiuni` din `build.mjs`; scriptul se oprește cu eroare dacă un marcaj lipsește.
- Restul (`index.html` în afara regiunilor, CSS, JS, `robots.txt`, `llms.txt`) se editează direct. Când se schimbă numărul de specii sau descrierea proiectului, actualizează și meta description, Open Graph, textul din `.description` și `llms.txt`: acestea nu sunt generate.

## Structura unei specii în `specii.json`

```json
{ "cod": "A5", "ro": "Paltin de câmp", "lat": "Acer platanoides", "type": "arbore",
  "h2": "3,0–3,5 m", "h5": "5,0–6,0 m", "hm": "20–25 m",
  "lumina": "mixt", "lumin_note": "opțional",
  "water_l": 25, "water_f": 2,
  "phenology": [[0,0,0], … 12 luni … ] }
```

- `cod`: prefixele au sens și sunt folosite în `llms.txt`: `A` arbori, `F` fructiferi, `S` arbuști, `ar` aromatice, `ia`/`ip` ierbacee. Codurile sunt ancorele `#specie-COD` și `@id`-urile din JSON-LD; nu le schimba fără motiv, sunt linkuri publice.
- `type`: numai `arbore`, `fructifer`, `arbust`, `aromat`, `ierbacee` (cheile obiectului `TYPE` din `build.mjs` și ale `typeInfo` din JS; o valoare nouă trebuie adăugată în ambele, plus clasa CSS `.tag-<type>`).
- `lumina`: `soare`, `mixt`, `umbra`.
- `phenology`: 12 luni (ianuarie → decembrie), fiecare `[udare, vegetație, înflorire]` cu 0 sau 1. Ordinea e cea citită de JS (`[water, veg, flower]`) și de `build.mjs`; nu există câmp pentru fructificare. Build-ul transformă vectorii în intervale de luni („Apr–Iul, Sep”, „tot anul”).
- Înălțimile sunt text liber cu virgulă zecimală și „m” (așa apar pe pagină și în CSV).
- `water_l` în litri la o udare, `water_f` udări pe săptămână vara (anii 1–2).

## Decizii luate și de ce

- **Tabel static + popup JS, nu doar popup.** Crawlerele AI (GPTBot, ClaudeBot, PerplexityBot) nu execută JS; tabelul gol din varianta veche însemna o pagină fără conținut pentru ele.
- **Fișe `<details>/<summary>`, nu conținut ascuns cu CSS.** Conținutul pliat e indexat și vizibil utilizatorului la clic; ascunderea cu `display:none` a conținutului destinat doar crawlerelor e cloaking.
- **Taburile de filtrare au `hidden` în HTML și sunt afișate de JS**, pentru că fără JS nu ar face nimic. Regula globală `[hidden] { display: none !important; }` e necesară: `display: flex` din `.type-tabs` ar bate atributul.
- **Numele latin e în tabel și în fișe**, nu doar în popup: e cheia de dezambiguizare pentru agenți și motoare.
- **JSON-LD în `@graph`:** `WebSite`, `Place` (Crucea, Constanța, RO), `WebPage`, `Dataset` cu `DataDownload` spre JSON și CSV, `ItemList` cu toate speciile (`Thing` + `additionalType: Taxon`, `alternateName` = numele latin, `sameAs` = Wikipedia). Compact (fără indentare) ca să țină pagina mică.
- **Linkurile Wikipedia** se construiesc în `build.mjs` din numele latin (`wiki()`), tăind `var.`, parantezele și numele de soi în ghilimele simple. Pozele din popup vin tot de la API-ul Wikipedia (en), la clic; nu se preîncarcă.
- **`robots.txt` permite explicit crawlerele AI.** Decizia e că tot conținutul e public și vrem să fie citat. Dacă se schimbă, se editează acolo; nu adăuga `noindex`/`X-Robots-Tag` din alt loc.
- **`llms.txt`** urmează formatul standard (H1, blockquote, secțiuni cu linkuri, `## Optional` la final). Linkurile duc spre GitHub Pages și repo, unde e documentația detaliată; pagina asta e doar intrarea.
- **Date deschise** `specii.json` și `specii.csv` sunt anunțate în trei locuri: `<link rel="alternate">`, `Dataset` în JSON-LD, footer și `llms.txt`. CSV-ul are BOM UTF-8 ca să se deschidă corect în Excel; coloanele cu luni sunt scrise în clar, nu ca vectori.
- **O singură pagină, un singur URL canonic** `https://poienel.ro/` (fără www). Dacă apar pagini noi, adaugă-le în `sitemap.xml` (în `build.mjs`) și în `llms.txt`.

## Publicare și securitate

- `sync-to-ftp.ps1` urcă tot folderul în `public_html`, mai puțin fișierele din `$ExcludeNames` (`sync-to-ftp.ps1`, `build.mjs`, `README.md`, `CLAUDE.md`). Orice fișier de lucru nou se adaugă acolo.
- **Parola FTP nu se scrie niciodată în repo.** Scriptul o ia din `$env:POIENEL_FTP_PASS` sau o cere la rulare. Repo-ul e public și tot conținutul lui ajunge pe GitHub Pages; workflow-ul `.github/workflows/static.yml` șterge `poienel.ro/sync-to-ftp.ps1` din artefact înainte de publicare. Parola veche din istoricul git a fost compromisă și trebuie considerată schimbată.
- Server local pentru verificare: `.claude/http-server.ps1` (Windows) sau `python3 -m http.server` din acest folder.

## Verificare înainte de publicare

1. `node build.mjs` rulează fără eroare și raportează 65 de specii (sau noul număr) cu totalurile pe tip.
2. În browser, cu JS dezactivat: tabelul și fișele complete, taburile ascunse. Cu JS: taburile filtrează, clic pe rând deschide popup-ul, Escape îl închide, fără erori în consolă.
3. JSON-LD valid (de exemplu validator.schema.org sau `JSON.parse` pe conținutul scriptului).
4. După upload: `https://poienel.ro/robots.txt`, `/sitemap.xml`, `/llms.txt`, `/specii.json` răspund 200 cu tipul corect; HTML-ul vine cu `charset=utf-8`.
