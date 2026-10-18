# poienel.ro — reguli pentru site și pentru orice pagină nouă

Acest folder este site-ul static publicat la https://poienel.ro/ (hosting cu FTP, `public_html`). Ajunge pe server doar prin `sync-to-ftp.ps1`; nu are legătură cu GitHub Pages, unde se publică restul repo-ului (`schmicky.github.io/crucea`). Site-ul este în limba română și este un punct de intrare: documentația detaliată rămâne pe GitHub Pages și în repo, iar paginile de aici trimit spre ea.

Regulile de mai jos se aplică fiecărei pagini, existente sau viitoare. Pagina speciilor (`index.html`) este primul exemplu, nu un caz special.

## 1. Principiul de bază: conținutul există fără JavaScript

Tot ce trebuie să citească un om, un motor de căutare sau un agent AI stă **în HTML-ul servit**. JavaScript-ul poate doar să îmbogățească: filtrare, sortare, popup, hartă, grafice peste date care sunt deja în pagină.

- Nu construi conținut în browser (`innerHTML` din date JS, `fetch` la încărcare, framework-uri care randează clientul). Crawlerele AI (GPTBot, ClaudeBot, PerplexityBot) nu execută JS, iar Googlebot o face cu întârziere.
- Conținutul care are sens doar cu JS (taburi de filtrare, butoane) primește atributul `hidden` în HTML și este afișat de JS. Regula globală `[hidden] { display: none !important; }` trebuie să existe în fiecare pagină, altfel un `display: flex` o anulează.
- Conținut pliat, nu ascuns: ce e secundar se pune în `<details>/<summary>`, care e indexat și accesibil. Ascunderea prin CSS a conținutului destinat crawlerelor e cloaking și nu se face.
- Testul de acceptare al oricărei pagini: deschisă cu JS dezactivat, arată titlul, `<h1>`, tot textul, toate tabelele și toate fișele. Cu JS, totul funcționează și consola nu are erori.

## 2. Ce are fiecare pagină în `<head>`

- `<html lang="ro">`, `<meta charset="UTF-8">`, viewport.
- `<title>` propriu, descriptiv, cu numele site-ului și locul („… — Poienel, Crucea, Constanța”).
- `<meta name="description">` de 1–2 fraze, scrisă pentru pagina respectivă, cu cifrele care contează.
- `<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">`.
- `<link rel="canonical">` cu URL-ul absolut, pe `https://poienel.ro/`, fără `www`, fără `index.html`.
- Favicon (`resurse/favicon-64.png` și `resurse/poienel-semn.svg`).
- Open Graph: `og:type`, `og:site_name` = Poienel, `og:locale` = ro_RO, `og:url`, `og:title`, `og:description`, `og:image` (absolut; implicit `resurse/poienel-logo.png`), plus `twitter:card`.
- Dacă pagina expune date descărcabile: `<link rel="alternate" type="…" href="…">` pentru fiecare format.
- Un bloc JSON-LD (vezi §4).

## 3. Structura corpului paginii

- Un singur `<h1>`, cu subiectul paginii și locul. Logo-ul este o imagine cu `alt`, nu înlocuiește `<h1>`.
- Ierarhie de titluri fără salturi (`h2` sub `h1`, `h3` sub `h2`), secțiuni în `<section>`, navigare în `<nav>`, conținut în `<main>`, subsol în `<footer>`.
- Primul paragraf spune ce este pagina, în 1–3 fraze, cu cifrele cheie (specii, suprafețe, număr de puieți). Este ce preiau agenții ca rezumat.
- Date tabelare în `<table>` cu `<thead>`; fiecare rând al unui obiect (specie, plantă, zonă) are `data-*` cu codul și categoria și o ancoră (`id="…"`) la care se poate lega.
- Numele științifice, codurile și unitățile apar în text, nu doar în popup sau în atribute. Numele latin este cheia de dezambiguizare pentru agenți.
- Imagini cu `alt` descriptiv și `width`/`height`. Fără imagini încărcate la vedere din API-uri externe; fotografiile la cerere (clic) sunt acceptabile.
- Fiecare pagină are o secțiune sau un `<nav>` cu linkuri către celelalte pagini ale site-ului, către pagina relevantă de pe GitHub Pages și către repo. Subsolul listează fișierele de date deschise și `llms.txt`.
- Toate linkurile interne sunt relative la rădăcină (`specii.json`, `plan.html`), cele externe absolute, cu `rel="noopener"` când au `target="_blank"`.
- Coduri și identificatori odată publicați nu se schimbă: sunt ancore, `@id`-uri în JSON-LD și linkuri pe care le pot ține alții.

