
# Ce fichier teste la fonction afficher_liste_vaccins avec différents cas

from AE_02_listes_type import afficher_liste_vaccins
from AE_00_type import VaccinData

""" 
Test 1 : Liste vide
Ce test vérifie que la fonction affiche correctement un message lorsque la liste est vide.
"""
print("Test 1 : Affichage d'une liste vide")
afficher_liste_vaccins([])  # On teste une liste sans élément

""" 
Test 2 : Liste avec un seul élément
Ce test vérifie que la fonction affiche correctement un seul objet VaccinData.
"""
print("Test 2 : Affichage d'une liste avec un élément")
liste1 = [VaccinData("07/02/2021", "AstraZeneca", 273600)]  # Création d'une liste avec un seul vaccin
afficher_liste_vaccins(liste1)  # Affichage de la liste

""" 
Test 3 : Liste avec plusieurs éléments
Ce test vérifie que la fonction affiche correctement plusieurs objets VaccinData dans une liste.
"""
print("Test 3 : Affichage d'une liste avec plusieurs éléments")
liste2 = [
    VaccinData("07/02/2021", "AstraZeneca", 273600),  # Premier vaccin
    VaccinData("14/02/2021", "Pfizer", 316800),       # Deuxième vaccin
    VaccinData("21/02/2021", "Moderna", 150000)       # Troisième vaccin
]
afficher_liste_vaccins(liste2)  # Affichage de la liste complète
