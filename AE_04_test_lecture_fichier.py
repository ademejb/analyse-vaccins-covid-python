
"""
Ce fichier contient des tests pour la fonction afficher_liste_vaccins.
Chaque test couvre un cas particulier : liste vide, liste avec un élément,
et liste avec plusieurs éléments.
"""

from AE_02_listes_type import afficher_liste_vaccins
from AE_00_type import VaccinData

"""
Test 1 : Liste vide
Vérifie que la fonction affiche un message approprié lorsque la liste est vide.
"""
print("Test 1 : Affichage d'une liste vide")
afficher_liste_vaccins([])

"""
Test 2 : Liste avec un seul élément
Vérifie que l'affichage fonctionne correctement avec une seule entrée.
"""
print("Test 2 : Affichage d'une liste avec un élément")
liste1 = [VaccinData("07/02/2021", "AstraZeneca", 273600)]
afficher_liste_vaccins(liste1)

"""
Test 3 : Liste avec plusieurs éléments
Vérifie que tous les éléments sont affichés correctement.
"""
print("Test 3 : Affichage d'une liste avec plusieurs éléments")
liste2 = [
    VaccinData("07/02/2021", "AstraZeneca", 273600),
    VaccinData("14/02/2021", "Pfizer", 316800),
    VaccinData("21/02/2021", "Moderna", 150000)
]
afficher_liste_vaccins(liste2)
