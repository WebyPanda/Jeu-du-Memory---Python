def verifier_carte_existe(tableau_cartes,choix):
    """
    Vérifie si une carte choisie est valide.
    Arguments:
        tableau_cartes (list): Plateau de jeu contenant les cartes et leur état.
        choix (str): Coordonnée de la carte choisie (ex. "A1").
    Return:
        bool: True si la carte existe et est jouable, sinon False.
    """
    abscisse='ABCDEFGHIJKLM'
    if len(choix) != 2:
        resultat=False
    elif choix[0] not in 'ABCDEFGHIJKLM':
        resultat=False
    elif not(choix[1].isdigit()):
        resultat=False
    elif choix[1].isdigit() and (int(choix[1])>4 or int(choix[1])<1):
        resultat=False
    elif tableau_cartes[int(choix[1])-1][abscisse.index(choix[0])][0]==None:
        resultat=False
    elif tableau_cartes[int(choix[1])-1][abscisse.index(choix[0])][1]:
        resultat=False
    else:
        resultat=True
    return resultat


def message_erreur(tableau_cartes,choix):
    """
    Affiche un message d'erreur détaillé si la carte choisie est invalide.
    Arguments:
        tableau_cartes (list): Plateau de jeu contenant les cartes et leur état.
        choix (str): Coordonnée de la carte choisie (ex. "A1").
    Return:
        None: La fonction affiche un message d'erreur, mais ne renvoie rien.
    """
    abscisse='ABCDEFGHIJKLM'
    if len(choix) != 2:
        print('erreur sur la carte :',choix,'. La carte doit être composée d\'une lettre et d\'un chiffre !')
    elif choix[0] not in 'ABCDEFGHIJKLM':
        print('erreur sur la colone :',choix[0],'. La lettre doit être entre A et M !')
    elif not(choix[1].isdigit()):
        print('erreur sur la ligne :',choix[1],'. Le chiffre doit être entre 1 et 4 !')
    elif choix[1].isdigit() and (int(choix[1])>4 or int(choix[1])<1):
        print('erreur sur la ligne :',int(choix[1]),'. Le chiffre doit être entre 1 et 4 !')
    elif tableau_cartes[int(choix[1])-1][abscisse.index(choix[0])][0]==None:
        print('erreur sur la carte :',choix,'. La carte est déjà enlevée !')
    elif tableau_cartes[int(choix[1])-1][abscisse.index(choix[0])][1]:
        print('erreur sur la carte :',choix,'. La carte est déjà retournée !')
