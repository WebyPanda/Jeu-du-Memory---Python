def initialiser_le_tapis():
    """
    Initialise le plateau de jeu pour une partie de Memory avec un jeu de 52 cartes mélangées.

    Cette fonction crée un tableau de 4 lignes et 13 colonnes représentant les cartes du jeu.
    Chaque carte est représentée par sa valeur (A, 2, 3, ..., K) et son enseigne (Pique, coeur, Carreau, Trèfle).
    Les cartes sont mélangées aléatoirement et placées sur le tableau, où chaque carte est initialement face cachée.

    Le plateau de jeu est une matrice 4x13, où chaque élément est une liste contenant :
    - Le nom de la carte (ex. "A P" pour l'As de Pique).
    - Un booléen indiquant si la carte est visible (initialement False).

    Return:
        list: Le tableau de 4x13 représentant le plateau de jeu, chaque carte étant une liste 
              de deux éléments : [nom_de_carte, visible].
    """
    import random
    TEXTES_ENSEIGNES_COURTS = tuple('PCKT')
    TEXTES_VALEURS_COURTS = 'A23456789XVDR' 
    liste=[]
    for i in range(4):
        for j in range(13):
            liste.append(str(TEXTES_VALEURS_COURTS[j])+str(TEXTES_ENSEIGNES_COURTS[i]))
    x=0
    tableau_cartes=[[[None,False] for i in range(13)] for j in range(4)]
    for i in range(4):
        for j in range(13):
            if len(liste)>1:
                x=random.randint(0,len(liste)-1)
            else:
                x=0
            tableau_cartes[i][j][0]=liste[x]
            liste.pop(x)
    return tableau_cartes

