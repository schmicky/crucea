// Test de fum pentru pagina unui studiu de caz: servește repo-ul local, deschide pagina în Chromium,
// numără fișele și problemele, caută imagini rupte și erori JS, face două capturi (grilă + o fișă).
//   node test.js <director-studiu-relativ-la-repo> <director-capturi>
// Are nevoie de playwright-core (npm i playwright-core, în scratchpad) și de Chromium-ul preinstalat.
const path = require('path'), fs = require('fs'), http = require('http');
const root = path.resolve(__dirname, '..', '..', '..', '..');          // rădăcina repo-ului
const studiu = process.argv[2], shots = process.argv[3] || process.cwd();
const modDirs = [process.env.PW_MODULE, path.join(process.cwd(), 'node_modules', 'playwright-core'),
  ...fs.readdirSync('/tmp').filter(d => d.startsWith('claude')).map(d => path.join('/tmp', d))].filter(Boolean);
function findModule() {
  for (const d of modDirs) { try { return require(d.endsWith('playwright-core') ? d : require.resolve('playwright-core', { paths: [d] })); } catch (e) {} }
  const hit = require('child_process').execSync("find /tmp -maxdepth 6 -type d -name playwright-core 2>/dev/null | head -1").toString().trim();
  if (hit) return require(hit);
  throw new Error('playwright-core lipsește: npm i playwright-core (în scratchpad) sau PW_MODULE=<cale>');
}
const { chromium } = findModule();
const exe = fs.readdirSync('/opt/pw-browsers').filter(d => d.startsWith('chromium-')).map(d => `/opt/pw-browsers/${d}/chrome-linux/chrome`).find(fs.existsSync);
const srv = http.createServer((q, s) => {
  const p = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  const f = fs.existsSync(p) && fs.statSync(p).isDirectory() ? path.join(p, 'index.html') : p;
  if (!fs.existsSync(f)) { s.writeHead(404); return s.end(); }
  s.writeHead(200, { 'Content-Type': f.endsWith('.html') ? 'text/html; charset=utf-8' : f.endsWith('.webp') ? 'image/webp' : 'application/octet-stream' });
  fs.createReadStream(f).pipe(s);
}).listen(0, async () => {
  const port = srv.address().port;
  const b = await chromium.launch({ executablePath: exe });
  const pg = await b.newPage({ viewport: { width: 1280, height: 900 } });
  const errs = [], e404 = []; pg.on('pageerror', e => errs.push(e.message));
  pg.on('response', r => r.status() === 404 && !/favicon/.test(r.url()) && e404.push(r.url()));
  await pg.goto(`http://localhost:${port}/${studiu}/`); await pg.waitForTimeout(800);
  const cards = await pg.locator('.card').count(), prob = await pg.locator('.pb').count();
  console.log('fișe', cards, '| probleme', prob, '| filtre', (await pg.locator('.chip').allTextContents()).join(' · '));
  const broken = await pg.evaluate(() => [...document.images].filter(i => i.getAttribute('src') && i.complete && i.naturalWidth === 0).map(i => i.src));
  console.log('imagini rupte:', broken.length ? broken : 'niciuna');
  await pg.screenshot({ path: path.join(shots, 'grila.png') });
  await pg.locator('.card').first().click(); await pg.waitForTimeout(500);
  console.log('fișa 1:', await pg.locator('#f-ro').textContent(), '|', await pg.locator('#f-tags').textContent());
  await pg.screenshot({ path: path.join(shots, 'fisa.png') });
  const real = errs.filter(e => !/wikipedia|fetch|net::ERR/i.test(e));
  console.log('erori JS:', real.length ? real : 'niciuna', '| 404:', e404.length ? e404 : 'niciunul');
  await b.close(); srv.close();
  if (!cards || broken.length || real.length || e404.length) process.exit(1);
});
