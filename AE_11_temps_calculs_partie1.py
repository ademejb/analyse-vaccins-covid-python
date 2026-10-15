"""
Ce script mesure le temps d'exécution (en nanosecondes) des fonctions :
- min_doses
- max_doses
- moyenne_doses
- ecart_type_doses

Les mesures sont effectuées sur des listes de vaccins de tailles 1, 5, 20 et 100,
et les résultats sont affichés sous forme de courbes (2 par graphique).
"""

from outils_dessin import *  # Pour l'affichage graphique
from AE_02_listes_type import min_doses, max_doses, moyenne_doses, ecart_type_doses, convertir_liste_csv_en_vaccins
from outils_mesure import temps_en_nanoseconde
from outils_csv import lecture_fichier_csv
import timeit

"""
Chargement des fichiers CSV et conversion en listes de VaccinData.
Chaque fichier correspond à une taille différente de données.
"""
liste_1 = convertir_liste_csv_en_vaccins(lecture_fichier_csv("AE_donnee/AE_data_1.csv", ",", "latin-1", 1)[1])
liste_5 = convertir_liste_csv_en_vaccins(lecture_fichier_csv("AE_donnee/AE_data_5.csv", ",", "latin-1", 1)[1])
liste_20 = convertir_liste_csv_en_vaccins(lecture_fichier_csv("AE_donnee/AE_data_20.csv", ",", "latin-1", 1)[1])
liste_100 = convertir_liste_csv_en_vaccins(lecture_fichier_csv("AE_donnee/AE_data_100.csv", ",", "latin-1", 1)[1])

"""
Préparation des données pour les mesures :
- tailles : tailles des listes
- listes : les listes elles-mêmes
- nb_repet : nombre de répétitions pour fiabiliser la mesure
"""
tailles = [1, 5, 20, 100]
listes = [liste_1, liste_5, liste_20, liste_100]
nb_repet = 50

"""
Initialisation des courbes de performance.
Chaque courbe est une liste de points (taille, temps).
Le point (0, 0) est ajouté pour le visuel.
"""
courbe_min = [(0, 0)]
courbe_max = [(0, 0)]
courbe_moyenne = [(0, 0)]
courbe_ecart = [(0, 0)]

"""
Boucle de mesure de temps pour chaque taille de liste.
On mesure le temps moyen d'exécution de chaque fonction.
"""
for taille, liste in zip(tailles, listes):
    t_min = timeit.timeit(lambda: min_doses(liste), number=nb_repet)
    t_max = timeit.timeit(lambda: max_doses(liste), number=nb_repet)
    t_moy = timeit.timeit(lambda: moyenne_doses(liste), number=nb_repet)
    t_et = timeit.timeit(lambda: ecart_type_doses(liste), number=nb_repet)

    # Conversion du temps moyen en nanosecondes et ajout aux courbes
    courbe_min.append((taille, temps_en_nanoseconde(t_min / nb_repet)))
    courbe_max.append((taille, temps_en_nanoseconde(t_max / nb_repet)))
    courbe_moyenne.append((taille, temps_en_nanoseconde(t_moy / nb_repet)))
    courbe_ecart.append((taille, temps_en_nanoseconde(t_et / nb_repet)))

"""
Affichage des résultats sous forme de courbes :
- Graphique 1 : min_doses (rouge) vs moyenne_doses (bleu)
- Graphique 2 : max_doses (rouge) vs ecart_type_doses (bleu)
"""
dessine_lignes_brisees(courbe_rouge=courbe_min, courbe_bleue=courbe_moyenne)
dessine_lignes_brisees(courbe_rouge=courbe_max, courbe_bleue=courbe_ecart)
