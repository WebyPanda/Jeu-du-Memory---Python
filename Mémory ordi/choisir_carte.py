from assertions import*
import random

def changer_état_cartes(tableau_cartes:list,cartes_choisies:list):
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

def chosir_carte_avec_mémoire(tableau_cartes,mémoire,cartes_choisies):
    '''
    L'ordinateur choisit une carte en fonction de la première carte choisie et de la mémoire. 
    Si cette carte forme une paire avec une carte en mémoire, l'ordinateur choisit la deuxième carte pour compléter la paire.

    Args:
        tableau_cartes (list): Le tableau représentant le tapis de jeu, utilisé pour accéder aux cartes.
        mémoire (list): La mémoire contenant les cartes mémorisées et leurs positions.
        cartes_choisies (list): La liste des cartes déjà choisies par l'ordinateur.

    Returns:
        None: La fonction modifie la liste des cartes choisies et l'état des cartes dans le tableau.
    '''
    for i in range(len(mémoire)):
        if dire_si_cartes_forment_paire(transformer_position_carte(cartes_choisies[0],tableau_cartes)[0],mémoire[i][0]):
            cartes_choisies.append(str(mémoire[i][1]))
            tableau_cartes[int(mémoire[i][1][1])-1]['ABCDEFGHIJKLM'.index(mémoire[i][1][0])][1]=True
    
def choisir_carte_dans_mémoire(tableau_cartes,mémoire,cartes_choisies):
    '''
    Si aucune carte n'a encore été choisie, mais que des paires peuvent être formées avec les cartes en mémoire,
    l'ordinateur choisit une carte parmi celles-ci.

    Args:
        tableau_cartes (list): Le tableau représentant le tapis de jeu, utilisé pour accéder aux cartes.
        mémoire (list): La mémoire contenant les cartes mémorisées et leurs positions.
        cartes_choisies (list): La liste des cartes déjà choisies par l'ordinateur.

    Returns:
        None: La fonction modifie la liste des cartes choisies et l'état des cartes dans le tableau.
    '''
    for i in range(len(mémoire)):
        for j in range(i+1,len(mémoire)):
            if dire_si_cartes_forment_paire(mémoire[i][0],mémoire[j][0]):
                cartes_choisies.append(mémoire[i][1])
                tableau_cartes[int(mémoire[i][1][1])-1]['ABCDEFGHIJKLM'.index(mémoire[i][1][0])][1]=True
    
def choisir_nouvelle_carte(tableau_cartes,mémoire,cartes_choisies,niveau_ordi):
    '''
    Si aucune paire ne peut être formée avec les cartes en mémoire, l'ordinateur choisit aléatoirement une carte parmi celles qui ne sont pas encore retournées.

    Args:
        tableau_cartes (list): Le tableau représentant le tapis de jeu, utilisé pour accéder aux cartes.
        mémoire (list): La mémoire contenant les cartes mémorisées et leurs positions.
        cartes_choisies (list): La liste des cartes déjà choisies par l'ordinateur.
        niveau_ordi (int): Le niveau de l'ordinateur, déterminant la capacité de mémorisation et de stratégie.

    Returns:
        None: La fonction modifie la liste des cartes choisies et l'état des cartes dans le tableau.
    '''
    #R4: Comment “Choisir une nouvelle carte”?
    choix=random.choice('ABCDEFGHIJKLM')+str(random.randint(1,4))
    while transformer_position_carte(choix,tableau_cartes)==None or transformer_position_carte(choix,tableau_cartes)[1]==True or carte_dans_mémoire(choix,mémoire):
        #R5: Comment “Choisir une lettre et un chiffre au hasard”?
        choix=random.choice('ABCDEFGHIJKLM')+str(random.randint(1,4))
    cartes_choisies.append(choix)
    mémoire.append((transformer_position_carte(choix,tableau_cartes)[0],choix))
    tableau_cartes[int(choix[1])-1]['ABCDEFGHIJKLM'.index(choix[0])][1]=True
    #R5: Comment “Gérer la place dans la mémoire”?
    while len(mémoire)>5*niveau_ordi:
        mémoire.pop(0)


def faire_choisir_carte(cartes_choisies:list,tableau_cartes:list,mémoire:list,niveau_ordi:int):
    '''
    Permet à un ordinateur de choisir une carte (ou une paire de cartes) en fonction de la mémoire et des règles établies. 
    Si une paire peut être formée avec des cartes en mémoire, elle est choisie. Sinon, l'ordinateur choisit aléatoirement.

    Args:
        cartes_choisies (list): La liste des cartes déjà choisies par l'ordinateur.
        tableau_cartes (list): Le tableau contenant les cartes à partir desquelles l'ordinateur choisit.
        mémoire (list): La mémoire contenant les cartes déjà mémorisées et leurs positions.
        niveau_ordi (int): Le niveau de l'ordinateur, influençant son comportement dans la mémoire.

    Returns:
        None
    '''
    #R3: Comment “Faire choisir une carte ” ?
    if cartes_choisies!=[] and former_paire_avec_mémoire(cartes_choisies[0],mémoire,tableau_cartes):
        chosir_carte_avec_mémoire(tableau_cartes,mémoire,cartes_choisies)
    elif cartes_choisies==[] and mémoire!=[] and former_paire_dans_mémoire(mémoire,tableau_cartes):
        choisir_carte_dans_mémoire(tableau_cartes,mémoire,cartes_choisies)
    else:
        choisir_nouvelle_carte(tableau_cartes,mémoire,cartes_choisies,niveau_ordi)