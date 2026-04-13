from assertions import*

def retirer_cartes(carte1:str,carte2:str,tableau_cartes:list):
    '''
    Retire les cartes qui forment une paire du tableau de cartes (tapis).

    Args:
        carte1 (str): La position de la première carte à retirer (ex: 'A1').
        carte2 (str): La position de la deuxième carte à retirer (ex: 'B3').
        tableau_cartes (list): Le tableau de cartes représentant le tapis de jeu.

    Returns:
        None
    '''
    #R3: Comment “Enlever les cartes ” ?
    abscisse='ABCDEFGHIJKLM'
    tableau_cartes[int(carte1[1])-1][abscisse.index(carte1[0])]=None
    tableau_cartes[int(carte2[1])-1][abscisse.index(carte2[0])]=None

def retourner_cartes(tableau_cartes:list):
    '''
    Retourne toutes les cartes du tableau (celles qui ont été retournées) pour les cacher à nouveau.

    Args:
        tableau_cartes (list): Le tableau de cartes représentant le tapis de jeu.

    Returns:
        list: Une liste vide, représentant le fait que les cartes ont été retournées.
    '''
    #R3: Comment “Retourner les cartes ” ?
    for j in range(4):
        for i in range(13):
            if tableau_cartes[j][i]!=None:
                tableau_cartes[j][i][1]=False
    return []

def vérifier_paire(tableau_cartes:list,cartes_choisies:list,mémoire:list):
    '''
    Vérifie si les deux cartes choisies forment une paire. Si c'est le cas, elles sont retirées du tableau et supprimées de la mémoire. 
    Sinon, les cartes sont retournées.

    Args:
        tableau_cartes (list): Le tableau de cartes représentant le tapis de jeu.
        cartes_choisies (list): Une liste contenant les positions des cartes choisies (ex: ['A1', 'B2']).
        mémoire (list): La mémoire contenant les cartes déjà mémorisées et leurs positions.

    Returns:
        None
    ''' 
    #R2: Comment  “ Vérifier cette paire ” ?
    carte1, carte2 = transformer_position_carte(cartes_choisies[0],tableau_cartes)[0], transformer_position_carte(cartes_choisies[1],tableau_cartes)[0]
    if dire_si_cartes_forment_paire(carte1, carte2):
        retirer_cartes(cartes_choisies[0], cartes_choisies[1],tableau_cartes)
        for j in range(2):
            indice=None
            for i in range(len(mémoire)):
                    if mémoire[i][1]==cartes_choisies[0] or mémoire[i][1]==cartes_choisies[1]:
                        indice=i
            if indice!=None:
                mémoire.pop(indice)
        print('Bravo !')
    else:
        cartes_choisies=retourner_cartes(tableau_cartes)
        print('Pas de paire.')