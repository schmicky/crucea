#!/usr/bin/env node
// Generează din specii.json părțile de pagină care trebuie să existe fără JavaScript:
// tabelul static, fișele speciilor, datele JSON-LD, datele inline pentru popup,
// plus specii.csv și sitemap.xml. Rulare: node build.mjs (din folderul poienel.ro).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const dir = path.dirname(fileURLToPath(import.meta.url));
const SITE = 'https://poienel.ro/';
const MONTHS = ['Ian', 'Feb', 'Mar', 'Apr', 'Mai', 'Iun', 'Iul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
const TYPE = {
  arbore:    { label: 'Arbore',    plural: 'Arbori' },
  fructifer: { label: 'Fructifer', plural: 'Fructiferi' },
  arbust:    { label: 'Arbust',    plural: 'Arbuști' },
  aromat:    { label: 'Aromatic',  plural: 'Aromatice' },
  ierbacee:  { label: 'Ierbacee',  plural: 'Ierbacee' },
};
const LUMINA = { soare: 'soare', mixt: 'soare sau semiumbră', umbra: 'umbră' };

const specii = JSON.parse(fs.readFileSync(path.join(dir, 'specii.json'), 'utf8'));
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

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

function descriere(s) {
  const t = TYPE[s.type].label.toLowerCase();
  const parts = [
    `${t}, ${s.hm} la maturitate (${s.h2} la 2 ani, ${s.h5} la 5 ani)`,
    `lumină: ${LUMINA[s.lumina] || s.lumina}`,
    `apă în anii 1–2: ${s.water_l} l la udare, de ${s.water_f} ori pe săptămână vara`,
    `înflorire: ${luni(s.phenology, 2)}`,
  ];
  let d = parts.join('; ') + '.';
  if (s.lumin_note) d += ' ' + s.lumin_note;
  return d;
}

// 1. Tabelul static
const tabel = specii.map((s) => `<tr data-cod="${esc(s.cod)}" data-type="${esc(s.type)}">
<td><strong>${esc(s.cod)}</strong></td>
<td><a href="#specie-${esc(s.cod)}">${esc(s.ro)}</a><br><em class="lat">${esc(s.lat)}</em></td>
<td><span class="tag tag-${esc(s.type)}">${TYPE[s.type].label}</span></td>
<td>${esc(s.hm)}</td>
</tr>`).join('\n');

// 2. Fișele speciilor (details/summary, lizibile fără JavaScript)
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

// 3. JSON-LD
const counts = Object.fromEntries(Object.keys(TYPE).map((t) => [t, specii.filter((s) => s.type === t).length]));
const descriereSite = `Poienel este o grădină în transformare la Crucea, județul Constanța: ${specii.length} de specii de arbori, arbuști, pomi fructiferi, plante aromatice și ierbacee, plus o pădure Miyawaki de 340 m² cu 919 puieți din 30 de specii autohtone de silvostepă dobrogeană.`;
const jsonld = {
  '@context': 'https://schema.org',
  '@graph': [
    { '@type': 'WebSite', '@id': SITE + '#website', url: SITE, name: 'Poienel', inLanguage: 'ro', description: descriereSite },
    {
      '@type': 'Place', '@id': SITE + '#loc', name: 'Poienel', url: SITE, image: SITE + 'resurse/poienel-logo.png',
      description: descriereSite,
      address: { '@type': 'PostalAddress', addressLocality: 'Crucea', addressRegion: 'Constanța', addressCountry: 'RO' },
      sameAs: ['https://github.com/schmicky/crucea', 'https://schmicky.github.io/crucea/'],
    },
    {
      '@type': 'WebPage', '@id': SITE + '#webpage', url: SITE, name: 'Poienel — Crucea, Constanța', inLanguage: 'ro',
      isPartOf: { '@id': SITE + '#website' }, about: { '@id': SITE + '#loc' }, mainEntity: { '@id': SITE + '#specii' },
      primaryImageOfPage: SITE + 'resurse/poienel-logo.png',
    },
    {
      '@type': 'Dataset', '@id': SITE + '#dataset', name: 'Speciile grădinii Poienel', inLanguage: 'ro', url: SITE,
      description: `Lista celor ${specii.length} de specii plantate la Poienel, cu cod, nume românesc și latin, tip, înălțime la 2 ani, 5 ani și la maturitate, cerințe de lumină și apă și calendar lunar de udare, vegetație și înflorire.`,
      license: 'https://creativecommons.org/licenses/by/4.0/',
      creator: { '@id': SITE + '#loc' },
      distribution: [
        { '@type': 'DataDownload', encodingFormat: 'application/json', contentUrl: SITE + 'specii.json' },
        { '@type': 'DataDownload', encodingFormat: 'text/csv', contentUrl: SITE + 'specii.csv' },
      ],
    },
    {
      '@type': 'ItemList', '@id': SITE + '#specii', name: 'Speciile grădinii Poienel', numberOfItems: specii.length,
      itemListOrder: 'https://schema.org/ItemListUnordered',
      itemListElement: specii.map((s, i) => ({
        '@type': 'ListItem', position: i + 1,
        item: {
          '@type': 'Thing', '@id': SITE + '#specie-' + s.cod, url: SITE + '#specie-' + s.cod,
          name: s.ro, alternateName: s.lat, identifier: s.cod,
          additionalType: 'https://schema.org/Taxon',
          description: descriere(s),
          sameAs: wiki(s.lat),
        },
      })),
    },
  ],
};

// 4. Datele inline pentru popup (aceeași sursă)
const dateInline = JSON.stringify(specii).replace(/</g, '\\u003c');

// Înlocuiește regiunile marcate din index.html
const regiuni = {
  tabel, fise,
  jsonld: `<script type="application/ld+json">\n${JSON.stringify(jsonld)}\n</script>`,
  date: `<script type="application/json" id="specii-data">${dateInline}</script>`,
  sumar: `${specii.length} de specii: ${Object.keys(TYPE).map((t) => `${counts[t]} ${TYPE[t].plural.toLowerCase()}`).join(', ')}.`,
  tabs: `<div class="type-tab active" data-type="all">Toate (${specii.length})</div>\n` +
    Object.keys(TYPE).map((t) => `<div class="type-tab" data-type="${t}">${TYPE[t].plural} (${counts[t]})</div>`).join('\n'),
};
const indexPath = path.join(dir, 'index.html');
let html = fs.readFileSync(indexPath, 'utf8');
for (const [nume, continut] of Object.entries(regiuni)) {
  const re = new RegExp(`(<!-- BUILD:${nume} -->)[\\s\\S]*?(<!-- /BUILD:${nume} -->)`);
  if (!re.test(html)) throw new Error(`Lipsește regiunea BUILD:${nume} din index.html`);
  html = html.replace(re, (_, a, b) => `${a}\n${continut}\n${b}`);
}
fs.writeFileSync(indexPath, html);

// 5. specii.csv
const csvCell = (v) => { const s = String(v ?? ''); return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s; };
const csvHead = ['cod', 'nume', 'nume_latin', 'tip', 'inaltime_2_ani', 'inaltime_5_ani', 'inaltime_matur', 'lumina', 'nota_lumina', 'apa_l_udare', 'udari_pe_saptamana', 'luni_udare', 'luni_vegetatie', 'luni_inflorire', 'wikipedia'];
const csv = [csvHead.join(',')].concat(specii.map((s) => [
  s.cod, s.ro, s.lat, TYPE[s.type].label, s.h2, s.h5, s.hm, LUMINA[s.lumina] || s.lumina, s.lumin_note || '',
  s.water_l, s.water_f, luni(s.phenology, 0), luni(s.phenology, 1), luni(s.phenology, 2), wiki(s.lat),
].map(csvCell).join(','))).join('\n') + '\n';
fs.writeFileSync(path.join(dir, 'specii.csv'), '﻿' + csv);

// 6. sitemap.xml
const azi = new Date().toISOString().slice(0, 10);
fs.writeFileSync(path.join(dir, 'sitemap.xml'), `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>${SITE}</loc><lastmod>${azi}</lastmod><changefreq>monthly</changefreq><priority>1.0</priority></url>
<url><loc>${SITE}llms.txt</loc><lastmod>${azi}</lastmod><changefreq>monthly</changefreq></url>
<url><loc>${SITE}specii.json</loc><lastmod>${azi}</lastmod><changefreq>monthly</changefreq></url>
<url><loc>${SITE}specii.csv</loc><lastmod>${azi}</lastmod><changefreq>monthly</changefreq></url>
</urlset>
`);

console.log(`index.html, specii.csv, sitemap.xml: ${specii.length} specii (${Object.keys(TYPE).map((t) => `${TYPE[t].plural} ${counts[t]}`).join(', ')})`);
