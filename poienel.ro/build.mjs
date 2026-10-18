#!/usr/bin/env node
// Generează, din fișierele JSON ale site-ului, tot ce trebuie să existe în pagini fără JavaScript
// (regiunile <!-- BUILD:nume --> … <!-- /BUILD:nume -->), fișierele de date deschise și sitemap.xml.
// Rulare: node build.mjs (din folderul poienel.ro). Regulile sunt în CLAUDE.md.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const dir = path.dirname(fileURLToPath(import.meta.url));
const SITE = 'https://poienel.ro/';
const MONTHS = ['Ian', 'Feb', 'Mar', 'Apr', 'Mai', 'Iun', 'Iul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
const LUNI_LUNGI = ['ianuarie', 'februarie', 'martie', 'aprilie', 'mai', 'iunie', 'iulie', 'august', 'septembrie', 'octombrie', 'noiembrie', 'decembrie'];

const citeste = (f) => JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
const scrie = (f, s) => fs.writeFileSync(path.join(dir, f), s);
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const jsonInline = (o) => JSON.stringify(o).replace(/</g, '\\u003c');
const jsonld = (o) => `<script type="application/ld+json">\n${jsonInline(o)}\n</script>`;
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
const dataRo = (iso) => { const [y, m, d] = iso.split('-').map(Number); return `${d} ${LUNI_LUNGI[m - 1]} ${y}`; };

// Înlocuiește regiunile marcate dintr-o pagină; eroare dacă lipsește vreuna.
function completeaza(fisier, regiuni) {
  let html = fs.readFileSync(path.join(dir, fisier), 'utf8');
  for (const [nume, continut] of Object.entries(regiuni)) {
    const re = new RegExp(`(<!-- BUILD:${nume} -->)[\\s\\S]*?(<!-- /BUILD:${nume} -->)`);
    if (!re.test(html)) throw new Error(`Lipsește regiunea BUILD:${nume} din ${fisier}`);
    html = html.replace(re, (_, a, b) => `${a}\n${continut}\n${b}`);
  }
  scrie(fisier, html);
}

// Entitățile comune tuturor paginilor (aceleași @id peste tot)
const descriereSite = 'Poienel este o grădină în transformare la Crucea, județul Constanța: 65 de specii de arbori, arbuști, pomi fructiferi, plante aromatice și ierbacee, plus o pădure Miyawaki de 340 m² cu 919 puieți din 30 de specii autohtone de silvostepă dobrogeană.';
const WEBSITE = { '@type': 'WebSite', '@id': SITE + '#website', url: SITE, name: 'Poienel', inLanguage: 'ro', description: descriereSite };
const LOC = {
  '@type': 'Place', '@id': SITE + '#loc', name: 'Poienel', url: SITE, image: SITE + 'resurse/poienel-logo.png', description: descriereSite,
  address: { '@type': 'PostalAddress', addressLocality: 'Crucea', addressRegion: 'Constanța', addressCountry: 'RO' },
  sameAs: ['https://github.com/schmicky/crucea', 'https://schmicky.github.io/crucea/'],
};
const webPage = (fisier, name, mainEntityId) => ({
  '@type': 'WebPage', '@id': SITE + fisier + '#webpage', url: SITE + (fisier === 'index.html' ? '' : fisier), name, inLanguage: 'ro',
  isPartOf: { '@id': SITE + '#website' }, about: { '@id': SITE + '#loc' }, mainEntity: { '@id': mainEntityId },
  primaryImageOfPage: SITE + 'resurse/poienel-logo.png',
});

// Bara de meniu, aceeași pe toate paginile; pagina curentă primește aria-current
const MENIU = [
  { href: 'index.html', text: 'Grădina' },
  { href: 'index.html#specii', text: 'Specii' },
  { href: 'atractii.html', text: 'Atracții turistice' },
  { href: 'jurnal.html', text: 'Jurnal' },
  { href: 'index.html#planuri', text: 'Planuri' },
];
const nav = (fisier) => `<nav class="menu" aria-label="Meniu principal">
<ul>
<li><a class="menu-brand" href="index.html"><img src="resurse/poienel-semn.svg" alt="" width="26" height="26">Poienel</a></li>
${MENIU.map((m) => `<li><a href="${m.href}"${m.href === fisier ? ' aria-current="page"' : ''}>${m.text}</a></li>`).join('\n')}
</ul>
</nav>`;

// ───────────────────────── index.html: speciile ─────────────────────────
const TYPE = {
  arbore:    { label: 'Arbore',    plural: 'Arbori' },
  fructifer: { label: 'Fructifer', plural: 'Fructiferi' },
  arbust:    { label: 'Arbust',    plural: 'Arbuști' },
  aromat:    { label: 'Aromatic',  plural: 'Aromatice' },
  ierbacee:  { label: 'Ierbacee',  plural: 'Ierbacee' },
};
const LUMINA = { soare: 'soare', mixt: 'soare sau semiumbră', umbra: 'umbră' };
const specii = citeste('specii.json');

// [[udare, vegetație, înflorire] × 12] → „Apr–Iul, Sep”
function luni(phen, idx) {
  const on = phen.map((m) => m[idx] === 1);
  const runs = [];
  for (let i = 0; i < 12; i++) {
    if (!on[i]) continue;
    if (runs.length && runs[runs.length - 1][1] === i - 1) runs[runs.length - 1][1] = i;
    else runs.push([i, i]);
  }
  if (!runs.length) return '—';
  if (runs.length === 1 && runs[0][0] === 0 && runs[0][1] === 11) return 'tot anul';
  return runs.map(([a, b]) => (a === b ? MONTHS[a] : `${MONTHS[a]}–${MONTHS[b]}`)).join(', ');
}
const wiki = (lat) => 'https://en.wikipedia.org/wiki/' + encodeURIComponent(lat.replace(/ × /g, '_×_').replace(/ var\. .*$/, '').replace(/ \(.*\)$/, '').replace(/ '.*'$/, '').replace(/ /g, '_'));
function descriereSpecie(s) {
  const parts = [
    `${TYPE[s.type].label.toLowerCase()}, ${s.hm} la maturitate (${s.h2} la 2 ani, ${s.h5} la 5 ani)`,
    `lumină: ${LUMINA[s.lumina] || s.lumina}`,
    `apă în anii 1–2: ${s.water_l} l la udare, de ${s.water_f} ori pe săptămână vara`,
    `înflorire: ${luni(s.phenology, 2)}`,
  ];
  return parts.join('; ') + '.' + (s.lumin_note ? ' ' + s.lumin_note : '');
}
const counts = Object.fromEntries(Object.keys(TYPE).map((t) => [t, specii.filter((s) => s.type === t).length]));

const tabel = specii.map((s) => `<tr data-cod="${esc(s.cod)}" data-type="${esc(s.type)}">
<td><strong>${esc(s.cod)}</strong></td>
<td><a href="#specie-${esc(s.cod)}">${esc(s.ro)}</a><br><em class="lat">${esc(s.lat)}</em></td>
<td><span class="tag tag-${esc(s.type)}">${TYPE[s.type].label}</span></td>
<td>${esc(s.hm)}</td>
</tr>`).join('\n');

const fise = specii.map((s) => `<details class="fisa" id="specie-${esc(s.cod)}">
<summary><strong>${esc(s.cod)}</strong> ${esc(s.ro)} <em class="lat">${esc(s.lat)}</em> <span class="tag tag-${esc(s.type)}">${TYPE[s.type].label}</span></summary>
<dl>
<dt>Înălțime</dt><dd>${esc(s.h2)} la 2 ani · ${esc(s.h5)} la 5 ani · ${esc(s.hm)} la maturitate</dd>
<dt>Lumină</dt><dd>${esc(LUMINA[s.lumina] || s.lumina)}${s.lumin_note ? ' — ' + esc(s.lumin_note) : ''}</dd>
<dt>Apă (anii 1–2)</dt><dd>${s.water_l} l la udare, de ${s.water_f} ${s.water_f === 1 ? 'dată' : 'ori'} pe săptămână vara</dd>
<dt>Udare</dt><dd>${luni(s.phenology, 0)}</dd>
<dt>Vegetație</dt><dd>${luni(s.phenology, 1)}</dd>
<dt>Înflorire</dt><dd>${luni(s.phenology, 2)}</dd>
<dt>Referință</dt><dd><a href="${wiki(s.lat)}" rel="noopener" target="_blank">${esc(s.lat)} pe Wikipedia</a></dd>
</dl>
</details>`).join('\n');

const jsonldSpecii = { '@context': 'https://schema.org', '@graph': [
  WEBSITE, LOC, webPage('index.html', 'Poienel — Crucea, Constanța', SITE + '#specii'),
  {
    '@type': 'Dataset', '@id': SITE + '#dataset', name: 'Speciile grădinii Poienel', inLanguage: 'ro', url: SITE,
    description: `Lista celor ${specii.length} de specii plantate la Poienel, cu cod, nume românesc și latin, tip, înălțime la 2 ani, 5 ani și la maturitate, cerințe de lumină și apă și calendar lunar de udare, vegetație și înflorire.`,
    license: 'https://creativecommons.org/licenses/by/4.0/', creator: { '@id': SITE + '#loc' },
    distribution: [
      { '@type': 'DataDownload', encodingFormat: 'application/json', contentUrl: SITE + 'specii.json' },
      { '@type': 'DataDownload', encodingFormat: 'text/csv', contentUrl: SITE + 'specii.csv' },
    ],
  },
  {
    '@type': 'ItemList', '@id': SITE + '#specii', name: 'Speciile grădinii Poienel', numberOfItems: specii.length, itemListOrder: 'https://schema.org/ItemListUnordered',
    itemListElement: specii.map((s, i) => ({ '@type': 'ListItem', position: i + 1, item: {
      '@type': 'Thing', '@id': SITE + '#specie-' + s.cod, url: SITE + '#specie-' + s.cod, name: s.ro, alternateName: s.lat, identifier: s.cod,
      additionalType: 'https://schema.org/Taxon', description: descriereSpecie(s), sameAs: wiki(s.lat),
    } })),
  },
] };

completeaza('index.html', {
  nav: nav('index.html'),
  jsonld: jsonld(jsonldSpecii),
  sumar: `${specii.length} de specii: ${Object.keys(TYPE).map((t) => `${counts[t]} ${TYPE[t].plural.toLowerCase()}`).join(', ')}.`,
  tabs: `<div class="type-tab active" data-type="all">Toate (${specii.length})</div>\n` + Object.keys(TYPE).map((t) => `<div class="type-tab" data-type="${t}">${TYPE[t].plural} (${counts[t]})</div>`).join('\n'),
  tabel, fise,
  date: `<script type="application/json" id="specii-data">${jsonInline(specii)}</script>`,
});

const csvCell = (v) => { const s = String(v ?? ''); return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s; };
const csvHead = ['cod', 'nume', 'nume_latin', 'tip', 'inaltime_2_ani', 'inaltime_5_ani', 'inaltime_matur', 'lumina', 'nota_lumina', 'apa_l_udare', 'udari_pe_saptamana', 'luni_udare', 'luni_vegetatie', 'luni_inflorire', 'wikipedia'];
scrie('specii.csv', '﻿' + [csvHead.join(',')].concat(specii.map((s) => [
  s.cod, s.ro, s.lat, TYPE[s.type].label, s.h2, s.h5, s.hm, LUMINA[s.lumina] || s.lumina, s.lumin_note || '',
  s.water_l, s.water_f, luni(s.phenology, 0), luni(s.phenology, 1), luni(s.phenology, 2), wiki(s.lat),
].map(csvCell).join(','))).join('\n') + '\n');

// ───────────────────────── atractii.html: obiectivele din zonă ─────────────────────────
const CATEG = { natura: 'Natură', religios: 'Religios', istorie: 'Istorie', cultura: 'Cultură', peisaj: 'Peisaj' };
const atractii = citeste('atractii.json').slice().sort((a, b) => a.distanta_km - b.distanta_km);
const countsCat = Object.fromEntries(Object.keys(CATEG).map((c) => [c, atractii.filter((a) => a.categorie === c).length]));
const urlAtr = (a) => SITE + 'atractii.html#' + a.id;

const listaAtr = `<ul class="atractii-lista">\n${atractii.map((a) => `<li><a href="#${esc(a.id)}">${a.foto ? `<img src="${esc(thumbDe(a.foto.src))}" alt="" width="56" height="56" loading="lazy">` : '<span class="fara-foto"></span>'}<span><span class="nume">${esc(a.nume)}</span><span class="cat">${CATEG[a.categorie]} · ${esc(a.localitate)} · ~${a.distanta_km} km</span></span></a></li>`).join('\n')}\n</ul>`;

function figuraAtr(a) {
  if (!a.foto) return '';
  const thumb = thumbDe(a.foto.src);
  if (!fs.existsSync(path.join(dir, thumb))) throw new Error(`Lipsește miniatura ${thumb} (rulează python foto.py)`);
  const d = dimJpeg(thumb), D = dimJpeg(a.foto.src);
  return `<figure class="atractie-foto"><a href="${esc(a.foto.src)}" title="Deschide fotografia mare (${D.w}×${D.h})"><img src="${esc(thumb)}" alt="${esc(a.foto.alt || '')}" width="${d.w}" height="${d.h}" loading="lazy"></a>${a.foto.credit ? `<figcaption>Foto: ${esc(a.foto.credit)}</figcaption>` : ''}</figure>\n`;
}
const articoleAtr = atractii.map((a) => `<article class="atractie" id="${esc(a.id)}">
${figuraAtr(a)}<h2>${esc(a.nume)}</h2>
<p class="meta"><span class="tag tag-${esc(a.categorie)}">${CATEG[a.categorie]}</span>${esc(a.localitate)}, ${esc(a.comuna)}, județul Constanța · circa ${a.distanta_km} km de Poienel</p>
<p><strong>${esc(a.rezumat)}</strong></p>
${a.descriere.map((p) => `<p>${esc(p)}</p>`).join('\n')}
<h3>Practic</h3>
<ul>
${a.practic.map((p) => `<li>${esc(p)}</li>`).join('\n')}
</ul>
<p class="surse">Surse: ${a.surse.map((s) => `<a href="${esc(s.url)}" rel="noopener" target="_blank">${esc(s.titlu)}</a>`).join(' · ')}</p>
</article>`).join('\n');

const jsonldAtr = { '@context': 'https://schema.org', '@graph': [
  WEBSITE, LOC, webPage('atractii.html', 'Atracții turistice în jurul Poienelului — Crucea, Constanța', SITE + 'atractii.html#lista'),
  {
    '@type': 'ItemList', '@id': SITE + 'atractii.html#lista', name: 'Atracții turistice în jurul Poienelului', numberOfItems: atractii.length, itemListOrder: 'https://schema.org/ItemListOrderAscending',
    description: 'Obiective naturale, istorice și religioase la cel mult o oră de mers de Crucea, Constanța, în ordinea distanței.',
    itemListElement: atractii.map((a, i) => ({ '@type': 'ListItem', position: i + 1, item: {
      '@type': 'TouristAttraction', '@id': urlAtr(a), url: urlAtr(a), name: a.nume, additionalType: a.tip_schema, description: a.rezumat,
      address: { '@type': 'PostalAddress', addressLocality: a.localitate, addressRegion: 'Constanța', addressCountry: 'RO' },
      isAccessibleForFree: true, sameAs: a.surse.map((s) => s.url),
      ...(a.foto ? { image: { '@type': 'ImageObject', contentUrl: SITE + a.foto.src, thumbnailUrl: SITE + thumbDe(a.foto.src), caption: a.foto.alt || '', ...(a.foto.credit ? { creditText: a.foto.credit } : {}) } } : {}),
    } })),
  },
] };

completeaza('atractii.html', {
  nav: nav('atractii.html'),
  jsonld: jsonld(jsonldAtr),
  sumar: `${atractii.length} obiective: ${Object.keys(CATEG).filter((c) => countsCat[c]).map((c) => `${countsCat[c]} ${CATEG[c].toLowerCase()}`).join(', ')}.`,
  lista: listaAtr,
  atractii: articoleAtr,
});

// ───────────────────────── jurnal.html: însemnările ─────────────────────────
const jurnal = citeste('jurnal.json').slice().sort((a, b) => b.data.localeCompare(a.data));
const idJurnal = (j) => j.id || j.data;
const intrariJurnal = jurnal.length ? jurnal.map((j) => `<article class="jurnal-intrare" id="${esc(idJurnal(j))}">
<h2>${esc(j.titlu)}</h2>
<p><time datetime="${esc(j.data)}">${dataRo(j.data)}</time></p>
${(j.text || []).map((p) => `<p>${esc(p)}</p>`).join('\n')}
${(j.foto || []).length ? `<div class="jurnal-foto">\n${j.foto.map((f) => {
  const thumb = thumbDe(f.src);
  if (!fs.existsSync(path.join(dir, thumb))) throw new Error(`Lipsește miniatura ${thumb} (rulează python foto.py)`);
  const d = dimJpeg(thumb), D = dimJpeg(f.src);
  return `<figure><a href="${esc(f.src)}" title="Deschide fotografia mare (${D.w}×${D.h})"><img src="${esc(thumb)}" alt="${esc(f.alt || '')}" width="${d.w}" height="${d.h}" loading="lazy"></a>${f.alt ? `<figcaption>${esc(f.alt)}</figcaption>` : ''}</figure>`;
}).join('\n')}\n</div>` : ''}
${(j.linkuri || []).length ? `<ul>\n${j.linkuri.map((l) => `<li><a href="${esc(l.url)}">${esc(l.titlu)}</a></li>`).join('\n')}\n</ul>` : ''}
</article>`).join('\n')
  : '<p class="gol">Jurnalul începe în curând: primele însemnări vor fi despre măsurători, comenzile de puieți și plantarea pădurii Miyawaki din toamna lui 2026.</p>';

const jsonldJurnal = { '@context': 'https://schema.org', '@graph': [
  WEBSITE, LOC, webPage('jurnal.html', 'Jurnalul grădinii — Poienel, Crucea, Constanța', SITE + 'jurnal.html#blog'),
  {
    '@type': 'Blog', '@id': SITE + 'jurnal.html#blog', name: 'Jurnalul grădinii Poienel', inLanguage: 'ro', url: SITE + 'jurnal.html',
    blogPost: jurnal.map((j) => ({
      '@type': 'BlogPosting', '@id': SITE + 'jurnal.html#' + idJurnal(j), url: SITE + 'jurnal.html#' + idJurnal(j), headline: j.titlu, datePublished: j.data, inLanguage: 'ro',
      articleBody: (j.text || []).join('\n\n'), image: (j.foto || []).map((f) => ({ '@type': 'ImageObject', contentUrl: SITE + f.src, thumbnailUrl: SITE + thumbDe(f.src), caption: f.alt || '' })), author: { '@type': 'Organization', name: 'Poienel' },
    })),
  },
] };

completeaza('jurnal.html', {
  nav: nav('jurnal.html'),
  jsonld: jsonld(jsonldJurnal),
  // fără însemnări pagina e goală: nu se indexează până apare prima
  robots: `<meta name="robots" content="${jurnal.length ? 'index, follow, max-image-preview:large, max-snippet:-1' : 'noindex, follow'}">`,
  jurnal: intrariJurnal,
});

// ───────────────────────── sitemap.xml ─────────────────────────
const lastmod = (f) => fs.statSync(path.join(dir, f)).mtime.toISOString().slice(0, 10);
const pagini = fs.readdirSync(dir).filter((f) => f.endsWith('.html') && !(f === 'jurnal.html' && !jurnal.length))
  .sort((a, b) => (a === 'index.html' ? -1 : b === 'index.html' ? 1 : a.localeCompare(b)));
const urlSitemap = (loc, f, extra = '') => `<url><loc>${loc}</loc><lastmod>${lastmod(f)}</lastmod>${extra}</url>`;
scrie('sitemap.xml', `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${pagini.map((f) => urlSitemap(f === 'index.html' ? SITE : SITE + f, f, f === 'index.html' ? '<priority>1.0</priority>' : '')).join('\n')}
${['llms.txt', 'specii.json', 'specii.csv', 'atractii.json', 'jurnal.json'].map((f) => urlSitemap(SITE + f, f)).join('\n')}
</urlset>
`);

console.log(`index.html: ${specii.length} specii (${Object.keys(TYPE).map((t) => `${TYPE[t].plural} ${counts[t]}`).join(', ')})`);
console.log(`atractii.html: ${atractii.length} obiective; jurnal.html: ${jurnal.length} însemnări${jurnal.length ? '' : ' (noindex)'}; sitemap.xml: ${pagini.length} pagini`);