## 4. Date structurate (JSON-LD)

Fiecare pagină are un `<script type="application/ld+json">` cu un `@graph` care conține cel puțin:

- `WebSite` cu `@id: https://poienel.ro/#website` (același pe toate paginile);
- `Place` cu `@id: https://poienel.ro/#loc`, adresa Crucea, Constanța, RO și `sameAs` spre GitHub (același pe toate paginile);
- `WebPage` al paginii, cu `isPartOf` → `#website`, `about` → `#loc`, `inLanguage: ro`, `mainEntity` → entitatea principală a paginii.

Entitatea principală depinde de pagină: `ItemList` pentru liste (specii, zone, plante), `Dataset` cu `DataDownload` pentru orice date publicate ca JSON/CSV, `HowTo` pentru proceduri (plantare, irigare), `Article`/`BlogPosting` pentru jurnal, `ImageGallery` pentru fotografii, `Event` pentru zile de plantare. Elementele de listă au `name` (română), `alternateName` (latin, dacă există), `identifier` (codul), `description` în clar și `sameAs` spre o sursă publică (Wikipedia) când există. JSON-LD se scrie compact, fără indentare, ca să nu umfle pagina. Trebuie să fie `JSON.parse`-abil; build-ul îl generează, nu se scrie de mână.

## 5. Pagini generate din date

Orice pagină care listează obiecte (specii, plante, zone de irigare, lucrări) urmează același model:

- **O sursă de adevăr** într-un fișier JSON din acest folder (`specii.json` pentru specii). Nu se editează manual HTML-ul generat din ea.
- **Regiuni generate** în HTML, delimitate de `<!-- BUILD:nume -->` … `<!-- /BUILD:nume -->`. Tot ce e în afara regiunilor se editează direct; tot ce e înăuntru se pierde la următorul build.
- **`build.mjs`** (Node ≥ 18, fără dependențe) citește JSON-ul, generează regiunile, JSON-LD-ul, datele inline pentru JS (`<script type="application/json" id="…-data">`, cu `<` scăpat), fișierele de date deschise (`.json` și `.csv` cu BOM UTF-8 și valori în clar, nu vectori) și `sitemap.xml`. Se oprește cu eroare dacă lipsește o regiune.
- JS-ul paginii citește datele din scriptul inline, nu dintr-o copie proprie; o singură sursă, trei consumatori (HTML static, JSON-LD, popup).
- O pagină nouă generată adaugă în `build.mjs` propria sursă și propriile regiuni, după modelul speciilor; sitemap-ul preia automat orice `*.html` din folder.
- Fiecare set de date publicat este anunțat în trei locuri: `<link rel="alternate">` în head, `Dataset` în JSON-LD, linkuri în subsol și în `llms.txt`.

Conversii convenționale: valorile pe luni (vectori de 12 × 0/1) se afișează ca intervale de luni („Apr–Iul, Sep”, „tot anul”); înălțimile și cantitățile rămân text cu virgulă zecimală și unitate, așa cum le scrie autorul.

## 6. Fișierele de site

