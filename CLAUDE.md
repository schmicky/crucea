# Poienel — proiectul de amenajare din Crucea (Constanța)

Reguli de lucru stabilite cu George Șerban:

- **Studiu de caz de vegetație**: când se cere un studiu de caz, un inventar sau o analiză a vegetației din poze
  („ca la Kaufland / Tăbăcărie"), se folosește skill-ul `studiu-caz-vegetatie` din `.claude/skills/`, nu o pagină scrisă de mână.
- **Fiecare pas se publică**: commit pe ramura de lucru, push, apoi merge în `master` cu `git merge --no-ff --no-edit`
  și push pe `master` (dacă `master` de pe GitHub a avansat, întâi `git fetch origin master && git reset --hard origin/master`).
  Se spune în răspuns că s-a făcut.
- **Limba**: română, cu diacritice, în fișiere și în răspunsuri.
- **Pagina principală** (`index.html` din rădăcină) se generează din `README.md` la publicare; nu se editează direct.
- **Fișierele generate** (`miyawaki/index-est*.html`, `plan-miyawaki-est*.md`, `resurse/oferte/comenzi-miyawaki-est.md`,
  `studiu-caz-*/index.html`) se refac din scripturile lor, nu se editează de mână, ca datele și paginile să nu se despartă.
- **Jurnalul** proiectului e în `time-lapse/plan-implementare-nord-miyawaki.md`: fiecare decizie sau răspuns de la furnizori
  primește o intrare datată, cea mai nouă prima.
