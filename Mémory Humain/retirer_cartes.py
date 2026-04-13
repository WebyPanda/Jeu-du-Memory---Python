def retirer_cartes(carte1,carte2,tableau_cartes):
    """
    Retire deux cartes du tapis.
    Prend en entrée deux cartes formant une paire et les retire du plateau de jeu.
    Arguments:
        carte1 (str): Première carte à retirer, sous la forme "A1".
        carte2 (str): Deuxième carte à retirer, sous la forme "B2".
        tableau_cartes (list): Plateau de jeu contenant les cartes à mettre à jour.
    Return:
        None
    """
    abscisse='ABCDEFGHIJKLM'
    tableau_cartes[int(carte1[1])-1][abscisse.index(carte1[0])][0]=None
    tableau_cartes[int(carte2[1])-1][abscisse.index(carte2[0])][0]=None