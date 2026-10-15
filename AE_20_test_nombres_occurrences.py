
"""
Ce fichier teste la fonction nombres_occurrences du module AE_02_listes_type.
Cette fonction retourne le nombre total d'occurrences d'une valeur donnée
dans une liste triée selon le champ nb_doses.
"""

from AE_02_listes_type import VaccinData, nombres_occurrences

"""
Liste triée selon le champ nb_doses : [10, 20, 20, 30]
Contient des cas avec valeur unique, doublons, et une valeur absente.
"""
liste = [
    VaccinData("01/01/2021", "Pfizer", 10),
    VaccinData("02/01/2021", "Moderna", 20),
    VaccinData("03/01/2021", "AstraZeneca", 20),
    VaccinData("04/01/2021", "Janssen", 30),
]

"""
Test 1 : valeur présente une seule fois (10)
Résultat attendu : 1
"""
print("Test 1 (valeur présente une fois) :", nombres_occurrences(liste, 10))

"""
Test 2 : valeur présente plusieurs fois (20)
Résultat attendu : 2
"""
print("Test 2 (valeur présente plusieurs fois) :", nombres_occurrences(liste, 20))

"""
Test 3 : valeur absente (999)
Résultat attendu : 0
"""
print("Test 3 (valeur absente) :", nombres_occurrences(liste, 999))
