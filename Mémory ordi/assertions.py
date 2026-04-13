def rester_des_paires(tableau_cartes:list):
    '''
    Vérifie s'il reste des cartes dans le jeu.

    Args:
        tableau_cartes (list): Un tableau de cartes à vérifier.

    Returns:
        bool: True si des cartes existent dans le tableau, False sinon.
    '''
    paires=False
    for lignes in tableau_cartes:
        for cartes in lignes:
            if cartes!=None:
                paires=True
    return paires

def dire_si_cartes_forment_paire(carte1:str, carte2:str):
    '''
    Vérifie si deux cartes forment une paire, en fonction de leur valeur et de leur couleur.

    Args:
        carte1 (str): La première carte à comparer, sous forme de chaîne: 'valeur'+'enseigne'.
        carte2 (str): La première carte à comparer, sous forme de chaîne: 'valeur'+'enseigne'.

    Returns:
        bool: True si les deux cartes forment une paire, False sinon.
    '''
    #R3: Comment “Dire si les cartes forment une paire ” ?
    TEXTES_VALEURS_COURTS = list('A23456789XVDR')
    TEXTES_ENSEIGNES_COURTS = list('PCKT')
    Couleurs=['Noir','Rouge','Rouge','Noir']
    résultat=False
    if carte1!=carte2 and Couleurs[TEXTES_ENSEIGNES_COURTS.index(carte1[1])]==Couleurs[TEXTES_ENSEIGNES_COURTS.index(carte2[1])]:
        if TEXTES_VALEURS_COURTS.index(carte1[0])==TEXTES_VALEURS_COURTS.index(carte2[0]):
            résultat=True
    return résultat

def former_paire_dans_mémoire(mémoire:list,tableau_cartes:list):
    '''
    Vérifie si des cartes dans la mémoire forment une paire.

    Args:
        mémoire (list): La mémoire contenant les cartes mémorisées.
        tableau_cartes (list): Le tableau des cartes à examiner.

    Returns:
        bool: True si une paire est formée dans la mémoire, False sinon.
    '''
    #R4: Comment “Former une paire dans mémoire”?
    résultat=False
    for i in range(len(mémoire)):
        for j in range(i+1,len(mémoire)):
            if mémoire[i]!=mémoire[j] and dire_si_cartes_forment_paire(mémoire[i][0],mémoire[j][0]):
                résultat=True
    return résultat

def transformer_position_carte(position:str,tableau_cartes:list):
    '''
    Transforme une position de carte sur le tapis en la carte associée dans le tableau.

    Args:
        position (str): La position sous forme de chaîne (ex: 'A1', 'B2').
        tableau_cartes (list): Le tableau des cartes à partir duquel la carte sera extraite.

    Returns:
        list: La carte à la position spécifiée dans le tableau.
    '''
    carte=tableau_cartes[int(position[1])-1]['ABCDEFGHIJKLM'.index(position[0])]
    return carte

def former_paire_avec_mémoire(carte_choisie:tuple,mémoire:list,tableau_cartes:list):
    '''
    Vérifie si la carte choisie peut former une paire avec une carte dans la mémoire.

    Args:
        carte_choisie (tuple): La carte choisie sous forme de tuple (valeur, enseigne).
        mémoire (list): La mémoire contenant les cartes mémorisées.
        tableau_cartes (list): Le tableau des cartes pour vérifier les paires.

    Returns:
        bool: True si la carte choisie forme une paire avec une carte dans la mémoire, False sinon.
    '''
    résultat=False
    carte1=transformer_position_carte(carte_choisie,tableau_cartes)[0]
    for elt in mémoire:
        if elt[0]!=carte1 and dire_si_cartes_forment_paire(carte1,elt[0]):
            résultat=True
    return résultat

def carte_dans_mémoire(carte_choisie:tuple,mémoire:list):
    '''
    Vérifie si une carte choisie est présente dans la mémoire.

    Args:
        carte_choisie (tuple): La carte choisie à vérifier.
        mémoire (list): La mémoire contenant les cartes mémorisées.

    Returns:
        bool: True si la carte est dans la mémoire, False sinon.
    '''
    résultat=False
    for elt in mémoire:
        if elt[1]==carte_choisie:
            résultat=True
    return résultat