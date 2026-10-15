from AE_00_type import VaccinData
from math import sqrt

#AFFICHAGE 
def afficher_liste_vaccins(liste_vaccins):
    """
    Affiche les informations de chaque vaccin dans la liste.
    Si la liste est vide, affiche un message spécifique.
    """
    if not liste_vaccins:
        print("La liste est vide.")
    else:
        for vaccin in liste_vaccins:
            vaccin.afficher()

#TRANSFORMATION 
def convertir_liste_csv_en_vaccins(liste_csv):
    """
    Convertit une liste de lignes CSV en objets VaccinData.
    Ignore les lignes avec données insuffisantes ou erreurs de conversion.
    
    Paramètre :
        liste_csv : liste de listes représentant les lignes du fichier CSV
    Retour :
        liste de VaccinData
    """
    liste_vaccins = []
    for ligne in liste_csv:
        if len(ligne) >= 4:
            try:
                date = ligne[0]
                type_vaccin = ligne[1]
                nb_doses = int(ligne[3])
                liste_vaccins.append(VaccinData(date, type_vaccin, nb_doses))
            except ValueError:
                print("Erreur de conversion pour la ligne :", ligne)
    return liste_vaccins

#STATS
def min_doses(liste):
    """
    Retourne le nombre minimum de doses parmi les vaccins de la liste.
    """
    return min(v.nb_doses for v in liste)

def max_doses(liste):
    """
    Retourne le nombre maximum de doses parmi les vaccins de la liste.
    """
    return max(v.nb_doses for v in liste)

def moyenne_doses(liste):
    """
    Calcule la moyenne du nombre de doses dans la liste.
    """
    return sum(v.nb_doses for v in liste) / len(liste)

def ecart_type_doses(liste):
    """
    Calcule l'écart type du nombre de doses dans la liste.
    
    Utilise la formule classique avec la moyenne.
    """
    m = moyenne_doses(liste)
    return sqrt(sum((v.nb_doses - m)**2 for v in liste) / len(liste))

#MEDIANE et MODALITES
def mediane_doses_triee(liste):
    """
    Calcule la médiane des doses (liste supposée triée).
    
    Retour :
        La valeur médiane ou None si la liste est vide.
    """
    n = len(liste)
    if n == 0:
        return None
    if n % 2 == 0:
        return (liste[n // 2 - 1].nb_doses + liste[n // 2].nb_doses) / 2
    else:
        return liste[n // 2].nb_doses

def modalites_doses(liste):
    """
    Renvoie la liste des différentes valeurs de doses (modalités) présentes.
    Supposé que la liste est triée par nb_doses.
    """
    if not liste:
        return []
    modalites = [liste[0].nb_doses]
    for i in range(1, len(liste)):
        if liste[i].nb_doses != liste[i - 1].nb_doses:
            modalites.append(liste[i].nb_doses)
    return modalites

#FILTRAGE
def filtrer_par_type_vaccin(liste, type_recherche):
    """
    Filtre les vaccins selon leur type.
    
    Paramètres :
        liste : liste de VaccinData
        type_recherche : chaîne représentant le type de vaccin recherché
    Retour :
        Liste des vaccins correspondant au type
    """
    return [v for v in liste if v.type_vaccin == type_recherche]

#TRI
def tri_selection_doses(liste):
    """
    Trie la liste de vaccins par nb_doses en utilisant le tri par sélection.
    
    Retour :
        La liste triée (en place).
    """
    n = len(liste)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if liste[j].nb_doses < liste[min_index].nb_doses:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

#TEST TRIÉ
def est_triee_par_doses(liste):
    """
    Vérifie si la liste est triée en ordre croissant selon nb_doses.
    
    Retour :
        True si triée, False sinon.
    """
    return all(liste[i].nb_doses <= liste[i+1].nb_doses for i in range(len(liste)-1))

# ----------RECHERCHES DICHOTOMIQUES
def recherche_dicho_quelconque(liste, valeur):
    """
    Recherche dichotomique d'une valeur dans une liste triée selon nb_doses.
    Retourne un indice quelconque ou -1 si absent.
    Complexité : O(log n)
    """
    g = 0
    d = len(liste) - 1
    while g <= d:
        m = (g + d) // 2
        if liste[m].nb_doses == valeur:
            return m
        elif liste[m].nb_doses < valeur:
            g = m + 1
        else:
            d = m - 1
    return -1

def recherche_dicho_plus_petit_indice(liste, valeur):
    """
    Recherche l'indice le plus petit (première occurrence) d'une valeur donnée.
    
    Retour :
        Indice trouvé ou -1 si absent.
    """
    g, d = 0, len(liste) - 1
    res = -1
    while g <= d:
        m = (g + d) // 2
        if liste[m].nb_doses == valeur:
            res = m
            d = m - 1
        elif liste[m].nb_doses < valeur:
            g = m + 1
        else:
            d = m - 1
    return res

def recherche_dicho_plus_grand_indice(liste, valeur):
    """
    Recherche l'indice le plus grand (dernière occurrence) d'une valeur donnée.
    
    Retour :
        Indice trouvé ou -1 si absent.
    """
    g, d = 0, len(liste) - 1
    res = -1
    while g <= d:
        m = (g + d) // 2
        if liste[m].nb_doses == valeur:
            res = m
            g = m + 1
        elif liste[m].nb_doses < valeur:
            g = m + 1
        else:
            d = m - 1
    return res

def nombres_occurrences(liste, valeur):
    """
    Compte le nombre d'occurrences d'une valeur (nb_doses) dans une liste triée.
    
    Retour :
        Nombre d’occurrences (entier).
    """
    min_i = recherche_dicho_plus_petit_indice(liste, valeur)
    if min_i == -1:
        return 0
    max_i = recherche_dicho_plus_grand_indice(liste, valeur)
    return max_i - min_i + 1