- `robots.txt`: `Allow: /` pentru toți, inclusiv crawlerele AI listate explicit, și linia `Sitemap:`. Decizia este că tot conținutul e public și vrem să fie citat. Dacă o pagină nu trebuie indexată, se spune aici sau cu `<meta name="robots" content="noindex">` în pagina aceea, nu prin header pe server.
- `sitemap.xml`: generat de `build.mjs` din toate paginile HTML și fișierele de date; nu se editează de mână. După orice pagină nouă sau modificată se rulează build-ul, ca să se actualizeze `lastmod`.
- `llms.txt`: formatul standard (H1, blockquote cu rezumatul, secțiuni cu linkuri `- [titlu](url): descriere`, `## Optional` la final). Se actualizează de mână la fiecare pagină nouă sau set de date nou și când se schimbă cifrele din rezumat. Linkurile spre GitHub Pages și repo rămân aici; `llms.txt` e harta pentru agenți.
- URL-uri: fișiere `.html` cu nume mici, fără diacritice, cu cratime (`plan-nord.html`); canonicul rădăcinii este `https://poienel.ro/`. Nu se schimbă numele unei pagini publicate fără redirect 301 pe server.
- CSS-ul este unul singur, `resurse/site.css`, încărcat de toate paginile; nu se pun blocuri `<style>` în pagini. Stilurile specifice unei pagini se adaugă tot acolo, sub un comentariu cu numele paginii.
- **Bara de meniu** este aceeași pe toate paginile și e generată de `build.mjs` (regiunea `BUILD:nav`, lista `MENIU`); pagina curentă primește `aria-current="page"`. O pagină nouă intră în meniu prin `MENIU`, nu prin HTML scris de mână.

## 7. Publicare și securitate

- `sync-to-ftp.ps1` urcă tot folderul în `public_html`, mai puțin `$ExcludeNames` (`sync-to-ftp.ps1`, `build.mjs`, `foto.py`, `README.md`, `CLAUDE.md`). Orice fișier de lucru nou (scripturi, note, surse neprocesate) se adaugă acolo.
- **Nicio parolă, cheie sau token în repo**, nici în acest folder, nici altundeva: repo-ul e public și tot conținutul lui ajunge pe GitHub Pages. Scriptul FTP ia parola din `$env:POIENEL_FTP_PASS` sau o cere la rulare. Workflow-ul `.github/workflows/static.yml` șterge `poienel.ro/sync-to-ftp.ps1` din artefactul Pages; dacă apar alte scripturi de publicare, se adaugă și ele acolo. Parola veche din istoricul git este compromisă și se consideră schimbată.
- Server local pentru verificare: `.claude/http-server.ps1` (Windows) sau `python3 -m http.server` din acest folder.

## 8. Verificare înainte de publicare (orice pagină)

1. `node build.mjs` rulează fără eroare și raportează numerele așteptate.
2. Cu JS dezactivat: titlu, `<h1>`, tot conținutul, tabelele și fișele complete; elementele `hidden` nu se văd.
3. Cu JS: interacțiunile merg, fără erori în consolă (singura excepție acceptată: cereri externe blocate de rețea).
4. JSON-LD valid (`JSON.parse` pe conținut sau validator.schema.org); meta description, canonical și `og:url` corespund paginii.
5. Pagina e în `sitemap.xml` și în `llms.txt`; linkurile interne duc la fișiere care există.
6. După upload: fiecare URL nou răspunde 200 cu tipul corect (`text/html; charset=utf-8`, `application/json`, `text/csv`, `text/plain` pentru `robots.txt` și `llms.txt`); `www` redirecționează spre domeniul fără `www`.

## Anexa: paginile existente

Fiecare pagină are regiunile comune `nav` și `jsonld`, propriul JSON ca sursă și propria secțiune în `build.mjs`.

### `index.html` — speciile grădinii

