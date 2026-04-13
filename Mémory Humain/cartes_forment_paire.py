def cartes_forment_paire(cartes_choisies,tableau_cartes):
    """
    Vérifie si deux cartes choisies forment une paire.
    Une paire est définie comme deux cartes ayant la même valeur et la même couleur (noir ou rouge).
    Arguments:
        cartes_choisies (list): Liste contenant deux cartes sélectionnées par le joueur au format ["A1", "B2"].
        tableau_cartes (list): Plateau de jeu contenant les cartes et leurs caractéristiques.
    Return:
        bool: True si les deux cartes forment une paire, sinon False.
    """
    #convertir les indices "joueur" en indices numeriques
    abscisse='ABCDEFGHIJKLM'
    i0=int(cartes_choisies[0][1])-1
    i1=int(cartes_choisies[1][1])-1
    j0=abscisse.index(cartes_choisies[0][0])
    j1=abscisse.index(cartes_choisies[1][0]) 

    #comparer les couleurs
    TEXTES_ENSEIGNES_COURTS ='PCKT' 
    Couleurs=['Noir','Rouge','Rouge','Noir']
    meme_couleur= Couleurs[TEXTES_ENSEIGNES_COURTS.index(tableau_cartes[i0][j0][0][1])]==Couleurs[TEXTES_ENSEIGNES_COURTS.index(tableau_cartes[i1][j1][0][1])]
    meme_numero= tableau_cartes[i0][j0][0][0]==tableau_cartes[i1][j1][0][0]

    return meme_couleur and meme_numero