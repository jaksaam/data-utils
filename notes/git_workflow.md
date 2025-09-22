# Git Workflow Notes

## Objasnjenja
- `branch` – kopija mog projekta ili ti mesto gde cu raditi a da nije main moja grana
Primer:

Imaš main sa 3 fajla.

Napraviš granu feature/login.

Sada u toj grani možeš dodavati/menjati fajlove, ali main i dalje ostaje čist.

- `merge` – spoj promene iz moje grane nazad u main
Git napravi poseban merge commit da se zna da su dve grane spojene.
Istorija ostaje “razgranata” (vidi se ko je gde radio).

- `rebase` – presloži tvoje commite da izgleda kao da si ih radio tek posle najnovijih izmena na main.
Kao da uzmeš svoj rad i zalepiš ga na kraj glavne priče.
Rezultat: istorija izgleda čisto i linearno (nema grananja).
Ali: rebase “prepisuje istoriju” → pravi nove commit ID-jeve.
Koristiš ga uglavnom lokalno da počistiš granu pre push-a.

Simulacija PR (Pull Request)
PR = “Zahtev za povlačenje koda”.
👉 Na GitHub-u otvoriš Pull Request i kažeš timu:
“Evo na grani feature/login imam nove izmene. Pogledajte, pa ako je ok — spojite sa main.”
PR služi za code review (da drugi vide šta si radio).
Kad se odobri → uradi se merge (najčešće).
To je standard u firmama jer niko ne gura kod direktno u main.