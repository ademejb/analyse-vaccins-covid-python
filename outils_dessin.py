"""
Création : Gwenaël Richomme, décembre 2015 pour cours algorithmique du semestre 2 de L1 MIASHS.
Modification : Gwenaël Richomme, décembre 2016 - simplification utilisation
Modification : Gwenaël Richomme, 22 janvier 2023 - adaptation documentation module TE24MI
Modification : Gwenaël Richomme, 31 décembre 2023 - affichage d'axes même si 0 n'appartient pas [xmin, xmax] et 0 n'appartient pas [ymin, ymax]
Contenu
Définition d'une fonction
dessine_courbes_brisees
permettant de dessiner
jusqu'à 3 courbes brisées, 1 rouge, 1 bleue, 1 verte.

Une courbe brisée est ici une liste de couples (x, y) représentant un point.
"""

"""
Conseil pédagogique :
Si vous cherchez à comprendre une partie du code
(la compréhension complète nécessite la compréhension de notions
non abordées cette année),vous pouvez :
- observer la vision Python des axes d'un graphique (origine en haut à gauche)
- essayer d'ajouter une quatrième courbe (dans une nouvelle couleur)
- observer que les appels où les paramètres (formels) sont nommés
- de remarquer le test
     if __name__ =='__main__':
qui permet de n'exécuter ce qui suit que si le programme exécuté est le présent module.
(Si on importe le contenu du module, la suite de ce if n'est pas exécutée)

Cette possibilité de sera pas utilisée dans le cadre du cours TE24MI :
    à la place, on écrira un programme de test pour chaque fonction développée

- observer en exécutant
    help("dessine_courbes_brisees")
que certaines fonctions n'apparaissent pas (il s'agit de fonctions développées
    pour un usage interne au module et qui ne sont pas prévues pour une utilisation externe)
"""

from tkinter import *

def __dessine_axes(can, can_height, can_width, bord, xmin, xmax, ymin, ymax):
    """
    Rôle : cette fonction interne permet de dessine des axes
    sur un Canvas de taille can_height X can_width
    les axes vont de xmin à xmax et de ymin à ymax
    un cadre de bord points tout autour du graphique est prévu
    Données :
       can : Canvas
       can_height, can_width, bord, xmin, xmax, ymin, ymax : entiers non nuls
    """    
    # calcul des positions réelles des extrémités des axes
    pos_xmin = bord
    pos_xmax = can_width - bord
    pos_ymin = can_height - bord
    pos_ymax = bord
    longueur_x = pos_xmax-pos_xmin
    longueur_y = pos_ymin-pos_ymax
    # axe des y
    if (xmin <= 0) and (0 <= xmax): # on affiche l'axe en position 0
        pos_x0 = int(bord+((0-xmin) / (xmax-xmin))*longueur_x)
        val_x0 = 0
    else: # on affiche l'axe en position xmin
        pos_x0 = pos_xmin + int(longueur_x*0.05)
        val_x0 = xmin + int((xmax-xmin)*0.05)
    can.create_line(pos_x0, pos_ymin, pos_x0, pos_ymax) # trait de l'axe
    can.create_line(pos_x0-5, pos_ymax+10, pos_x0, pos_ymax) # trait flèche gauche
    can.create_line(pos_x0+5, pos_ymax+10, pos_x0, pos_ymax) # trait flèche droite
    can.create_text(pos_x0-1, pos_ymin, text=str(ymin), anchor=W) # étiquette ymin
    can.create_text(pos_x0-1, pos_ymax,text=str(ymax), anchor=W) # étiquette ymax
        

    # axe des x
    if (ymin <= 0) and (0 <= ymax):
        pos_y0 = pos_ymin - int(((0-ymin) / (ymax-ymin))*longueur_y)
        val_y0 = 0
    else:
        pos_y0 = pos_ymin - int(longueur_y*0.05)
        val_y0 = ymin+int((ymax-ymin)*0.05)
    can.create_line(pos_xmin, pos_y0, pos_xmax, pos_y0)
    can.create_line(pos_xmax-10, pos_y0-5, pos_xmax, pos_y0)
    can.create_line(pos_xmax-10, pos_y0+5, pos_xmax, pos_y0)
    can.create_text(pos_xmin, pos_y0-8, text=str(xmin), anchor=CENTER)
    can.create_text(pos_xmax, pos_y0-8, text=str(xmax), anchor=CENTER)

    can.create_text(pos_x0, pos_y0-8, text=str(val_x0), anchor=CENTER)
    can.create_text(pos_x0, pos_y0,text=str(val_y0), anchor=NW) 

