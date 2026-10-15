#Fichier : AE_00_type.py
# Définition d'un nouveau type de données pour représenter les informations sur les vaccins

class VaccinData:
    def __init__(self, date, type_vaccin, nb_doses):
        """ Initialise une instance de VaccinData avec une date, un type de vaccin et un nombre de doses """
        self.date = date  # Date de fin de la semaine
        self.type_vaccin = type_vaccin  # Type de vaccin
        self.nb_doses = nb_doses  # Nombre total de doses

    def afficher(self):
        """ Affiche les informations sur le vaccin """
        print("Date:", self.date, "| Vaccin:", self.type_vaccin, "| Doses:", self.nb_doses)

