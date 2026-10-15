
"""
Ce fichier teste la fonction filtrer_par_type_vaccin du module AE_02_listes_type.
Il vérifie que seuls les vaccins correspondant au type spécifié (ici "Pfizer") sont conservés.
"""

from AE_02_listes_type import convertir_liste_csv_en_vaccins, filtrer_par_type_vaccin, afficher_liste_vaccins

"""
Données de test contenant différents types de vaccins.
Chaque sous-liste correspond à une ligne de données CSV simulée.
"""
donnees_test = [
    ["01/01/2021", "Pfizer", "0", "100"],
    ["02/01/2021", "Moderna", "0", "200"],
    ["03/01/2021", "Pfizer", "0", "300"],
    ["04/01/2021", "Janssen", "0", "400"],
    ["05/01/2021", "Pfizer", "0", "500"]
]

"""
Conversion des données CSV en objets VaccinData.
"""
liste_vaccins = convertir_liste_csv_en_vaccins(donnees_test)

"""
Application du filtrage : on sélectionne uniquement les vaccins de type 'Pfizer'.
"""
liste_filtrée = filtrer_par_type_vaccin(liste_vaccins, "Pfizer")

"""
Affichage du résultat : seuls les vaccins de type 'Pfizer' doivent être affichés.
"""
print("Vaccins filtrés de type 'Pfizer' :")
afficher_liste_vaccins(liste_filtrée)
