"""
Ce module contient les fonctions nécessaires pour gérer la sélection des cartes
par le joueur dans le jeu de mémoire humain.
"""

from verifier_carte_existe import verifier_carte_existe, message_erreur
from afficher_tapis import afficher_tapis

def afficher_toutes_cartes(tableau_cartes,cartes_choisies,choix):
    """
    Affiche toutes les cartes du plateau en les retournant toutes face visible 
    pendant un court instant, puis retourne la carte choisie par le joueur.

    Arguments:
        tableau_cartes (list): Plateau de jeu sous forme d'une matrice 4x13, 
                            où chaque élément est une liste [carte, visible].
        cartes_choisies (list): Liste des cartes déjà choisies par le joueur.
        choix (str): La carte choisie par le joueur, initialement 'T' si l'option 
                    tricher est sélectionnée.

    Return:
        str: La carte choisie par le joueur après avoir affiché toutes les cartes.
    """
    for i in range (4):
        for j in range (13):
            tableau_cartes[i][j][1]=True
    afficher_tapis(tableau_cartes)
    for i in range (4):
        for j in range (13):
            tableau_cartes[i][j][1]=False
    choix=faire_choir_carte(cartes_choisies,tableau_cartes)
    return choix


def faire_choir_carte(cartes_choisies,tableau_cartes):
    """
    Gère la sélection d'une carte par le joueur et vérifie si la carte choisie est valide.

    Cette fonction gère l'entrée de l'utilisateur pour sélectionner une carte et effectue 
    les vérifications nécessaires pour s'assurer que la carte existe et que l'entrée est correcte.
    Si l'utilisateur choisit 'T', toutes les cartes sont affichées temporairement.
    Si la carte choisie n'est pas valide, une erreur est affichée et l'utilisateur doit recommencer.

    Arguments:
        cartes_choisies (list): Liste des cartes déjà choisies par le joueur.
        tableau_cartes (list): Plateau de jeu sous forme d'une matrice 4x13, 
                                où chaque élément est une liste [carte, visible].

    Return:
        str: La carte choisie par le joueur.
    """
    #demander à l'utilisteur une lettre et un chiffre
    if len(cartes_choisies)==0:
        choix=input('Première carte :')
    elif len(cartes_choisies)==1:
        choix=input('Deuxième carte :')

    if choix=='T':
        #Afficher toutes les cartes
        choix=afficher_toutes_cartes(tableau_cartes,cartes_choisies,choix)

    elif choix!='T'and (choix=='Q' or verifier_carte_existe(tableau_cartes,choix)):
        #on retourne toutes les cartes au cas où on sort d'une triche
        for i in range (4):
            for j in range (13):
                tableau_cartes[i][j][1]=False
    else:
        while choix!='Q' and not verifier_carte_existe(tableau_cartes,choix):
            #Dire pourquoi il y a un problème
            message_erreur(tableau_cartes,choix)
            choix=faire_choir_carte(cartes_choisies,tableau_cartes)
    return choix
