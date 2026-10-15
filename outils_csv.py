"""
Auteur : G. Richomme
Création 13/02/2024, modifié 17/02/2025
Contenu : une fonction de lecture de fichiers csv
"""
import csv

def lecture_fichier_csv( nom_fichier, separateur, encodage, nb_lignes_entete ):
    """
    Rôle : la fonction retourne deux listes de listes
        - une première liste contenant les listes de valeurs des nb_lignes_entete
            lignes du fichier
        - une deuxième liste contenant les autres lignes du fichier
    Type des données :
        nom_fichier : chaîne de caractères
        separateur : chaîne de caractères
        encodage : chaîne de caractères
        nb_lignes_entete : entier
    Précondition :
        separateur est de longueur 1
        nom_fichier est le nom d'un fichier csv (avec suffixe et chemin)
            dont les séparateur et encodage correspondent aux paramètres
        le fichier contient nb_lignes_entete lignes d'en-tête
    Type du résultat : couple de listes de listes de chaîne de caractéres
    """
    fichier = open(nom_fichier,"r", encoding=encodage)
    cr = csv.reader(fichier,delimiter=separateur)

    entete = []
    donnees = []
    compteur = 0
    for ligne in cr:
        if compteur < nb_lignes_entete:
            entete.append( ligne )
        else:
            donnees.append( ligne )
        compteur += 1
    fichier.close()
    return (entete, donnees)

