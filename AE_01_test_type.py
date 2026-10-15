# Fichier : AE_01_test_type.py
# Programme de test pour la classe VaccinData

from AE_00_type import VaccinData  # Importation de la classe

# Création de deux instances de VaccinData avec des données fictives
vaccin1 = VaccinData("07/02/2021", "AstraZeneca", 273600)
vaccin2 = VaccinData("14/02/2021", "AstraZeneca", 316800)

# Affichage des informations des deux instances créées
vaccin1.afficher()
vaccin2.afficher()
