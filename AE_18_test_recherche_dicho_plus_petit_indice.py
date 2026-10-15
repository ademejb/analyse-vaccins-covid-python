
"""
Ce fichier teste la fonction recherche_dicho_plus_petit_indice du module AE_02_listes_type.
Cette fonction retourne l’indice le plus petit d’une valeur présente dans une liste triée selon nb_doses.
Si la valeur est absente, elle retourne -1.
"""

from AE_02_listes_type import VaccinData, recherche_dicho_plus_petit_indice

"""
Liste triée selon le champ nb_doses : [10, 20, 20, 30]
Utilisée pour les différents cas de recherche.
"""
liste = [
    VaccinData("01/01/2021", "Pfizer", 10),
    VaccinData("02/01/2021", "Moderna", 20),
    VaccinData("03/01/2021", "AstraZeneca", 20),
    VaccinData("04/01/2021", "Janssen", 30),
]

"""
Test 1 : valeur présente une seule fois (10)
Doit retourner l’indice 0.
"""
print("Test 1 (valeur présente une fois) :", recherche_dicho_plus_petit_indice(liste, 10))

"""
Test 2 : valeur présente plusieurs fois (20)
Doit retourner l’indice du premier (1).
"""
print("Test 2 (valeur présente plusieurs fois) :", recherche_dicho_plus_petit_indice(liste, 20))

"""
Test 3 : valeur absente (999)
Doit retourner -1 car la valeur n’est pas dans la liste.
"""
print("Test 3 (valeur absente) :", recherche_dicho_plus_petit_indice(liste, 999))
