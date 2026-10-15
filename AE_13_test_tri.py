"""
Ce fichier teste la fonction tri_selection_doses du module AE_02_listes_type.
Il vérifie si le tri est correct, si l'ordre est croissant selon nb_doses,
et si le nombre d’éléments reste inchangé après le tri.
"""

from AE_02_listes_type import *

"""
Création d'une liste non triée de vaccins avec des nb_doses dans le désordre.
"""
liste_depart = [
    VaccinData("01/01/2021", "Moderna", 80),
    VaccinData("01/01/2021", "Pfizer", 10),
    VaccinData("01/01/2021", "Janssen", 50),
    VaccinData("01/01/2021", "AstraZeneca", 30)
]

"""
Affichage de la liste avant tri pour vérification visuelle.
"""
print("Liste de départ :")
afficher_liste_vaccins(liste_depart)

"""
Tri de la liste avec la fonction tri_selection_doses.
"""
liste_triee = tri_selection_doses(liste_depart)

"""
Affichage de la liste après tri pour s'assurer que l'ordre est respecté.
"""
print("\nListe après tri :")
afficher_liste_vaccins(liste_triee)

"""
Vérifie que la liste est bien triée par nb_doses.
"""
print("\nLa liste est-elle triée ?", est_triee_par_doses(liste_triee))

"""
Vérifie que la taille de la liste reste identique après tri.
Cela garantit qu'aucun élément n'a été perdu ou ajouté.
"""
print("Nombre d'éléments inchangé ?", len(liste_depart) == len(liste_triee))
