
"""
Ce fichier propose un menu interactif pour manipuler des données de vaccination.
L'utilisateur peut :
1. Charger différents fichiers CSV
2. Filtrer par type de vaccin
3. Afficher des statistiques
4. Rechercher une valeur dans nb_doses
"""

from AE_02_listes_type import *
from outils_csv import *

"""
Initialisation d'une liste de données simulées (par défaut au lancement).
Chaque élément est un objet VaccinData.
"""
donnees_vaccins = [
    VaccinData("01/01/2021", "Pfizer", 549),
    VaccinData("01/01/2021", "Moderna", 1),
    VaccinData("01/01/2021", "AstraZeneca", 100),
    VaccinData("01/01/2021", "Janssen", 7),
    VaccinData("01/01/2021", "Pfizer", 77)
]

stopp = False
while not stopp:
    print("\nVoici la liste courante :")
    afficher_liste_vaccins(donnees_vaccins)

    menu = ("\nMenu :\n"
            "1 - Ouverture d'un fichier parmi une liste\n"
            "2 - Filtrage des données de la liste courante\n"
            "3 - Affichage d'indicateur statistique de la liste courante\n"
            "4 - Quitter\n"
            "5 - Rechercher le nombre d'occurrences d'une valeur dans nb_doses")
    print(menu)
    choix = input("Votre choix : ")

    if choix == "4":
        stopp = True  # Quitter le programme

    elif choix == "1":
        """
        Permet à l'utilisateur de choisir un fichier CSV à ouvrir.
        Le contenu du fichier remplace la liste courante de données.
        """
        print("Quel fichier voulez-vous ouvrir pour remplacer la liste courante ?")
        print("1 - Fichier avec 1 ligne de données")
        print("2 - Fichier avec 5 lignes de données")
        print("3 - Fichier avec 20 lignes de données")
        print("4 - Fichier avec 100 lignes de données")
        choix_fichier = input("Votre choix : ")

        if choix_fichier == "1":
            entete, donnees = lecture_fichier_csv("AE_donnee/AE_data_1.csv", ",", "latin-1", 1)
            donnees_vaccins = convertir_liste_csv_en_vaccins(donnees)
        elif choix_fichier == "2":
            entete, donnees = lecture_fichier_csv("AE_donnee/AE_data_5.csv", ",", "latin-1", 1)
            donnees_vaccins = convertir_liste_csv_en_vaccins(donnees)
        elif choix_fichier == "3":
            entete, donnees = lecture_fichier_csv("AE_donnee/AE_data_20.csv", ",", "latin-1", 1)
            donnees_vaccins = convertir_liste_csv_en_vaccins(donnees)
        elif choix_fichier == "4":
            entete, donnees = lecture_fichier_csv("AE_donnee/AE_data_100.csv", ",", "latin-1", 1)
            donnees_vaccins = convertir_liste_csv_en_vaccins(donnees)
        else:
            print("Choix invalide.")

    elif choix == "2":
        """
        Permet à l'utilisateur de filtrer la liste courante selon un type de vaccin choisi.
        """
        print("Vous pouvez filtrer vos données par type de vaccin.")
        type_vaccin_filtre = input("Entrez le type de vaccin à filtrer (ex: Pfizer) : ")
        donnees_vaccins = filtrer_par_type_vaccin(donnees_vaccins, type_vaccin_filtre)

    elif choix == "3":
        """
        Affiche des indicateurs statistiques calculés sur la liste actuelle :
        - minimum, maximum, moyenne, écart-type, médiane et modalités.
        """
        print("Indicateurs statistiques sur nb_doses :")
        if not donnees_vaccins:
            print("Liste vide, aucun calcul possible.")
        else:
            donnees_vaccins_tries = tri_selection_doses(donnees_vaccins.copy())
            print(" - Minimum :", min_doses(donnees_vaccins_tries))
            print(" - Maximum :", max_doses(donnees_vaccins_tries))
            print(" - Moyenne :", moyenne_doses(donnees_vaccins_tries))
            print(" - Écart type :", ecart_type_doses(donnees_vaccins_tries))
            print(" - Médiane :", mediane_doses_triee(donnees_vaccins_tries))
            print(" - Modalités :", modalites_doses(donnees_vaccins_tries))

    elif choix == "5":
        """
        Recherche le nombre d'occurrences d'une valeur saisie par l'utilisateur dans nb_doses.
        La liste est triée avant la recherche.
        """
        if not donnees_vaccins:
            print("Liste vide, impossible de faire une recherche.")
        else:
            try:
                valeur = int(input("Entrez une valeur numérique pour rechercher dans nb_doses : "))
                donnees_vaccins_tries = tri_selection_doses(donnees_vaccins.copy())
                nb = nb_occurrences_nb_doses(donnees_vaccins_tries, valeur)
                print(f"Il y a {nb} occurrence(s) de la valeur {valeur} dans nb_doses.")
            except ValueError:
                print("Erreur : veuillez entrer une valeur entière correcte.")
