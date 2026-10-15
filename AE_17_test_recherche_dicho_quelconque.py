
"""
Ce fichier teste la fonction recherche_dicho_quelconque du module AE_02_listes_type.
La liste utilisée doit être triée par nb_doses pour que la recherche soit correcte.
La fonction retourne un indice quelconque correspondant à la valeur cherchée,
ou -1 si elle est absente.
"""

from AE_02_listes_type import VaccinData, recherche_dicho_quelconque

"""
Liste triée selon le champ nb_doses : [10, 20, 20, 30]
Utilisée pour les 3 tests suivants.
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
print("Test 1 (valeur présente une fois) :", recherche_dicho_quelconque(liste, 10))

"""
Test 2 : valeur présente plusieurs fois (20)
Peut retourner 1 ou 2 (n’importe lequel des deux).
"""
print("Test 2 (valeur présente plusieurs fois) :", recherche_dicho_quelconque(liste, 20))

"""
Test 3 : valeur absente (999)
Doit retourner -1.
"""
print("Test 3 (valeur absente) :", recherche_dicho_quelconque(liste, 999))