def __dessine_ligne_brisee(can, can_height, can_width, bord,
                         xmin, xmax, ymin, ymax, 
                         liste_points, couleur='black'):
    """
    Rôle : dessine la ligne brisée désignée par liste_points
           dans le canevas can
           dont les caractéristiques sont rappelés en paramètres (dimensions, positions).
           La couleur de la courbe peut être précisée.
           Un changement d'échelle est effectué pour que toute la courbe apparaisse
             dans le canvas.
    Données : 
       can : Canvas
       can_height, can_width, bord, xmin, xmax, ymin, ymax : entiers non nuls
       liste_points : liste de couples d'entiers
       couleur : chaîne contenant un nom de couleur
    """
    pos_xmin = bord
    pos_xmax = can_width - bord
    pos_ymin = can_height - bord
    pos_ymax = bord
    longueur_x = pos_xmax-pos_xmin
    longueur_y = pos_ymin-pos_ymax
    # Recalcule de la liste_points
    # - Pour create_line, une liste de n points est une liste de 2n entiers :
    # 1 entier sur 2 représentant une abscisse, la suivante représentant une ordonnée
    # - Les coordonnées des points pour create_line sont compris
    #    entre 0 et width pour l'axe des x
    #    et entre 0 et height pour l'axe des y
    # - Le point (0,0) pour create_line est (classiquement) le coin supérieur gauche
    #    si l'axe des x est orienté vers la gauche
    #    l'axe des y est orienté vers le bas (au lieu de traditionnellement vers le haut)
    new_liste = []
    for i in range(len(liste_points)):
        xi = liste_points[i][0]
        yi = liste_points[i][1]
        new_xi = int(bord+((xi-xmin) / (xmax-xmin))*longueur_x)
        new_yi = pos_ymin - int(((yi-ymin) / (ymax-ymin))*longueur_y)
        new_liste += [new_xi, new_yi]
    can.create_line( new_liste, fill=couleur)

def dessine_lignes_brisees( courbe_rouge = [], courbe_bleue = [], courbe_verte = [],
                            height=600, width=600):
    """
    La fonction dessine_courbes_brisees dessine sur un Canvas
        de taille height par width.
    Les courbes en paramètres sont des listes de points (x, y).
    Les couleurs des courbes sont précisées dans les noms de paramètre.
    Données
	courbe_rouge : listes de couples d’entiers
	courbe_bleu : listes de couples d’entiers
	courbe_verte : listes de couples d’entiers
	height, width : entier
    Pas de résultat (uniquement affichage)
    """
    couleur_courbe_rouge = 'red'
    couleur_courbe_bleue = 'blue'
    couleur_courbe_verte = 'dark green'
    
    abscisses = [i for (i, _) in courbe_rouge + courbe_bleue + courbe_verte]
    xmin = min(abscisses)
    xmax = max(abscisses)
    ordonnees = [i for (_, i) in courbe_rouge + courbe_bleue + courbe_verte]
    ymin = min(ordonnees)
    ymax = max(ordonnees)


    bord = 20 # espace nécessaire pour mettre les étiquettes le long des axes
    fen = Tk() # Définition d'une fenêtre Tkinter
    can = Canvas( fen, height = height, width = width, bd = 0, bg='light grey')
        # Création de la toile (Canvas) de dessin
    can.pack(side=LEFT) #placement de la toile dans la fenêtre
    __dessine_axes(can, can_height = height, can_width = width,
                 bord = bord, xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax)
    # dessin de la première ligne
    if len(courbe_rouge) != 0:
        __dessine_ligne_brisee(can, can_height = height, can_width = width,
                         bord = bord,xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax,
                         liste_points=courbe_rouge, couleur = couleur_courbe_rouge)
    # dessin de la deuxième ligne
    if len(courbe_bleue) != 0:
        __dessine_ligne_brisee(can, can_height = height, can_width = width,
                         bord = bord,xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax,
                         liste_points=courbe_bleue, couleur = couleur_courbe_bleue)
    # dessin de la deuxième ligne
    if len(courbe_verte) != 0:
        __dessine_ligne_brisee(can, can_height = height, can_width = width,
                         bord = bord,xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax,
                         liste_points=courbe_verte, couleur = couleur_courbe_verte)
    #Autres couleurs possibles si besoin d'ajouter des courbes :
    #   green, purple, yellow, white, grey (sur grey ?), pink, orange
    fen.mainloop()

if __name__ =='__main__':
    # exemple d'appel local
    courbe = [(-100, -200), (-50,0), (0, 100), (100, -100), (300, 100)]
    courbe2 = [(-100, 50), (-50, 100), (0, 10), (50, 50), (100, -10), (300, 100)]
    courbe3 = [(-100, -50), (-50, -100), (0, -10), (50, -50), (100, 10), (300, -100)]
    dessine_lignes_brisees( courbe_rouge = courbe,
                            courbe_bleue = courbe2,
                            courbe_verte = courbe3,
                            height = 700, width = 1000 )
