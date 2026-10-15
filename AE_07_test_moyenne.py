
"""
Ce fichier teste la fonction moyenne_doses du module AE_02_listes_type.
Il vérifie que la fonction calcule correctement la moyenne du nombre de doses dans une liste de vaccins.
"""

from AE_02_listes_type import moyenne_doses, convertir_liste_csv_en_vaccins

"""
Création d'une liste de vaccins à partir de données CSV simulées.
Les doses sont : 10, 20 et 30.
"""
liste_test = convertir_liste_csv_en_vaccins([
    ["01/01/2021", "Test", "0", "10"],
    ["02/01/2021", "Test", "0", "20"],
    ["03/01/2021", "Test", "0", "30"]
])

"""
Test de la fonction moyenne_doses sur la liste créée.
La moyenne attendue est : (10 + 20 + 30) / 3 = 20.0
"""
print("Test moyenne :", moyenne_doses(liste_test))

