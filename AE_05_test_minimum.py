
"""
Ce fichier teste la fonction min_doses du module AE_02_listes_type.
Il vérifie que la fonction renvoie correctement le minimum de doses parmi une liste de vaccins.
"""

from AE_02_listes_type import min_doses, convertir_liste_csv_en_vaccins

"""
Création d'une liste de vaccins à partir de données CSV simulées.
Chaque ligne contient une date, un type, un champ vide (inutile ici), et un nombre de doses.
"""
liste_test = convertir_liste_csv_en_vaccins([
    ["01/01/2021", "Test", "0", "10"],
    ["02/01/2021", "Test", "0", "20"],
    ["03/01/2021", "Test", "0", "5"]
])

"""
Test de la fonction min_doses sur la liste créée.
Le résultat attendu est 5 (le plus petit nombre de doses).
"""
print("Test minimum :", min_doses(liste_test))


