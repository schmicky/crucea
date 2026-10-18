// Filtrarea însemnărilor după tag. Fără JavaScript se văd toate însemnările; taburile apar doar cu JS.
(function () {
  const tabs = document.getElementById('jurnal-tabs');
  if (!tabs) return;
  const articole = [...document.querySelectorAll('article.jurnal-intrare[data-taguri]')];
  function filtreaza(tag) {
    tabs.querySelectorAll('.type-tab').forEach((t) => t.classList.toggle('active', t.dataset.tag === tag));
    articole.forEach((a) => { a.hidden = tag !== 'all' && !a.dataset.taguri.split(' ').includes(tag); });
  }
  tabs.querySelectorAll('.type-tab').forEach((t) => t.addEventListener('click', () => {
    filtreaza(t.dataset.tag);
    history.replaceState(null, '', t.dataset.tag === 'all' ? location.pathname + '#insemnari' : '?tag=' + t.dataset.tag + '#insemnari');
  }));
  // linkurile din chips și adresele cu ?tag=… deschid pagina gata filtrată
  document.querySelectorAll('a.tag[href^="?tag="]').forEach((a) => a.addEventListener('click', (e) => { e.preventDefault(); filtreaza(new URL(a.href).searchParams.get('tag')); history.replaceState(null, '', a.getAttribute('href')); }));
  const initial = new URLSearchParams(location.search).get('tag');
  tabs.hidden = false;
  if (initial && tabs.querySelector(`.type-tab[data-tag="${initial}"]`)) filtreaza(initial);
})();
