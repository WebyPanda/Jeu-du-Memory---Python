def changer_état_cartes(tableau_cartes,cartes_choisies):
    '''
    Change l'état des cartes choisies dans le tableau de cartes en marquant celles-ci comme retournées (état = True).

    Args:
        tableau_cartes (list): Le tableau contenant les cartes.
        cartes_choisies (list): Une liste contenant les positions des cartes choisies (sous forme de chaînes comme 'A1', 'B2', etc.).

    Returns:
        None
    '''
    abscisse='ABCDEFGHIJKLM'
    for cartes in cartes_choisies:
        tableau_cartes[int(cartes[1])-1][abscisse.index(cartes[0])][1]=True