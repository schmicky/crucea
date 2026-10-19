#!/usr/bin/env node
// Generează, din fișierele JSON ale site-ului, paginile în română (ro/) și engleză (en/):
// regiunile <!-- BUILD:nume --> … <!-- /BUILD:nume -->, fișierele de date deschise și sitemap.xml.
// Rulare: node build.mjs (din folderul poienel.ro). Regulile sunt în CLAUDE.md.
// Orice text din JSON care se afișează trebuie să fie {ro, en}; build-ul se oprește dacă lipsește o limbă.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const dir = path.dirname(fileURLToPath(import.meta.url));
const SITE = 'https://poienel.ro/';
const LANGS = ['ro', 'en'];
const PAGINI = ['index.html', 'atractii.html', 'jurnal.html'];

const citeste = (f) => JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
const scrie = (f, s) => fs.writeFileSync(path.join(dir, f), s);
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const jsonInline = (o) => JSON.stringify(o).replace(/</g, '\\u003c');
const jsonld = (o) => `<script type="application/ld+json">\n${jsonInline(o)}\n</script>`;
const urlPagina = (lang, f) => SITE + `${lang}/${f}`;

// Text bilingv: {ro, en} → limba cerută; se oprește dacă lipsește traducerea
function txt(v, lang, ctx) {
  if (v && typeof v === 'object' && !Array.isArray(v)) {
    if (typeof v[lang] !== 'string' && !Array.isArray(v[lang])) throw new Error(`Lipsește traducerea „${lang}” la ${ctx}`);
    return v[lang];
  }
  throw new Error(`Textul de la ${ctx} trebuie să fie {ro, en}, nu „${String(v).slice(0, 40)}”`);
}

// Dimensiunile unui JPEG din antetul SOF, ca să punem width/height pe <img> fără biblioteci
function dimJpeg(fisier) {
  const b = fs.readFileSync(path.join(dir, fisier));
  let i = 2;
  while (i < b.length) {
    if (b[i] !== 0xff) throw new Error(`${fisier}: nu e JPEG valid`);
    const m = b[i + 1];
    if (m >= 0xc0 && m <= 0xcf && m !== 0xc4 && m !== 0xc8 && m !== 0xcc) return { h: b.readUInt16BE(i + 5), w: b.readUInt16BE(i + 7) };
    i += 2 + b.readUInt16BE(i + 2);
  }
  throw new Error(`${fisier}: fără antet SOF`);
}
const thumbDe = (src) => src.replace(/\/([^/]+)$/, '/thumb/$1');
// Figură cu miniatură pătrată și link spre fișierul mare; cu width/height citite din JPEG
function figura(foto, lang, clasa, ctx, L) {
  const thumb = thumbDe(foto.src);
  if (!fs.existsSync(path.join(dir, thumb))) throw new Error(`Lipsește miniatura ${thumb} (rulează python foto.py)`);
  const d = dimJpeg(thumb), D = dimJpeg(foto.src);
  const alt = foto.alt ? txt(foto.alt, lang, `${ctx} foto.alt`) : '';
  const legenda = clasa === 'atractie-foto' ? (foto.credit ? `<figcaption>${L.foto}: ${esc(foto.credit)}</figcaption>` : '') : (alt ? `<figcaption>${esc(alt)}</figcaption>` : '');
  return `<figure class="${clasa}"><a href="../${esc(foto.src)}" title="${L.foto_mare} (${D.w}×${D.h})"><img src="../${esc(thumb)}" alt="${esc(alt)}" width="${d.w}" height="${d.h}" loading="lazy"></a>${legenda}</figure>`;
}

// Înlocuiește regiunile marcate dintr-o pagină; eroare dacă lipsește vreuna
function completeaza(fisier, regiuni) {
  let html = fs.readFileSync(path.join(dir, fisier), 'utf8');
  for (const [nume, continut] of Object.entries(regiuni)) {
    const re = new RegExp(`(<!-- BUILD:${nume} -->)[\\s\\S]*?(<!-- /BUILD:${nume} -->)`);
    if (!re.test(html)) throw new Error(`Lipsește regiunea BUILD:${nume} din ${fisier}`);
    html = html.replace(re, (_, a, b) => `${a}\n${continut}\n${b}`);
  }
  scrie(fisier, html);
}