- Sursa: `specii.json`, 65 de specii. Câmpuri: `cod`, `ro`, `lat`, `type` (`arbore`, `fructifer`, `arbust`, `aromat`, `ierbacee`), `h2`/`h5`/`hm` (înălțimi la 2 ani, 5 ani, maturitate), `lumina` (`soare`, `mixt`, `umbra`), `lumin_note` opțional, `water_l` (litri la udare), `water_f` (udări pe săptămână vara, anii 1–2), `phenology` (12 luni ianuarie → decembrie, fiecare `[udare, vegetație, înflorire]` cu 0/1; nu există fructificare).
- Prefixele codurilor: `A` arbori, `F` fructiferi, `S` arbuști, `ar` aromatice, `ia`/`ip` ierbacee. Ancorele sunt `#specie-COD`.
- Regiuni generate: `jsonld` (head), `sumar`, `tabs`, `tabel`, `fise`, `date`. Un `type` nou se adaugă în `TYPE` din `build.mjs`, în `typeInfo` din JS și ca clasă CSS `.tag-<type>`.
- Linkurile Wikipedia se construiesc din numele latin (`wiki()` în `build.mjs`), tăind `var.`, parantezele și soiul în ghilimele simple; pozele din popup vin de la API-ul Wikipedia (en), la clic.
- Texte neregenerate care conțin cifre: meta description, Open Graph, paragrafele din `.description`, `llms.txt`.

### `atractii.html` — atracțiile turistice din jur

- Sursa: `atractii.json`. Câmpuri: `id` (ancora `#id`, fără diacritice), `nume`, `categorie` (`natura`, `religios`, `istorie`, `cultura`, `peisaj`; cheile `CATEG` din `build.mjs` și clasele CSS `.tag-<categorie>`), `tip_schema` (listă de tipuri schema.org pentru `additionalType`, de exemplu `PlaceOfWorship`, `Park`, `Museum`, `LandmarksOrHistoricalBuildings`), `localitate`, `comuna`, `distanta_km` (pe șosea, de la Poienel, aproximativ, număr întreg), `rezumat` (o frază, intră și în JSON-LD), `descriere` (listă de paragrafe), `practic` (listă de sfaturi de acces și vizitare), `surse` (listă de `{titlu, url}`; devin `sameAs`).
- Lista și articolele sunt sortate după `distanta_km`. Regiuni: `sumar`, `lista`, `atractii`.
- Fiecare obiectiv are cel puțin o sursă verificabilă; faptele (ani, dimensiuni, hramuri) se iau din surse, nu din memorie. Distanțele sunt estimări și se corectează pe măsură ce se verifică pe teren.
- Texte neregenerate cu cifre: meta description, Open Graph, paragraful de introducere, `llms.txt`.

### `jurnal.html` — jurnalul grădinii

- Sursa: `jurnal.json`, listă de însemnări: `id` (opțional; implicit data), `data` (ISO `AAAA-LL-ZZ`), `titlu`, `text` (listă de paragrafe), `foto` (listă de `{src, alt}`; `src` e fișierul mare din `resurse/jurnal/`, nume `AAAA-LL-ZZ-descriere.jpg`, lățime maximă 900 px, cu miniatura pătrată de 300 × 300 px, decupată din centru, cu același nume în `resurse/jurnal/thumb/`; ambele le face `python foto.py <data> <subiect> <poza>` (Pillow), care aplică și orientarea EXIF; `alt` spune ce se vede; originalele nu se păstrează în repo), `linkuri` (listă de `{titlu, url}`; relative pentru paginile site-ului).
- Însemnările se afișează cu cea mai nouă prima; ancora e `#id`. Fotografiile apar ca miniaturi pătrate de 300 × 300 px (aceeași mărime indiferent de orientare) cu link spre fișierul mare; build-ul citește dimensiunile din JPEG și se oprește dacă lipsește miniatura. JSON-LD: `Blog` cu `BlogPosting` pe însemnare, cu `datePublished`, `articleBody` și `ImageObject` (fișier mare + miniatură) pe poză.
- Cât timp `jurnal.json` e gol, build-ul pune `noindex` pe pagină (regiunea `robots`) și o lasă afară din sitemap; la prima însemnare devine indexabilă automat.
- Însemnările sunt fapte din teren, la persoana întâi plural, cu data lucrării; nu se rescriu retroactiv decât pentru greșeli.

