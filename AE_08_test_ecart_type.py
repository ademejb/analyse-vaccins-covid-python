
"""
Ce fichier teste la fonction ecart_type_doses du module AE_02_listes_type.
Il vérifie que l'écart type est correctement calculé à partir d'une liste de vaccins.
"""

from AE_02_listes_type import ecart_type_doses, convertir_liste_csv_en_vaccins

"""
Création d'une liste de vaccins à partir de données CSV simulées.
Les doses sont : 10, 10, 10, 10, 95.
La moyenne est de 27.
L'écart type est censé refléter l'écart important causé par la valeur 95.
"""
liste_test = convertir_liste_csv_en_vaccins([
    ["01/01/2021", "Test", "0", "10"],
    ["02/01/2021", "Test", "0", "10"],
    ["03/01/2021", "Test", "0", "10"],
    ["04/01/2021", "Test", "0", "10"],
    ["05/01/2021", "Test", "0", "95"]
])

"""
Test de la fonction ecart_type_doses sur la liste créée.
Un écart type élevé est attendu à cause de la dernière valeur (95).
"""
print("Test écart-type :", ecart_type_doses(liste_test))

