# Koda lauzējs: AI Efektivitāte

## Projekta apraksts

Šī ir termināļa spēle, kurā lomas ir apmainītas: skaitli iedomājas cilvēks,
bet min dators. Spēlētājs iedomājas veselu skaitli no 1 līdz 100, un dators
to uzmin ar binārās meklēšanas stratēģiju - katru reizi min diapazona vidu.

Spēlētājs atbild ar vienu burtu:

| Atbilde | Nozīme |
|---------|--------|
| `l` | mans skaitlis ir lielāks |
| `m` | mans skaitlis ir mazāks |
| `p` | pareizi, dators uzminēja |

Projektā ir trīs faili:

- `engine.py` - algoritma funkcijas (bez `input()` un `print()`)
- `main.py` - pati spēle, kas izmanto `engine.py` funkcijas
- `README.md` - šis apraksts

## Palaišana

Failiem `main.py` un `engine.py` jāatrodas vienā mapē. Atver termināli šajā
mapē un ieraksti:

```
python main.py
```

## Algoritma skaidrojums

Dators glabā divas robežas: `apaksa` (sākumā 1) un `augsa` (sākumā 100).
Iedomātais skaitlis vienmēr atrodas starp tām.

1. Minējums ir diapazona vidus: `(apaksa + augsa) // 2`.
2. Ja atbilde ir `l`, skaitlis ir lielāks par minējumu, tāpēc
   `apaksa = minejums + 1`.
3. Ja atbilde ir `m`, skaitlis ir mazāks par minējumu, tāpēc
   `augsa = minejums - 1`.
4. Soļi atkārtojas, līdz atbilde ir `p`.

### Kāpēc +1 un -1?

Ja spēlētājs atbild `l`, tad pats minējums noteikti nav pareizais skaitlis,
tāpēc to var izmest no diapazona. Ja rakstītu `apaksa = minejums` bez `+ 1`,
programma varētu iestrēgt bezgalīgā ciklā.

Piemērs: `apaksa = 99`, `augsa = 100`. Minējums ir `(99 + 100) // 2 = 99`.
Ja atbilde ir `l` un mēs rakstām `apaksa = minejums`, tad `apaksa` atkal
ir 99, nākamais minējums atkal ir 99, un tā bez gala. Ar `minejums + 1`
diapazons katrā solī kļūst mazāks, tāpēc spēle vienmēr beidzas.

## Pretrunu noteikšana

Pēc katras atbildes programma pārbauda, vai `apaksa > augsa`. Ja tā ir,
diapazonā vairs nav neviena skaitļa - tātad neviens skaitlis neatbilst
visām spēlētāja atbildēm. Tas nozīmē, ka spēlētājs kļūdījās vai krāpās,
un programma paziņo par pretrunu un beidz spēli.

## Efektivitāte: O(log n) pret O(n)

Binārā meklēšana ar katru minējumu izmet apmēram pusi no atlikušajiem
skaitļiem: 100 → 50 → 25 → 12 → 6 → 3 → 1. Minējumu skaits aug tikpat lēni
kā logaritms, tāpēc sarežģītība ir **O(log n)**.

Lineārā meklēšana min pēc kārtas: 1, 2, 3, ... Sliktākajā gadījumā jāpārbauda
visi skaitļi, tāpēc sarežģītība ir **O(n)**.

| Skaitļu daudzums | Binārā meklēšana (max) | Lineārā meklēšana (max) |
|------------------|------------------------|-------------------------|
| 100 | 7 | 100 |
| 1000 | 10 | 1000 |

Kad skaitļu ir 10 reizes vairāk, lineārajai meklēšanai vajag 10 reizes
vairāk minējumu, bet binārajai - tikai 3 papildu minējumus.

### Matemātiskais pamatojums

Ar `k` minējumiem var atšķirt `2^k - 1` skaitļus.

100 skaitļiem:

- `2^6 - 1 = 63 < 100` - ar 6 minējumiem nepietiek
- `2^7 - 1 = 127 ≥ 100` - ar 7 minējumiem pietiek

Tātad vajag ne vairāk kā **7** minējumus.

1000 skaitļiem:

- `2^9 - 1 = 511 < 1000` - ar 9 minējumiem nepietiek
- `2^10 - 1 = 1023 ≥ 1000` - ar 10 minējumiem pietiek

Tātad vajag ne vairāk kā **10** minējumus.

## Testi

### Parastās partijas

| Iedomātais skaitlis | Datora minējumi | Atbildes | Minējumu skaits |
|---------------------|-----------------|----------|-----------------|
| 73 | 50, 75, 62, 68, 71, 73 | l, m, l, l, l, p | 6 |
| 25 | 50, 25 | m, p | 2 |
| 100 | 50, 75, 88, 94, 97, 99, 100 | l, l, l, l, l, l, p | 7 |

Lielākais minējumu skaits testos: **7** (skaitlim 100). Tas sakrīt ar
aprēķināto maksimumu.

### Pretrunīga spēle

| Minējums | Atbilde | apaksa | augsa |
|----------|---------|--------|-------|
| 50 | l | 51 | 100 |
| 75 | m | 51 | 74 |
| 62 | m | 51 | 61 |
| 56 | m | 51 | 55 |
| 53 | m | 51 | 52 |
| 51 | m | 51 | 50 |

Pēc pēdējās atbildes `apaksa = 51`, `augsa = 50`, tātad `apaksa > augsa`.
Programma izdrukā:

```
Tavas atbildes bija pretrunīgas - šķiet, ka tu krāpies!
Spēle beigusies.
```

Programma neiestrēgst, bet beidz darbu.

### Nederīga ievade

Iedomātais skaitlis ir 73.

| Minējums | Ievade | Rezultāts |
|----------|--------|-----------|
| 50 | `x` | noraidīts: "Nederīga atbilde!", minējumos neieskaita, jautā vēlreiz |
| 50 | `L ` (lielais burts ar atstarpi) | pieņemts kā `l` |
| 75 | `m` | pieņemts |
| 62 | `l` | pieņemts |
| 68 | `l` | pieņemts |
| 71 | `l` | pieņemts |
| 73 | `p` | "Man vajadzēja 6 minējumus." |

Nederīgā ievade `x` netika ieskaitīta, tāpēc rezultāts ir 6, nevis 7.
