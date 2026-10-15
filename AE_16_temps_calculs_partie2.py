"""
Ce script mesure les temps d'exécution (en nanosecondes) des fonctions :
- est_triee_par_doses
- tri_selection_doses
- mediane_doses_triee
- modalites_doses

Les mesures sont réalisées sur des fichiers de tailles croissantes (1, 5, 20, 100),
et les temps sont affichés sous forme de courbes à l'aide de dessine_lignes_brisees.
"""

from outils_dessin import *
from AE_02_listes_type import (
    mediane_doses_triee, modalites_doses,
    tri_selection_doses, est_triee_par_doses,
    convertir_liste_csv_en_vaccins
)
from outils_mesure import temps_en_nanoseconde
import timeit
from outils_csv import lecture_fichier_csv

"""
Chargement des fichiers CSV et conversion en listes de VaccinData.
Chaque fichier correspond à un volume de données différent.
"""
liste_vaccins_1 = convertir_liste_csv_en_vaccins(lecture_fichier_csv("AE_donnee/AE_data_1.csv", ",", "latin-1", 1)[1])
liste_vaccins_5 = convertir_liste_csv_en_vaccins(lecture_fichier_csv("AE_donnee/AE_data_5.csv", ",", "latin-1", 1)[1])
liste_vaccins_20 = convertir_liste_csv_en_vaccins(lecture_fichier_csv("AE_donnee/AE_data_20.csv", ",", "latin-1", 1)[1])
liste_vaccins_100 = convertir_liste_csv_en_vaccins(lecture_fichier_csv("AE_donnee/AE_data_100.csv", ",", "latin-1", 1)[1])

nb_repet = 10  # Nombre de répétitions pour chaque mesure


"""
Mesure des temps d'exécution de la fonction est_triee_par_doses
sur des listes de tailles croissantes.
"""
print("\n--- Temps est_triee ---")
temps_1 = timeit.timeit(stmt="est_triee_par_doses(liste_vaccins_1)", globals=globals(), number=nb_repet)
temps_5 = timeit.timeit(stmt="est_triee_par_doses(liste_vaccins_5)", globals=globals(), number=nb_repet)
temps_20 = timeit.timeit(stmt="est_triee_par_doses(liste_vaccins_20)", globals=globals(), number=nb_repet)
temps_100 = timeit.timeit(stmt="est_triee_par_doses(liste_vaccins_100)", globals=globals(), number=nb_repet)

courbe1 = [
    (0, 0),
    (1, temps_en_nanoseconde(temps_1 / nb_repet)),
    (5, temps_en_nanoseconde(temps_5 / nb_repet)),
    (20, temps_en_nanoseconde(temps_20 / nb_repet)),
    (100, temps_en_nanoseconde(temps_100 / nb_repet))
]


"""
Mesure des temps d'exécution de la fonction tri_selection_doses
sur les mêmes listes (avec copie pour ne pas modifier les données d'origine).
"""
print("--- Temps tri_selection_doses ---")
temps_1_tri = timeit.timeit(stmt="tri_selection_doses(liste_vaccins_1.copy())", globals=globals(), number=nb_repet)
temps_5_tri = timeit.timeit(stmt="tri_selection_doses(liste_vaccins_5.copy())", globals=globals(), number=nb_repet)
temps_20_tri = timeit.timeit(stmt="tri_selection_doses(liste_vaccins_20.copy())", globals=globals(), number=nb_repet)
temps_100_tri = timeit.timeit(stmt="tri_selection_doses(liste_vaccins_100.copy())", globals=globals(), number=nb_repet)

courbe2 = [
    (0, 0),
    (1, temps_en_nanoseconde(temps_1_tri / nb_repet)),
    (5, temps_en_nanoseconde(temps_5_tri / nb_repet)),
    (20, temps_en_nanoseconde(temps_20_tri / nb_repet)),
    (100, temps_en_nanoseconde(temps_100_tri / nb_repet))
]

"""
Affichage comparatif des temps : est_triee vs tri_selection_doses
"""
dessine_lignes_brisees(courbe_rouge=courbe1, courbe_bleue=courbe2)


"""
Mesure des temps d'exécution de mediane_doses_triee
sur des listes triées de tailles différentes.
"""
print("\n--- Temps mediane_doses_triee ---")
temps_1_med = timeit.timeit(stmt="mediane_doses_triee(liste_vaccins_1)", globals=globals(), number=nb_repet)
temps_5_med = timeit.timeit(stmt="mediane_doses_triee(liste_vaccins_5)", globals=globals(), number=nb_repet)
temps_20_med = timeit.timeit(stmt="mediane_doses_triee(liste_vaccins_20)", globals=globals(), number=nb_repet)
temps_100_med = timeit.timeit(stmt="mediane_doses_triee(liste_vaccins_100)", globals=globals(), number=nb_repet)

courbe3 = [
    (0, 0),
    (1, temps_en_nanoseconde(temps_1_med / nb_repet)),
    (5, temps_en_nanoseconde(temps_5_med / nb_repet)),
    (20, temps_en_nanoseconde(temps_20_med / nb_repet)),
    (100, temps_en_nanoseconde(temps_100_med / nb_repet))
]

"""
Mesure des temps d'exécution de modalites_doses
sur des listes triées de tailles différentes.
"""
print("--- Temps modalites_doses ---")
temps_1_mod = timeit.timeit(stmt="modalites_doses(liste_vaccins_1)", globals=globals(), number=nb_repet)
temps_5_mod = timeit.timeit(stmt="modalites_doses(liste_vaccins_5)", globals=globals(), number=nb_repet)
temps_20_mod = timeit.timeit(stmt="modalites_doses(liste_vaccins_20)", globals=globals(), number=nb_repet)
temps_100_mod = timeit.timeit(stmt="modalites_doses(liste_vaccins_100)", globals=globals(), number=nb_repet)

courbe4 = [
    (0, 0),
    (1, temps_en_nanoseconde(temps_1_mod / nb_repet)),
    (5, temps_en_nanoseconde(temps_5_mod / nb_repet)),
    (20, temps_en_nanoseconde(temps_20_mod / nb_repet)),
    (100, temps_en_nanoseconde(temps_100_mod / nb_repet))
]

"""
Affichage comparatif des temps : mediane_doses_triee vs modalites_doses
"""
dessine_lignes_brisees(courbe_rouge=courbe3, courbe_bleue=courbe4)
