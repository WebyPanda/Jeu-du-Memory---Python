def rester_paire(tableau_cartes):
    """
    Vérifie s'il reste des cartes disponibles pour former des paires.
    Arguments:
        tableau_cartes (list): Plateau de jeu contenant les cartes et leur état. 
            Chaque carte est représentée par une liste où l'élément `cartes[0]` 
            est None si la carte a été retirée.
    Return:
        bool: True s'il reste des cartes disponibles, sinon False.
    """
    paires=False
    for lignes in tableau_cartes:
        for cartes in lignes:
            if cartes[0]!=None:
                paires=True
    return paires