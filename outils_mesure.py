"""
    Auteur : Gwenaël Richomme
    Date création : 3 janvier 2024
    Contenu : fonction outils pour les mesures
"""
import timeit

def temps_en_nanoseconde( temps ):
    """
    Retourne la valeur de temps en nombre entier de nanosecondes
    Donnée
        temps : float mesurant un temps en seconde
    Résultat : entier
    """
    return int(temps*10**9)

def mesure_temps( nb_mesures, instructions_a_mesurer,
                  instructions_initialisation, nb_repet):
    """
    Données
        nb_mesures : entier
        instructions_a_mesurer : chaîne des caractères
            Précondition : la chaîne contient une séquence valide d'instructions        instructions_a_mesurer : chaîne des caractères
        instructions_initialisaition : chaîne des caractères
            Précondition : la chaîne contient une séquence valide d'instructions
        nb_repet : entier
    Aucun résultat interne
    Rôle : realise nb_mesures fois l'appel 
            timeit.timeit(stmt=instructions_a_mesurer,
                          setup=instructions_initialisation,
                          number=nb_repet)
        et affiche le résultat en un nombre entier de nanosecondes.
        Affiche également le temps moyen des mesures
    """
    temps_total = 0
    for i in range(nb_mesures):
        temps = timeit.timeit(stmt=instructions_a_mesurer,
                              setup=instructions_initialisation,
                              number=nb_repet)
        temps = temps_en_nanoseconde(temps/nb_repet)
        print("Mesure", (i+1),":", temps)
        temps_total += temps
    print("Temps moyen : ", temps_total/nb_mesures)
