def initialiser_le_tapis():
    '''
    Initialise le tapis de jeu avec des cartes placées aléatoirement.

    Cette fonction crée un tableau de cartes (4 rangées de 13 cartes), chacune ayant une valeur et une enseigne. 
    Les cartes sont placées de manière aléatoire sur le tapis, avec des cartes du type Pioche (P), Coeur (C), Carreau (K), et Trèfle (T) et des valeurs de A à R.

    Args:
        Aucun argument.

    Returns:
        list: Un tableau représentant le tapis de jeu avec 4 rangées et 13 cartes par rangée, où chaque carte est un tableau de deux éléments :
              1. La carte sous forme de chaîne ('valeur'+'enseigne').
              2. Un booléen indiquant si la carte est retournée.

    Exemple:
        >>> tapis = initialiser_le_tapis()
        >>> len(tapis)
        4
        >>> len(tapis[0])
        13
    '''
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
