
"""
Ce fichier teste la fonction max_doses du module AE_02_listes_type.
Il vérifie que la fonction renvoie correctement le nombre maximum de doses dans une liste de vaccins.
"""

from AE_02_listes_type import max_doses, convertir_liste_csv_en_vaccins

"""
Création d'une liste de vaccins à partir de données CSV simulées.
Chaque ligne contient une date, un type, un champ inutile, et un nombre de doses.
"""
liste_test = convertir_liste_csv_en_vaccins([
    ["01/01/2021", "Test", "0", "10"],
    ["02/01/2021", "Test", "0", "99"],
    ["03/01/2021", "Test", "0", "75"]
])

"""
Test de la fonction max_doses sur la liste créée.
Le résultat attendu est 99 (le plus grand nombre de doses).
"""
print("Test maximum :", max_doses(liste_test))
