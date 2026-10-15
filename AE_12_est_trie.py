
"""
Ce fichier teste la fonction est_triee_par_doses du module AE_02_listes_type.
Il vérifie si les listes de vaccins sont bien triées selon nb_doses.
Différents cas sont examinés : liste triée, non triée, un seul élément, vide.
"""

from AE_02_listes_type import *

"""
Liste triée : les doses sont en ordre croissant (10, 20, 30).
Résultat attendu : True
"""
liste1 = [
    VaccinData("01/01/2021", "Pfizer", 10),
    VaccinData("01/01/2021", "Moderna", 20),
    VaccinData("01/01/2021", "AstraZeneca", 30)
]

"""
Liste non triée : l'ordre des doses est irrégulier (50, 20, 40).
Résultat attendu : False
"""
liste2 = [
    VaccinData("01/01/2021", "Pfizer", 50),
    VaccinData("01/01/2021", "Moderna", 20),
    VaccinData("01/01/2021", "AstraZeneca", 40)
]

"""
Liste avec un seul élément : considérée comme triée.
Résultat attendu : True
"""
liste3 = [
    VaccinData("01/01/2021", "Pfizer", 100)
]

"""
Liste vide : une liste vide est considérée comme triée.
Résultat attendu : True
"""
liste4 = []

# Affichage des résultats de test
print("Test 1 - Liste triée :", est_triee_par_doses(liste1))      # True
print("Test 2 - Liste non triée :", est_triee_par_doses(liste2))  # False
print("Test 3 - Liste un élément :", est_triee_par_doses(liste3)) # True
print("Test 4 - Liste vide :", est_triee_par_doses(liste4))       # True