// ───────────────────────── etichetele pe limbi ─────────────────────────
const ETICHETE = {
  ro: {
    nume: 'Română', luni: ['Ian', 'Feb', 'Mar', 'Apr', 'Mai', 'Iun', 'Iul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    luniLungi: ['ianuarie', 'februarie', 'martie', 'aprilie', 'mai', 'iunie', 'iulie', 'august', 'septembrie', 'octombrie', 'noiembrie', 'decembrie'],
    totAnul: 'tot anul', dataRo: (d, m, y) => `${d} ${m} ${y}`,
    tipuri: { arbore: 'Arbore', fructifer: 'Fructifer', arbust: 'Arbust', aromat: 'Aromatic', ierbacee: 'Ierbacee' },
    plural: { arbore: 'Arbori', fructifer: 'Fructiferi', arbust: 'Arbuști', aromat: 'Aromatice', ierbacee: 'Ierbacee' },
    lumina: { soare: 'soare', mixt: 'soare sau semiumbră', umbra: 'umbră' }, luminaScurt: { soare: 'Soare', mixt: 'Mixt', umbra: 'Umbră' },
    categ: { natura: 'Natură', religios: 'Religios', istorie: 'Istorie', cultura: 'Cultură', peisaj: 'Peisaj' },
    toate: 'Toate', specii: 'de specii', cod: 'Cod', foto: 'Foto', foto_mare: 'Deschide fotografia mare', foto_cautare: 'Se caută fotografia…', foto_lipsa: 'Fotografia nu e disponibilă',
    apa_doza: '{n} l/udare', apa_frecventa: 'De {n} ori/săptămână în vară',
    inaltime: 'Înălțime', la2: 'la 2 ani', la5: 'la 5 ani', laMat: 'la maturitate', luminaT: 'Lumină', apa: 'Apă (anii 1–2)',
    apaText: (l, f) => `${l} l la udare, de ${f} ${f === 1 ? 'dată' : 'ori'} pe săptămână vara`,
    udare: 'Udare', vegetatie: 'Vegetație', inflorire: 'Înflorire', referinta: 'Referință', peWikipedia: 'pe Wikipedia',
    descSpecie: (s, tip, hm, h2, h5, lum, l, f, infl) => `${tip}, ${hm} la maturitate (${h2} la 2 ani, ${h5} la 5 ani); lumină: ${lum}; apă în anii 1–2: ${l} l la udare, de ${f} ori pe săptămână vara; înflorire: ${infl}.`,
    datasetNume: 'Speciile grădinii Poienel', datasetDesc: (n) => `Lista celor ${n} de specii plantate la Poienel, cu cod, nume românesc și latin, tip, înălțime la 2 ani, 5 ani și la maturitate, cerințe de lumină și apă și calendar lunar de udare, vegetație și înflorire.`,
    paginaSpecii: 'Poienel — grădină și pădure Miyawaki în Crucea, Constanța',
    csvHead: ['cod', 'nume', 'nume_latin', 'tip', 'inaltime_2_ani', 'inaltime_5_ani', 'inaltime_matur', 'lumina', 'nota_lumina', 'apa_l_udare', 'udari_pe_saptamana', 'luni_udare', 'luni_vegetatie', 'luni_inflorire', 'wikipedia'],
    sumarSpecii: (n, parti) => `${n} de specii: ${parti.join(', ')}.`,
    obiective: 'obiective', sumarAtr: (n, parti) => `${n} obiective: ${parti.join(', ')}.`, km: 'km', deLaPoienel: 'de Poienel', circa: 'circa', judet: 'județul Constanța', practic: 'Practic', surse: 'Surse',
    atrNume: 'Atracții turistice în jurul Poienelului', atrDesc: 'Obiective naturale, istorice și religioase la cel mult o oră de mers de Crucea, Constanța, în ordinea distanței.', paginaAtr: 'Atracții turistice în jurul Poienelului — Crucea, Constanța',
    taguri: { amenajare: 'Amenajare', relaxare: 'Relaxare', etape: 'Etape' }, filtreaza: 'Filtrează după temă',
    jurnalNume: 'Jurnalul grădinii Poienel', paginaJurnal: 'Jurnalul grădinii — Poienel, Crucea, Constanța', jurnalGol: 'Jurnalul începe în curând: primele însemnări vor fi despre măsurători, comenzile de puieți și plantarea pădurii Miyawaki din toamna lui 2026.',
    meniu: { 'index.html': 'Grădina', 'index.html#specii': 'Specii', 'atractii.html': 'Atracții turistice', 'jurnal.html': 'Jurnal', 'index.html#planuri': 'Planuri' }, meniuAria: 'Meniu principal', limba: 'Limba',
    siteDesc: 'Poienel este o grădină în transformare la Crucea, județul Constanța: 65 de specii de arbori, arbuști, pomi fructiferi, plante aromatice și ierbacee, plus o pădure Miyawaki de 340 m² cu 919 puieți din 30 de specii autohtone de silvostepă dobrogeană.',
    footerDesc: 'Grădină și pădure Miyawaki la Crucea, județul Constanța, în nordul Dobrogei.', footerLinkuri: 'Linkuri recomandate', footerDate: 'Date deschise', footerDateText: 'Conținutul poate fi citit și citat liber, inclusiv de agenți AI; sursa: poienel.ro.',
    footerProiect: 'Proiectul', footerGithub: 'Documentația completă pe GitHub', footerGithubText: 'planuri, comenzi de puieți, oferte, studii de caz.', footerContact: 'Scrie-ne prin', footerJos: 'Crucea, Constanța',
    recomandate: [
      { href: 'https://discoverdobrogea.ro/', text: 'Descoperă Dobrogea', desc: 'locuri, trasee și povești din Dobrogea' },
      { href: 'https://www.turistulliber.ro/', text: 'Turistul Liber', desc: 'blog de călătorii prin România' },
      { href: 'https://epicvistaexperience.com/', text: 'Epic Vista Experience', desc: 'experiențe și călătorii' },
      { href: 'https://schmicky.github.io/crucea/', text: 'Proiectul Poienel pe GitHub Pages', desc: 'planurile, schema Miyawaki, irigarea, studiile de caz' },
    ],
  },
  en: {
    nume: 'English', luni: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    luniLungi: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    totAnul: 'all year', dataRo: (d, m, y) => `${d} ${m} ${y}`,
    tipuri: { arbore: 'Tree', fructifer: 'Fruit', arbust: 'Shrub', aromat: 'Aromatic', ierbacee: 'Herbaceous' },
    plural: { arbore: 'Trees', fructifer: 'Fruit trees & bushes', arbust: 'Shrubs', aromat: 'Aromatics', ierbacee: 'Herbaceous' },
    lumina: { soare: 'sun', mixt: 'sun or part shade', umbra: 'shade' }, luminaScurt: { soare: 'Sun', mixt: 'Mixed', umbra: 'Shade' },
    categ: { natura: 'Nature', religios: 'Religious', istorie: 'History', cultura: 'Culture', peisaj: 'Scenery' },
    toate: 'All', specii: 'species', cod: 'Code', foto: 'Photo', foto_mare: 'Open the full-size photo', foto_cautare: 'Looking for a photo…', foto_lipsa: 'No photo available',
    apa_doza: '{n} l per watering', apa_frecventa: '{n} times a week in summer',
    inaltime: 'Height', la2: 'at 2 years', la5: 'at 5 years', laMat: 'at maturity', luminaT: 'Light', apa: 'Water (years 1–2)',
    apaText: (l, f) => `${l} l per watering, ${f === 1 ? 'once' : f + ' times'} a week in summer`,
    udare: 'Watering', vegetatie: 'Growth', inflorire: 'Flowering', referinta: 'Reference', peWikipedia: 'on Wikipedia',
    descSpecie: (s, tip, hm, h2, h5, lum, l, f, infl) => `${tip}, ${hm} at maturity (${h2} at 2 years, ${h5} at 5 years); light: ${lum}; water in years 1–2: ${l} l per watering, ${f} times a week in summer; flowering: ${infl}.`,
    datasetNume: 'The species of the Poienel garden', datasetDesc: (n) => `The ${n} species planted at Poienel, with code, Romanian, English and Latin name, type, height at 2 years, 5 years and maturity, light and water needs and a monthly calendar of watering, growth and flowering.`,
    paginaSpecii: 'Poienel — garden and Miyawaki forest in Crucea, Constanța, Romania',
    csvHead: ['code', 'name', 'latin_name', 'type', 'height_2_years', 'height_5_years', 'height_mature', 'light', 'light_note', 'water_l_per_watering', 'waterings_per_week', 'watering_months', 'growth_months', 'flowering_months', 'wikipedia'],
    sumarSpecii: (n, parti) => `${n} species: ${parti.join(', ')}.`,
    obiective: 'sights', sumarAtr: (n, parti) => `${n} sights: ${parti.join(', ')}.`, km: 'km', deLaPoienel: 'from Poienel', circa: 'about', judet: 'Constanța County', practic: 'Practical', surse: 'Sources',
    atrNume: 'Sights around Poienel', atrDesc: 'Natural, historical and religious sights within an hour of Crucea, Constanța, in order of distance.', paginaAtr: 'Sights around Poienel — Crucea, Constanța, Romania',
    taguri: { amenajare: 'Landscaping', relaxare: 'Leisure', etape: 'Milestones' }, filtreaza: 'Filter by theme',
    jurnalNume: 'The Poienel garden journal', paginaJurnal: 'Garden journal — Poienel, Crucea, Constanța', jurnalGol: 'The journal starts soon: the first entries will be about measurements, sapling orders and the planting of the Miyawaki forest in autumn 2026.',
    meniu: { 'index.html': 'The garden', 'index.html#specii': 'Species', 'atractii.html': 'Sights', 'jurnal.html': 'Journal', 'index.html#planuri': 'Plans' }, meniuAria: 'Main menu', limba: 'Language',
    siteDesc: 'Poienel is a garden in the making at Crucea, Constanța County, Romania: 65 species of trees, shrubs, fruit trees, aromatic and herbaceous plants, plus a 340 m² Miyawaki forest with 919 saplings of 30 native Dobrogea forest-steppe species.',
    footerDesc: 'Garden and Miyawaki forest at Crucea, Constanța County, in northern Dobrogea, Romania.', footerLinkuri: 'Recommended links', footerDate: 'Open data', footerDateText: 'The content may be read and quoted freely, including by AI agents; source: poienel.ro.',
    footerProiect: 'The project', footerGithub: 'Full documentation on GitHub', footerGithubText: 'plans, sapling orders, quotes, case studies (in Romanian).', footerContact: 'Write to us via', footerJos: 'Crucea, Constanța, Romania',
    recomandate: [
      { href: 'https://discoverdobrogea.ro/', text: 'Discover Dobrogea', desc: 'places, routes and stories from Dobrogea (in Romanian)' },
      { href: 'https://www.turistulliber.ro/', text: 'Turistul Liber', desc: 'a travel blog about Romania (in Romanian)' },
      { href: 'https://epicvistaexperience.com/', text: 'Epic Vista Experience', desc: 'travel experiences' },
      { href: 'https://schmicky.github.io/crucea/', text: 'The Poienel project on GitHub Pages', desc: 'the plans, the Miyawaki layout, irrigation, case studies (in Romanian)' },
    ],
  },
};
const DATE_DESCHISE = ['specii.json', 'specii-ro.csv', 'specii-en.csv', 'atractii.json', 'jurnal.json', 'llms.txt', 'sitemap.xml'];
const extern = (href, text) => `<a href="${esc(href)}" rel="noopener" target="_blank">${esc(text)}</a>`;
const dataLunga = (iso, L) => { const [y, m, d] = iso.split('-').map(Number); return L.dataRo(d, L.luniLungi[m - 1], y); };
// Înălțimile sunt scrise cu virgulă zecimală (română); în engleză devin cu punct
const numar = (s, lang) => (lang === 'en' ? String(s).replace(/(\d),(\d)/g, '$1.$2') : s);

// ───────────────────────── părțile comune: head, meniu, subsol, JSON-LD ─────────────────────────
const alternate = (lang, f) => [
  `<link rel="canonical" href="${urlPagina(lang, f)}">`,
  ...LANGS.map((l) => `<link rel="alternate" hreflang="${l}" href="${urlPagina(l, f)}">`),
  `<link rel="alternate" hreflang="x-default" href="${urlPagina('ro', f)}">`,
  `<meta property="og:url" content="${urlPagina(lang, f)}">`,
].join('\n');

const nav = (lang, f) => {
  const L = ETICHETE[lang];
  return `<nav class="menu" aria-label="${L.meniuAria}">
<ul>
<li><a class="menu-brand" href="index.html"><img src="../resurse/poienel-semn.svg" alt="" width="26" height="26">Poienel</a></li>
${Object.entries(L.meniu).map(([href, text]) => `<li><a href="${href}"${href === f ? ' aria-current="page"' : ''}>${text}</a></li>`).join('\n')}
<li class="menu-limbi" aria-label="${L.limba}">${LANGS.map((l) => `<a href="../${l}/${f}" hreflang="${l}" lang="${l}" title="${ETICHETE[l].nume}"${l === lang ? ' aria-current="true"' : ''}><img src="../resurse/flag-${l}.svg" alt="${ETICHETE[l].nume}" width="24" height="16"></a>`).join('')}</li>
</ul>
</nav>`;
};

const footer = (lang) => {
  const L = ETICHETE[lang];
  return `<footer class="site-footer">
<div class="footer-coloane">
<section>
<h2>Poienel</h2>
<p>${L.footerDesc}</p>
<ul>
${Object.entries(L.meniu).filter(([h]) => !h.includes('#')).map(([h, t]) => `<li><a href="${h}">${t}</a></li>`).join('\n')}
</ul>
</section>
<section>
<h2>${L.footerLinkuri}</h2>
<ul>
${L.recomandate.map((l) => `<li>${extern(l.href, l.text)}${l.desc ? ` — ${esc(l.desc)}` : ''}</li>`).join('\n')}
</ul>
</section>
<section>
<h2>${L.footerDate}</h2>
<p>${DATE_DESCHISE.map((f) => `<a href="../${f}">${f}</a>`).join(' · ')}</p>
<p>${L.footerDateText}</p>
</section>
<section>
<h2>${L.footerProiect}</h2>
<p>${extern('https://github.com/schmicky/crucea', L.footerGithub)}: ${L.footerGithubText}</p>
<p>${L.footerContact} ${extern('https://github.com/schmicky/crucea/issues', 'GitHub Issues')}.</p>
</section>
</div>
<p class="footer-jos">© Poienel ${new Date().getFullYear()} · ${L.footerJos}</p>
</footer>`;
};

// Autorul datelor și al jurnalului: Google cere pentru creator/author un Person sau Organization, nu un Place
const ORG = { '@type': 'Organization', '@id': SITE + '#org', name: 'Poienel', url: SITE, logo: SITE + 'resurse/poienel-logo.png', sameAs: ['https://github.com/schmicky/crucea'] };
const WEBSITE = (lang) => ({ '@type': 'WebSite', '@id': SITE + '#website', url: SITE, name: 'Poienel', inLanguage: LANGS, description: ETICHETE[lang].siteDesc });
const LOC = (lang) => ({
  '@type': 'Place', '@id': SITE + '#loc', name: 'Poienel', url: SITE, image: SITE + 'resurse/poienel-logo.png', description: ETICHETE[lang].siteDesc,
  address: { '@type': 'PostalAddress', addressLocality: 'Crucea', addressRegion: 'Constanța', addressCountry: 'RO' },
  sameAs: ['https://github.com/schmicky/crucea', 'https://schmicky.github.io/crucea/'],
});
const webPage = (lang, f, name, mainEntityId) => ({
  '@type': 'WebPage', '@id': urlPagina(lang, f) + '#webpage', url: urlPagina(lang, f), name, inLanguage: lang,
  isPartOf: { '@id': SITE + '#website' }, about: { '@id': SITE + '#loc' }, mainEntity: { '@id': mainEntityId },
  primaryImageOfPage: SITE + 'resurse/poienel-logo.png',
});

// ───────────────────────── datele ─────────────────────────
const specii = citeste('specii.json');
const atractii = citeste('atractii.json').slice().sort((a, b) => a.distanta_km - b.distanta_km);
const jurnal = citeste('jurnal.json').slice().sort((a, b) => b.data.localeCompare(a.data));
const TIPURI = Object.keys(ETICHETE.ro.tipuri), CATEG = Object.keys(ETICHETE.ro.categ), TAGURI = Object.keys(ETICHETE.ro.taguri);
// Fiecare însemnare are cel puțin un tag din lista cunoscută (regula de etichetare e în CLAUDE.md)
for (const j of jurnal) {
  if (!Array.isArray(j.taguri) || !j.taguri.length) throw new Error(`Însemnarea ${j.data} nu are „taguri”`);
  for (const t of j.taguri) if (!TAGURI.includes(t)) throw new Error(`Însemnarea ${j.data}: tag necunoscut „${t}” (permise: ${TAGURI.join(', ')})`);
}
const countsTag = Object.fromEntries(TAGURI.map((t) => [t, jurnal.filter((j) => j.taguri.includes(t)).length]));
const counts = Object.fromEntries(TIPURI.map((t) => [t, specii.filter((s) => s.type === t).length]));
const countsCat = Object.fromEntries(CATEG.map((c) => [c, atractii.filter((a) => a.categorie === c).length]));

// [[udare, vegetație, înflorire] × 12] → „Apr–Iul, Sep”
function luni(phen, idx, L) {
  const on = phen.map((m) => m[idx] === 1);
  const runs = [];
  for (let i = 0; i < 12; i++) {
    if (!on[i]) continue;
    if (runs.length && runs[runs.length - 1][1] === i - 1) runs[runs.length - 1][1] = i;
    else runs.push([i, i]);
  }
  if (!runs.length) return '—';
  if (runs.length === 1 && runs[0][0] === 0 && runs[0][1] === 11) return L.totAnul;
  return runs.map(([a, b]) => (a === b ? L.luni[a] : `${L.luni[a]}–${L.luni[b]}`)).join(', ');
}
const wiki = (lat) => 'https://en.wikipedia.org/wiki/' + encodeURIComponent(lat.replace(/ × /g, '_×_').replace(/ var\. .*$/, '').replace(/ \(.*\)$/, '').replace(/ '.*'$/, '').replace(/ /g, '_'));
const numeSpecie = (s, lang) => { if (typeof s[lang] !== 'string') throw new Error(`Lipsește numele „${lang}” la specia ${s.cod}`); return s[lang]; };
const notaSpecie = (s, lang) => (s.lumin_note ? txt(s.lumin_note, lang, `specia ${s.cod} lumin_note`) : '');
const idJurnal = (j) => j.id || j.data;

for (const lang of LANGS) {
  const L = ETICHETE[lang];
  const sp = (s) => ({ nume: numeSpecie(s, lang), nota: notaSpecie(s, lang), h2: numar(s.h2, lang), h5: numar(s.h5, lang), hm: numar(s.hm, lang) });

  // ── index.html: speciile ──
  const tabel = specii.map((s) => { const v = sp(s); return `<tr data-cod="${esc(s.cod)}" data-type="${esc(s.type)}">
<td><strong>${esc(s.cod)}</strong></td>
<td><a href="#specie-${esc(s.cod)}">${esc(v.nume)}</a><br><em class="lat">${esc(s.lat)}</em></td>
<td><span class="tag tag-${esc(s.type)}">${L.tipuri[s.type]}</span></td>
<td>${esc(v.hm)}</td>
</tr>`; }).join('\n');

  const fise = specii.map((s) => { const v = sp(s); return `<details class="fisa" id="specie-${esc(s.cod)}">
<summary><strong>${esc(s.cod)}</strong> ${esc(v.nume)} <em class="lat">${esc(s.lat)}</em> <span class="tag tag-${esc(s.type)}">${L.tipuri[s.type]}</span></summary>
<dl>
<dt>${L.inaltime}</dt><dd>${esc(v.h2)} ${L.la2} · ${esc(v.h5)} ${L.la5} · ${esc(v.hm)} ${L.laMat}</dd>
<dt>${L.luminaT}</dt><dd>${esc(L.lumina[s.lumina] || s.lumina)}${v.nota ? ' — ' + esc(v.nota) : ''}</dd>
<dt>${L.apa}</dt><dd>${L.apaText(s.water_l, s.water_f)}</dd>
<dt>${L.udare}</dt><dd>${luni(s.phenology, 0, L)}</dd>
<dt>${L.vegetatie}</dt><dd>${luni(s.phenology, 1, L)}</dd>
<dt>${L.inflorire}</dt><dd>${luni(s.phenology, 2, L)}</dd>
<dt>${L.referinta}</dt><dd><a href="${wiki(s.lat)}" rel="noopener" target="_blank">${esc(s.lat)} ${L.peWikipedia}</a></dd>
</dl>
</details>`; }).join('\n');

  const idSpecii = urlPagina(lang, 'index.html') + '#specii';
  const jsonldSpecii = { '@context': 'https://schema.org', '@graph': [
    WEBSITE(lang), LOC(lang), webPage(lang, 'index.html', L.paginaSpecii, idSpecii),
    {
      '@type': 'Dataset', '@id': SITE + '#dataset', name: L.datasetNume, inLanguage: LANGS, url: urlPagina(lang, 'index.html'),
      description: L.datasetDesc(specii.length), license: 'https://creativecommons.org/licenses/by/4.0/', creator: ORG, publisher: ORG,
      distribution: [
        { '@type': 'DataDownload', encodingFormat: 'application/json', contentUrl: SITE + 'specii.json' },
        { '@type': 'DataDownload', encodingFormat: 'text/csv', contentUrl: SITE + 'specii-ro.csv', inLanguage: 'ro' },
        { '@type': 'DataDownload', encodingFormat: 'text/csv', contentUrl: SITE + 'specii-en.csv', inLanguage: 'en' },
      ],
    },
    {
      '@type': 'ItemList', '@id': idSpecii, name: L.datasetNume, numberOfItems: specii.length, itemListOrder: 'https://schema.org/ItemListUnordered',
      itemListElement: specii.map((s, i) => { const v = sp(s); return { '@type': 'ListItem', position: i + 1, item: {
        '@type': 'Thing', '@id': urlPagina(lang, 'index.html') + '#specie-' + s.cod, url: urlPagina(lang, 'index.html') + '#specie-' + s.cod, name: v.nume, alternateName: s.lat, identifier: s.cod,
        additionalType: 'https://schema.org/Taxon', sameAs: wiki(s.lat),
        description: L.descSpecie(s, L.tipuri[s.type].toLowerCase(), v.hm, v.h2, v.h5, L.lumina[s.lumina] || s.lumina, s.water_l, s.water_f, luni(s.phenology, 2, L)) + (v.nota ? ' ' + v.nota : ''),
      } }; }),
    },
  ] };

  const dateInline = {
    etichete: { luni: L.luni, tipuri: L.tipuri, lumina: L.luminaScurt, cod: L.cod, foto_cautare: L.foto_cautare, foto_lipsa: L.foto_lipsa, apa_doza: L.apa_doza, apa_frecventa: L.apa_frecventa },
    specii: specii.map((s) => { const v = sp(s); return { cod: s.cod, nume: v.nume, lat: s.lat, type: s.type, h2: v.h2, h5: v.h5, hm: v.hm, lumina: s.lumina, lumin_note: v.nota, water_l: s.water_l, water_f: s.water_f, phenology: s.phenology }; }),
  };

  completeaza(`${lang}/index.html`, {
    alternate: alternate(lang, 'index.html'), nav: nav(lang, 'index.html'), footer: footer(lang), jsonld: jsonld(jsonldSpecii),
    sumar: L.sumarSpecii(specii.length, TIPURI.map((t) => `${counts[t]} ${L.plural[t].toLowerCase()}`)),
    tabs: `<div class="type-tab active" data-type="all">${L.toate} (${specii.length})</div>\n` + TIPURI.map((t) => `<div class="type-tab" data-type="${t}">${L.plural[t]} (${counts[t]})</div>`).join('\n'),
    tabel, fise,
    date: `<script type="application/json" id="specii-data">${jsonInline(dateInline)}</script>`,
  });

  const csvCell = (v) => { const s = String(v ?? ''); return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s; };
  scrie(`specii-${lang}.csv`, '﻿' + [L.csvHead.join(',')].concat(specii.map((s) => { const v = sp(s); return [
    s.cod, v.nume, s.lat, L.tipuri[s.type], v.h2, v.h5, v.hm, L.lumina[s.lumina] || s.lumina, v.nota,
    s.water_l, s.water_f, luni(s.phenology, 0, L), luni(s.phenology, 1, L), luni(s.phenology, 2, L), wiki(s.lat),
  ].map(csvCell).join(','); })).join('\n') + '\n');

  // ── atractii.html: obiectivele din zonă ──
  const at = (a) => ({ nume: txt(a.nume, lang, `${a.id} nume`), rezumat: txt(a.rezumat, lang, `${a.id} rezumat`), descriere: txt(a.descriere, lang, `${a.id} descriere`), practic: txt(a.practic, lang, `${a.id} practic`) });
  const urlAtr = (a) => urlPagina(lang, 'atractii.html') + '#' + a.id;
  const listaAtr = `<ul class="atractii-lista">\n${atractii.map((a) => `<li><a href="#${esc(a.id)}">${a.foto ? `<img src="../${esc(thumbDe(a.foto.src))}" alt="" width="56" height="56" loading="lazy">` : '<span class="fara-foto"></span>'}<span><span class="nume">${esc(at(a).nume)}</span><span class="cat">${L.categ[a.categorie]} · ${esc(a.localitate)} · ~${a.distanta_km} ${L.km}</span></span></a></li>`).join('\n')}\n</ul>`;
  const articoleAtr = atractii.map((a) => { const v = at(a); return `<article class="atractie" id="${esc(a.id)}">
${a.foto ? figura(a.foto, lang, 'atractie-foto', a.id, L) + '\n' : ''}<h2>${esc(v.nume)}</h2>
<p class="meta"><span class="tag tag-${esc(a.categorie)}">${L.categ[a.categorie]}</span>${esc(a.localitate)}, ${esc(txt(a.comuna, lang, `${a.id} comuna`))}, ${L.judet} · ${L.circa} ${a.distanta_km} ${L.km} ${L.deLaPoienel}</p>
<p><strong>${esc(v.rezumat)}</strong></p>
${v.descriere.map((p) => `<p>${esc(p)}</p>`).join('\n')}
<h3>${L.practic}</h3>
<ul>
${v.practic.map((p) => `<li>${esc(p)}</li>`).join('\n')}
</ul>
<p class="surse">${L.surse}: ${a.surse.map((s) => `<a href="${esc(s.url)}" rel="noopener" target="_blank">${esc(s.titlu)}</a>`).join(' · ')}</p>
</article>`; }).join('\n');
  const idLista = urlPagina(lang, 'atractii.html') + '#lista';
  const jsonldAtr = { '@context': 'https://schema.org', '@graph': [
    WEBSITE(lang), LOC(lang), webPage(lang, 'atractii.html', L.paginaAtr, idLista),
    {
      '@type': 'ItemList', '@id': idLista, name: L.atrNume, numberOfItems: atractii.length, itemListOrder: 'https://schema.org/ItemListOrderAscending', description: L.atrDesc,
      itemListElement: atractii.map((a, i) => { const v = at(a); return { '@type': 'ListItem', position: i + 1, item: {
        '@type': 'TouristAttraction', '@id': urlAtr(a), url: urlAtr(a), name: v.nume, additionalType: a.tip_schema, description: v.rezumat,
        address: { '@type': 'PostalAddress', addressLocality: a.localitate, addressRegion: 'Constanța', addressCountry: 'RO' },
        isAccessibleForFree: true, sameAs: a.surse.map((s) => s.url),
        ...(a.foto ? { image: { '@type': 'ImageObject', contentUrl: SITE + a.foto.src, thumbnailUrl: SITE + thumbDe(a.foto.src), caption: txt(a.foto.alt, lang, `${a.id} foto.alt`), ...(a.foto.credit ? { creditText: a.foto.credit } : {}) } } : {}),
      } }; }),
    },
  ] };
  completeaza(`${lang}/atractii.html`, {
    alternate: alternate(lang, 'atractii.html'), nav: nav(lang, 'atractii.html'), footer: footer(lang), jsonld: jsonld(jsonldAtr),
    sumar: L.sumarAtr(atractii.length, CATEG.filter((c) => countsCat[c]).map((c) => `${countsCat[c]} ${L.categ[c].toLowerCase()}`)),
    lista: listaAtr, atractii: articoleAtr,
  });

  // ── jurnal.html: însemnările ──
  const jt = (j) => ({ titlu: txt(j.titlu, lang, `jurnal ${j.data} titlu`), text: txt(j.text, lang, `jurnal ${j.data} text`) });
  const intrari = jurnal.length ? jurnal.map((j) => { const v = jt(j); return `<article class="jurnal-intrare" id="${esc(idJurnal(j))}" data-taguri="${j.taguri.join(' ')}">
<h2>${esc(v.titlu)}</h2>
<p class="meta"><time datetime="${esc(j.data)}">${dataLunga(j.data, L)}</time> ${j.taguri.map((t) => `<a class="tag tag-${t}" href="?tag=${t}#insemnari">${L.taguri[t]}</a>`).join(' ')}</p>
${v.text.map((p) => `<p>${esc(p)}</p>`).join('\n')}
${(j.foto || []).length ? `<div class="jurnal-foto">\n${j.foto.map((f) => figura(f, lang, '', `jurnal ${j.data}`, L)).join('\n')}\n</div>` : ''}
${(j.linkuri || []).length ? `<ul>\n${j.linkuri.map((l) => `<li><a href="${esc(l.url)}">${esc(txt(l.titlu, lang, `jurnal ${j.data} link`))}</a></li>`).join('\n')}\n</ul>` : ''}
</article>`; }).join('\n') : `<p class="gol">${L.jurnalGol}</p>`;
  const idBlog = urlPagina(lang, 'jurnal.html') + '#blog';
  const jsonldJurnal = { '@context': 'https://schema.org', '@graph': [
    WEBSITE(lang), LOC(lang), webPage(lang, 'jurnal.html', L.paginaJurnal, idBlog),
    {
      '@type': 'Blog', '@id': idBlog, name: L.jurnalNume, inLanguage: lang, url: urlPagina(lang, 'jurnal.html'),
      blogPost: jurnal.map((j) => { const v = jt(j); return {
        '@type': 'BlogPosting', '@id': urlPagina(lang, 'jurnal.html') + '#' + idJurnal(j), url: urlPagina(lang, 'jurnal.html') + '#' + idJurnal(j), headline: v.titlu, datePublished: j.data, inLanguage: lang,
        articleBody: v.text.join('\n\n'), keywords: j.taguri.map((t) => L.taguri[t]), author: ORG, publisher: ORG,
        image: (j.foto || []).map((f) => ({ '@type': 'ImageObject', contentUrl: SITE + f.src, thumbnailUrl: SITE + thumbDe(f.src), caption: txt(f.alt, lang, `jurnal ${j.data} foto.alt`) })),
      }; }),
    },
  ] };
  completeaza(`${lang}/jurnal.html`, {
    alternate: alternate(lang, 'jurnal.html'), nav: nav(lang, 'jurnal.html'), footer: footer(lang), jsonld: jsonld(jsonldJurnal),
    robots: `<meta name="robots" content="${jurnal.length ? 'index, follow, max-image-preview:large, max-snippet:-1' : 'noindex, follow'}">`,
    'jurnal-tabs': `<div class="type-tab active" data-tag="all">${L.toate} (${jurnal.length})</div>\n` + TAGURI.map((t) => `<div class="type-tab" data-tag="${t}">${L.taguri[t]} (${countsTag[t]})</div>`).join('\n'),
    jurnal: intrari,
  });
}

// ───────────────────────── sitemap.xml: toate paginile în ambele limbi, cu hreflang ─────────────────────────
const lastmod = (f) => fs.statSync(path.join(dir, f)).mtime.toISOString().slice(0, 10);
const paginiSitemap = PAGINI.filter((f) => !(f === 'jurnal.html' && !jurnal.length));
const xhtml = (f) => LANGS.map((l) => `<xhtml:link rel="alternate" hreflang="${l}" href="${urlPagina(l, f)}"/>`).join('') + `<xhtml:link rel="alternate" hreflang="x-default" href="${urlPagina('ro', f)}"/>`;
scrie('sitemap.xml', `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
${paginiSitemap.flatMap((f) => LANGS.map((l) => `<url><loc>${urlPagina(l, f)}</loc><lastmod>${lastmod(`${l}/${f}`)}</lastmod>${f === 'index.html' ? '<priority>1.0</priority>' : ''}${xhtml(f)}</url>`)).join('\n')}
${DATE_DESCHISE.filter((f) => f !== 'sitemap.xml').map((f) => `<url><loc>${SITE}${f}</loc><lastmod>${lastmod(f)}</lastmod></url>`).join('\n')}
</urlset>
`);

console.log(`${LANGS.join('+')}: ${specii.length} specii (${TIPURI.map((t) => `${ETICHETE.ro.plural[t]} ${counts[t]}`).join(', ')}), ${atractii.length} obiective, ${jurnal.length} însemnări${jurnal.length ? '' : ' (noindex)'}; sitemap: ${paginiSitemap.length * LANGS.length} pagini`);
