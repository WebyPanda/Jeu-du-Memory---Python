def retirer_cartes(carte1,carte2,tableau_cartes):
    '''
    Retire les cartes qui forment une paire du tableau de cartes (tapis).

    Args:
        carte1 (str): La position de la première carte à retirer (ex: 'A1').
        carte2 (str): La position de la deuxième carte à retirer (ex: 'B3').
        tableau_cartes (list): Le tableau de cartes représentant le tapis de jeu.

    Returns:
        None
    '''
    abscisse='ABCDEFGHIJKLM'
    tableau_cartes[int(carte1[1])-1][abscisse.index(carte1[0])]=None
    tableau_cartes[int(carte2[1])-1][abscisse.index(carte2[0])]=None