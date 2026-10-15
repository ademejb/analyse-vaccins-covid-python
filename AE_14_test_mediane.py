"""
Ce fichier teste la fonction mediane_doses_triee du module AE_02_listes_type.
Il couvre plusieurs cas : 
- liste triée avec un nombre impair d'éléments
- liste triée avec un nombre pair d'éléments
- liste avec un seul élément
- liste vide
"""

from AE_02_listes_type import VaccinData, mediane_doses_triee

print("===== TEST MEDIANE =====")

"""
Test 1 : Liste triée avec un nombre impair d'éléments (3 éléments)
Les doses sont : 10, 20, 30 → médiane attendue = 20
"""
liste_1 = [
    VaccinData("2021-01-01", "Pfizer", 10),
    VaccinData("2021-01-01", "Pfizer", 20),
    VaccinData("2021-01-01", "Pfizer", 30)
]
print("Test 1 (impair, attendue = 20) : ", mediane_doses_triee(liste_1))

"""
Test 2 : Liste triée avec un nombre pair d'éléments (4 éléments)
Les doses sont : 10, 20, 30, 40 → médiane attendue = (20 + 30) / 2 = 25
"""
liste_2 = [
    VaccinData("2021-01-01", "Moderna", 10),
    VaccinData("2021-01-01", "Moderna", 20),
    VaccinData("2021-01-01", "Moderna", 30),
    VaccinData("2021-01-01", "Moderna", 40)
]
print("Test 2 (pair, attendue = 25) : ", mediane_doses_triee(liste_2))

"""
Test 3 : Liste contenant un seul élément
La médiane est la valeur unique présente → attendue = 15
"""
liste_3 = [
    VaccinData("2021-01-01", "AstraZeneca", 15)
]
print("Test 3 (1 seul élément, attendue = 15) : ", mediane_doses_triee(liste_3))

"""
Test 4 : Liste vide
Pas de médiane possible → résultat attendu : None
"""
liste_4 = []
print("Test 4 (liste vide, attendue = None) : ", mediane_doses_triee(liste_4))
