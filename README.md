# Covid-19 Vaccine Delivery Analysis in Python

Algorithms project from my first year of a BSc in Applied Mathematics & Computer Science for Social Sciences (MIASHS, Université Paul-Valéry Montpellier 3, course TE24MI).

The program loads French open data on weekly Covid-19 vaccine deliveries and lets you explore it from an interactive menu: filtering, descriptive statistics and value search. Every statistic and algorithm (sorting, binary search…) is implemented from scratch, without external libraries. The runtime complexity of each function is then measured on datasets of increasing size.

## Data

- **Source:** data.gouv.fr, national Covid-19 vaccine delivery flows (`flux-total-nat.csv`, about 350 rows)
- **Fields used:** week-ending date, vaccine type (Pfizer, Moderna, AstraZeneca, Janssen), number of doses
- **Test datasets:** `AE_donnee/AE_data_{0,1,5,20,100}.csv`, samples from 0 to 100 rows used for tests and timing

## Features

| Area | What is implemented |
|---|---|
| Data model | `VaccinData` class and conversion from CSV rows to objects |
| Statistics | Minimum, maximum, mean, standard deviation, median, distinct values |
| Filtering | Selection by vaccine type |
| Sorting | Selection sort and is-sorted check |
| Search | Binary search (standard, first index, last index) and occurrence counting |
| Performance | Runtime measurements and plots against input size |
| Testing | One test program per function (normal case, empty list, single element, missing value…) |

Example output (20-row file):

```
Indicateurs statistiques sur nb_doses :
 - Minimum : 206370
 - Maximum : 473830
 - Moyenne : 364605.5
 - Écart type : 95801.72
 - Médiane : 391980.0
```

*(The program interface is in French.)*

## Running the project

Requires Python 3 with tkinter (included by default on macOS and Windows).

```bash
python AE_10_analyseur.py               # interactive menu
python AE_13_test_tri.py                # example test
python AE_16_temps_calculs_partie2.py   # runtime plots
```

## File structure

- `AE_00_type.py`: data type definition
- `AE_02_listes_type.py`: all functions (statistics, sorting, search)
- `AE_10_analyseur.py`: main program (menu)
- `AE_01`–`AE_09`, `AE_12`–`AE_15`, `AE_17`–`AE_20`: test programs
- `AE_11`, `AE_16`, `AE_21`: runtime measurements

## Credits

The modules `outils_csv.py`, `outils_mesure.py` and `outils_dessin.py` were provided by Gwenaël Richomme as part of the TE24MI course. All other code is my own.

**Author:** Adem Ejebli
