"""Ce script mesure les temps d’exécution (en nanosecondes) de quatre fonctions de recherche dichotomique :
- recherche_dicho_quelconque
- recherche_dicho_plus_petit_indice
- recherche_dicho_plus_grand_indice
- nombres_occurrences

Les tests sont réalisés sur des listes triées de tailles croissantes (1, 5, 20, 100),
avec 100 répétitions par mesure, puis les résultats sont affichés sous forme de courbes comparatives.
"""

from outils_dessin import *
from AE_02_listes_type import (
    recherche_dicho_quelconque,
    recherche_dicho_plus_petit_indice,
    recherche_dicho_plus_grand_indice,
    nombres_occurrences,
    convertir_liste_csv_en_vaccins
)
from outils_mesure import temps_en_nanoseconde
import timeit
from outils_csv import lecture_fichier_csv

"""
Chargement des données de fichiers CSV convertis en objets VaccinData.
Chaque fichier représente un volume croissant de données.
"""
liste_vaccins_1 = convertir_liste_csv_en_vaccins(lecture_fichier_csv("AE_donnee/AE_data_1.csv", ",", "latin-1", 1)[1])
liste_vaccins_5 = convertir_liste_csv_en_vaccins(lecture_fichier_csv("AE_donnee/AE_data_5.csv", ",", "latin-1", 1)[1])
liste_vaccins_20 = convertir_liste_csv_en_vaccins(lecture_fichier_csv("AE_donnee/AE_data_20.csv", ",", "latin-1", 1)[1])
liste_vaccins_100 = convertir_liste_csv_en_vaccins(lecture_fichier_csv("AE_donnee/AE_data_100.csv", ",", "latin-1", 1)[1])

nb_repet = 100  # Nombre de répétitions pour fiabiliser les mesures

"""
Mesure des temps pour la fonction recherche_dicho_quelconque.
Recherche d'une valeur présente dans chaque liste.
"""
print("\n--- recherche_dicho_quelconque ---")
temps_1 = timeit.timeit(stmt="recherche_dicho_quelconque(liste_vaccins_1,456770)", globals=globals(), number=nb_repet)
temps_5 = timeit.timeit(stmt="recherche_dicho_quelconque(liste_vaccins_5,404970)", globals=globals(), number=nb_repet)
temps_20 = timeit.timeit(stmt="recherche_dicho_quelconque(liste_vaccins_20,327110)", globals=globals(), number=nb_repet)
temps_100 = timeit.timeit(stmt="recherche_dicho_quelconque(liste_vaccins_100,445990)", globals=globals(), number=nb_repet)

courbe1 = [
    (0, 0),
    (1, temps_en_nanoseconde(temps_1 / nb_repet)),
    (5, temps_en_nanoseconde(temps_5 / nb_repet)),
    (20, temps_en_nanoseconde(temps_20 / nb_repet)),
    (100, temps_en_nanoseconde(temps_100 / nb_repet))
]

"""
Mesure des temps pour la fonction recherche_dicho_plus_petit_indice.
Elle retourne la première occurrence d'une valeur.
"""
print("--- recherche_dicho_plus_petit_indice ---")
temps_1_tri = timeit.timeit(stmt="recherche_dicho_plus_petit_indice(liste_vaccins_1,456770)", globals=globals(), number=nb_repet)
temps_5_tri = timeit.timeit(stmt="recherche_dicho_plus_petit_indice(liste_vaccins_5,404970)", globals=globals(), number=nb_repet)
temps_20_tri = timeit.timeit(stmt="recherche_dicho_plus_petit_indice(liste_vaccins_20,327110)", globals=globals(), number=nb_repet)
temps_100_tri = timeit.timeit(stmt="recherche_dicho_plus_petit_indice(liste_vaccins_100,445990)", globals=globals(), number=nb_repet)

courbe2 = [
    (0, 0),
    (1, temps_en_nanoseconde(temps_1_tri / nb_repet)),
    (5, temps_en_nanoseconde(temps_5_tri / nb_repet)),
    (20, temps_en_nanoseconde(temps_20_tri / nb_repet)),
    (100, temps_en_nanoseconde(temps_100_tri / nb_repet))
]

dessine_lignes_brisees(courbe_rouge=courbe1, courbe_bleue=courbe2)

"""
Mesure des temps pour la fonction recherche_dicho_plus_grand_indice.
Elle retourne la dernière occurrence d'une valeur.
"""
print("\n--- recherche_dicho_plus_grand_indice ---")
temps_1_med = timeit.timeit(stmt="recherche_dicho_plus_grand_indice(liste_vaccins_1,456770)", globals=globals(), number=nb_repet)
temps_5_med = timeit.timeit(stmt="recherche_dicho_plus_grand_indice(liste_vaccins_5,404970)", globals=globals(), number=nb_repet)
temps_20_med = timeit.timeit(stmt="recherche_dicho_plus_grand_indice(liste_vaccins_20,327110)", globals=globals(), number=nb_repet)
temps_100_med = timeit.timeit(stmt="recherche_dicho_plus_grand_indice(liste_vaccins_100,445990)", globals=globals(), number=nb_repet)

courbe3 = [
    (0, 0),
    (1, temps_en_nanoseconde(temps_1_med / nb_repet)),
    (5, temps_en_nanoseconde(temps_5_med / nb_repet)),
    (20, temps_en_nanoseconde(temps_20_med / nb_repet)),
    (100, temps_en_nanoseconde(temps_100_med / nb_repet))
]

"""
Mesure des temps pour la fonction nombres_occurrences.
Elle retourne le nombre total d’occurrences d'une valeur donnée.
"""
print("--- nombres_occurrences ---")
temps_1_mod = timeit.timeit(stmt="nombres_occurrences(liste_vaccins_1,456770)", globals=globals(), number=nb_repet)
temps_5_mod = timeit.timeit(stmt="nombres_occurrences(liste_vaccins_5,404970)", globals=globals(), number=nb_repet)
temps_20_mod = timeit.timeit(stmt="nombres_occurrences(liste_vaccins_20,327110)", globals=globals(), number=nb_repet)
temps_100_mod = timeit.timeit(stmt="nombres_occurrences(liste_vaccins_100,445990)", globals=globals(), number=nb_repet)

courbe4 = [
    (0, 0),
    (1, temps_en_nanoseconde(temps_1_mod / nb_repet)),
    (5, temps_en_nanoseconde(temps_5_mod / nb_repet)),
    (20, temps_en_nanoseconde(temps_20_mod / nb_repet)),
    (100, temps_en_nanoseconde(temps_100_mod / nb_repet))
]

dessine_lignes_brisees(courbe_rouge=courbe3, courbe_bleue=courbe4)
