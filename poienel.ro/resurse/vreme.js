// Prognoza pe 7 zile din Open-Meteo (gratuit, fără cheie, CORS deschis), pentru banda din antet.
// Este un adaos: fără JavaScript sau fără rețea banda rămâne ascunsă și pagina nu se schimbă.
// Configurația (coordonate, etichete în limba paginii) vine din <script id="vreme-data">, generat de build.mjs.
(function () {
  const box = document.getElementById('vreme');
  const cfgEl = document.getElementById('vreme-data');
  if (!box || !cfgEl) return;
  const C = JSON.parse(cfgEl.textContent);
  const T = C.etichete;
  const CACHE = 'poienel-vreme-v1';
  const URL = 'https://api.open-meteo.com/v1/forecast?latitude=' + C.lat + '&longitude=' + C.lon +
    '&daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=' + encodeURIComponent('Europe/Bucharest') + '&forecast_days=7';

  // Pictograme proprii, 24×24, doar contur; culorile vin din CSS (.sol, .nor, .apa, .zapada, .fulger)
  const CLOUD = 'M7 17.5h10.2a3.8 3.8 0 0 0 .5-7.57A5.6 5.6 0 0 0 6.9 11 3.3 3.3 0 0 0 7 17.5z';
  const SUN_BIG = '<g class="sol"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></g>';
  const SUN_SMALL = '<g class="sol"><circle cx="8.5" cy="8.5" r="3.2"/><path d="M8.5 2.6v1.6M2.6 8.5h1.6M4.3 4.3l1.1 1.1M12.7 4.3l-1.1 1.1M4.3 12.7l1.1-1.1"/></g>';
  const cloud = (tf) => '<g transform="' + tf + '"><path class="nor" d="' + CLOUD + '"/></g>';
  const CLOUD_UP = cloud('translate(0 -3.6)');
  const CLOUD_SUN = cloud('translate(4.2 3.6) scale(.82)');
  const drops = (n, strong) => '<path class="apa' + (strong ? ' tare' : '') + '" d="' + (n === 2 ? 'M9 18.4l-.9 2.6M14 18.4l-.9 2.6' : 'M8 18.4l-.9 2.8M12 18.4l-.9 2.8M16 18.4l-.9 2.8') + '"/>';
  const dots = (n) => '<path class="zapada" d="' + (n === 3 ? 'M8.5 19v.01M12 20.8v.01M15.5 19v.01' : 'M7.5 19v.01M10.2 20.8v.01M13 19v.01M15.8 20.8v.01M18 19v.01') + '"/>';
  const ICON = {
    clear: SUN_BIG,
    mostlyClear: SUN_SMALL + cloud('translate(8 7.5) scale(.62)'),
    partly: SUN_SMALL + CLOUD_SUN,
    overcast: cloud('translate(0 0)'),
    fog: '<path class="nor" d="M4 9h16M6.5 13h11M4 17h16"/>',
    drizzle: CLOUD_UP + '<path class="apa" d="M8.5 19.2v.01M12 20.8v.01M15.5 19.2v.01"/>',
    rainLight: CLOUD_UP + drops(2),
    rain: CLOUD_UP + drops(3),
    rainHeavy: CLOUD_UP + drops(3, true),
    showers: SUN_SMALL + CLOUD_SUN + '<path class="apa" d="M10.5 19.2l-.8 2.2M15 19.2l-.8 2.2"/>',
    snow: CLOUD_UP + dots(3),
    snowHeavy: CLOUD_UP + dots(5),
    snowShowers: SUN_SMALL + CLOUD_SUN + '<path class="zapada" d="M10.5 19.6v.01M14 21v.01M17.5 19.6v.01"/>',
    thunder: CLOUD_UP + '<path class="fulger" d="M12.8 13.2l-3 4.6h3.6l-1.8 3.9"/>',
    hail: CLOUD_UP + '<path class="fulger" d="M12.8 13.2l-3 4.6h3.6l-1.8 3.9"/><path class="zapada" d="M7.5 19.6v.01M17 19.6v.01"/>',
  };
  const ALIAS = { freezingDrizzle: 'drizzle', freezingRain: 'rain', snowLight: 'snow', snowGrains: 'snow', showersHeavy: 'showers' };
  // Codurile WMO folosite de Open-Meteo → cheia pictogramei și a descrierii
  function key(c) {
    if (c === 0) return 'clear'; if (c === 1) return 'mostlyClear'; if (c === 2) return 'partly'; if (c === 3) return 'overcast';
    if (c === 45 || c === 48) return 'fog';
    if (c === 51 || c === 53 || c === 55) return 'drizzle'; if (c === 56 || c === 57) return 'freezingDrizzle';
    if (c === 61) return 'rainLight'; if (c === 63) return 'rain'; if (c === 65) return 'rainHeavy'; if (c === 66 || c === 67) return 'freezingRain';
    if (c === 71) return 'snowLight'; if (c === 73) return 'snow'; if (c === 75) return 'snowHeavy'; if (c === 77) return 'snowGrains';
    if (c === 80 || c === 81) return 'showers'; if (c === 82) return 'showersHeavy'; if (c === 85 || c === 86) return 'snowShowers';
    if (c === 95) return 'thunder'; if (c >= 96) return 'hail';
    return 'overcast';
  }
  const svg = (k) => '<svg viewBox="0 0 24 24" aria-hidden="true">' + (ICON[ALIAS[k] || k] || ICON.overcast) + '</svg>';
  const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');

  function render(d) {
    const days = d.daily.time, code = d.daily.weather_code, tmax = d.daily.temperature_2m_max, tmin = d.daily.temperature_2m_min;
    const fmt = new Intl.DateTimeFormat(C.lang, { weekday: 'short' });
    box.querySelector('.vreme-zile').innerHTML = days.map((iso, i) => {
      const p = iso.split('-').map(Number);
      let nume = i === 0 ? T.azi : i === 1 ? T.maine : fmt.format(new Date(p[0], p[1] - 1, p[2])).replace('.', '');
      nume = nume.charAt(0).toUpperCase() + nume.slice(1);
      const k = key(code[i]), desc = T.conditii[ALIAS[k] && !T.conditii[k] ? ALIAS[k] : k] || '';
      const mx = Math.round(tmax[i]), mn = Math.round(tmin[i]);
      const aria = nume + ': ' + desc + ', ' + T.max + ' ' + mx + '°, ' + T.min + ' ' + mn + '°';
      return '<li title="' + esc(aria) + '" aria-label="' + esc(aria) + '"><span class="vreme-zi">' + esc(nume) + '</span>' + svg(k) +
        '<span class="vreme-t"><b>' + mx + '°</b><i>' + mn + '°</i></span></li>';
    }).join('');
    box.hidden = false;
  }
  const valid = (d) => d && d.daily && Array.isArray(d.daily.time) && d.daily.time.length >= 3 && d.daily.weather_code && d.daily.temperature_2m_max && d.daily.temperature_2m_min;
  const azi = () => { const n = new Date(); return n.getFullYear() + '-' + String(n.getMonth() + 1).padStart(2, '0') + '-' + String(n.getDate()).padStart(2, '0'); };
  let cached = null;
  try { cached = JSON.parse(localStorage.getItem(CACHE)); } catch (e) {}
  // cache de o oră, ca să nu apelăm API-ul la fiecare pagină; ținut doar dacă începe de azi
  if (cached && valid(cached.d) && Date.now() - cached.t < 3600e3 && cached.d.daily.time[0] === azi()) { render(cached.d); return; }
  const ctl = new AbortController(); const timer = setTimeout(() => ctl.abort(), 6000);
  fetch(URL, { signal: ctl.signal }).then((r) => (r.ok ? r.json() : Promise.reject(r.status))).then((d) => {
    if (!valid(d)) throw new Error('format');
    try { localStorage.setItem(CACHE, JSON.stringify({ t: Date.now(), d })); } catch (e) {}
    render(d);
  }).catch(() => {
    if (cached && valid(cached.d) && Date.now() - cached.t < 24 * 3600e3) render(cached.d); // rețea căzută: ultima prognoză, dacă e de azi
  }).finally(() => clearTimeout(timer));
})();
