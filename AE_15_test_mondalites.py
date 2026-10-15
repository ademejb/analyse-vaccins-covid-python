"""
Ce fichier teste la fonction modalites_doses du module AE_02_listes_type.
La fonction extrait les différentes valeurs de nb_doses d'une liste triée,
en supprimant les doublons successifs.
"""

from AE_02_listes_type import VaccinData, modalites_doses

print("===== TEST MODALITÉS DU CHAMP nb_doses =====\n")

"""
Test 1 : Liste avec des valeurs répétées (doublons)
Les doses sont : 5, 5, 10, 10, 15, 15
Modalités attendues : [5, 10, 15]
"""
liste1 = [
    VaccinData("2021-01-01", "Pfizer", 5),
    VaccinData("2021-01-01", "Pfizer", 5),
    VaccinData("2021-01-01", "Pfizer", 10),
    VaccinData("2021-01-01", "Pfizer", 10),
    VaccinData("2021-01-01", "Pfizer", 15),
    VaccinData("2021-01-01", "Pfizer", 15)
]
print("Test 1 (attendu : [5, 10, 15])")
print("Résultat :", modalites_doses(liste1), "\n")

"""
Test 2 : Liste triée avec des valeurs toutes différentes
Les doses sont : 100, 200, 300
Modalités attendues : [100, 200, 300]
"""
liste2 = [
    VaccinData("2021-01-01", "Moderna", 100),
    VaccinData("2021-01-01", "Moderna", 200),
    VaccinData("2021-01-01", "Moderna", 300)
]
print("Test 2 (attendu : [100, 200, 300])")
print("Résultat :", modalites_doses(liste2), "\n")

"""
Test 3 : Liste avec toutes les valeurs identiques
Les doses sont : 77, 77, 77
Modalité attendue : [77]
"""
liste3 = [
    VaccinData("2021-01-01", "AstraZeneca", 77),
    VaccinData("2021-01-01", "AstraZeneca", 77),
    VaccinData("2021-01-01", "AstraZeneca", 77)
]
print("Test 3 (attendu : [77])")
print("Résultat :", modalites_doses(liste3), "\n")

"""
Test 4 : Liste vide
Aucune modalité possible.
Modalité attendue : []
"""
liste4 = []
print("Test 4 (attendu : [])")
print("Résultat :", modalites_doses(liste4), "\n")
