// Popup-ul și filtrarea speciilor. Datele și etichetele (în limba paginii) vin din
// <script type="application/json" id="specii-data">, pus în pagină de build.mjs.
(function () {
  const DATE = JSON.parse(document.getElementById('specii-data').textContent);
  const T = DATE.etichete;           // etichetele traduse: luni, tipuri, lumină, texte
  const PLANTS = Object.fromEntries(DATE.specii.map((d) => [d.cod, d]));
  const typeColor = { arbore: '#2d6a2d', fructifer: '#c0392b', arbust: '#8e44ad', aromat: '#c7a200', ierbacee: '#1a7a9a' };
  const luminaIcon = { soare: '☀', mixt: '⛅', umbra: '🌑' };
  let currentType = 'all';

  const wikiCache = {};
  async function wikiSummary(title) {
    if (wikiCache[title]) return wikiCache[title];
    try {
      const resp = await fetch('https://en.wikipedia.org/api/rest_v1/page/summary/' + encodeURIComponent(title.replace(/ /g, '_')) + '?redirect=true', { headers: { Accept: 'application/json' } });
      const data = resp.ok ? await resp.json() : {};
      wikiCache[title] = { img: (data.thumbnail && data.thumbnail.source) || '' };
    } catch (e) { wikiCache[title] = { img: '' }; }
    return wikiCache[title];
  }

  function renderTable() {
    document.querySelectorAll('#plants-table tr[data-cod]').forEach((row) => {
      row.hidden = currentType !== 'all' && row.dataset.type !== currentType;
    });
  }

  async function showPopup(cod, data) {
    document.getElementById('popup-name').textContent = data.nume;
    document.getElementById('popup-lat').textContent = data.lat;
    document.getElementById('popup-meta').innerHTML = `<span class="popup-tag" style="background: ${typeColor[data.type]};">${T.tipuri[data.type]}</span><span class="popup-tag">${T.cod}: ${cod}</span>`;

    const img = document.getElementById('popup-img');
    const photoState = document.getElementById('popup-photo-state');
    photoState.textContent = T.foto_cautare; photoState.style.display = 'block';
    img.style.display = 'none'; img.classList.remove('loaded');
    const wikiData = await wikiSummary(data.lat);
    if (wikiData.img) {
      img.onload = () => { img.classList.add('loaded'); img.style.display = 'block'; photoState.style.display = 'none'; };
      img.onerror = () => { photoState.textContent = T.foto_lipsa; img.style.display = 'none'; photoState.style.display = 'block'; };
      img.src = wikiData.img;
    } else { photoState.textContent = T.foto_lipsa; }

    document.getElementById('h2').textContent = data.h2;
    document.getElementById('h5').textContent = data.h5;
    document.getElementById('hm').textContent = data.hm;
    const lumEl = document.getElementById('popup-lum');
    lumEl.textContent = `${luminaIcon[data.lumina] || ''} ${T.lumina[data.lumina] || ''}`.trim();
    lumEl.className = `l-${data.lumina}`;
    document.getElementById('popup-lumd').textContent = data.lumin_note || '';
    document.getElementById('water-dose').textContent = T.apa_doza.replace('{n}', data.water_l);
    document.getElementById('water-freq').textContent = T.apa_frecventa.replace('{n}', data.water_f);

    const calBar = document.getElementById('popup-cal-bar');
    const calMonths = document.getElementById('popup-cal-months');
    calBar.innerHTML = ''; calMonths.innerHTML = '';
    const stateEmoji = { repaus: '❄️', vegetatie: '🌿', inflorire: '🌸' };
    data.phenology.forEach((month, idx) => {
      const [, veg, flower] = month;
      const state = flower ? 'inflorire' : veg ? 'vegetatie' : 'repaus';
      const cell = document.createElement('div');
      cell.className = `cal-cell s-${state}`; cell.title = T.luni[idx]; cell.textContent = stateEmoji[state];
      cell.style.cssText = 'font-size:16px;display:flex;align-items:center;justify-content:center';
      calBar.appendChild(cell);
      const m = document.createElement('div'); m.className = 'cal-m'; m.textContent = T.luni[idx]; calMonths.appendChild(m);
    });

    document.getElementById('overlay-bg').classList.add('visible');
    document.getElementById('popup').classList.add('visible');
    document.body.style.overflow = 'hidden';
  }

  function closePopup() {
    document.getElementById('popup').classList.remove('visible');
    document.getElementById('overlay-bg').classList.remove('visible');
    document.body.style.overflow = 'auto';
  }

  document.querySelectorAll('#plants-table tr[data-cod]').forEach((row) => {
    row.addEventListener('click', (e) => {
      e.preventDefault();
      showPopup(row.dataset.cod, PLANTS[row.dataset.cod]).catch((err) => console.error('Error loading plant details:', err));
    });
  });
  document.getElementById('type-tabs').hidden = false;
  document.getElementById('popup-x').addEventListener('click', closePopup);
  document.getElementById('overlay-bg').addEventListener('click', closePopup);
  document.querySelectorAll('.type-tab').forEach((tab) => {
    tab.addEventListener('click', () => {
      document.querySelectorAll('.type-tab').forEach((t) => t.classList.remove('active'));
      tab.classList.add('active');
      currentType = tab.dataset.type || 'all';
      renderTable();
    });
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closePopup(); });
})();
