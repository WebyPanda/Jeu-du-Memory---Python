"""
Ce module contient les fonctions nécessaires pour afficher le tapis de jeu du mémoire humain,
"""

def ajouter_une_ligne(barre,tableau_cartes,carte_enlevee,i,TEXTES_VALEURS_LONGS,TEXTES_ENSEIGNES_COURTS,TEXTES_VALEURS_COURTS,TEXTES_ENSEIGNES_LONGS,carte_cachée):
    '''
    Ajoute une ligne de cartes au tapis de jeu sous forme de texte.

    Cette fonction génère une ligne complète pour le tapis de jeu,
    en ajoutant les cartes dans leur état actuel, qu'elles soient retournées ou non.
    Chaque ligne contient 13 cartes et peut inclure des indices de lignes et des symboles
    pour les cartes enlevées ou retournées.

    Arguments:
        barre (str): Le symbole de barre à afficher pour la séparation des lignes.
        tableau_cartes (list): Le tableau représentant les cartes du jeu et leur état 
                                (retournées ou non).
        carte_enlevee (str): Le symbole représentant une carte enlevée du tapis.
        i (int): L'indice de la ligne dans le tableau (de 0 à 3).
        TEXTES_VALEURS_LONGS (list): Liste des représentations longues des valeurs des cartes.
        TEXTES_ENSEIGNES_COURTS (tuple): Liste des symboles courts pour les enseignes des cartes.
        TEXTES_VALEURS_COURTS (str): Liste des symboles courts pour les valeurs des cartes.
        TEXTES_ENSEIGNES_LONGS (tuple): Liste des représentations longues des enseignes des cartes.
        carte_cachée (str): Le symbole représentant une carte cachée.

    Returns:
        str: La ligne générée avec les cartes correspondantes à l'état actuel du jeu.
    '''
    axe=''
    axe+=barre

    for j in range(2):
        ligne=''
        if j==1:
            ligne+=' '+str(4-i)+' '
        else:
            ligne+='   '

        for k in range(13):
            ligne+=ajouter_une_carte(tableau_cartes,k,j,i,carte_enlevee,TEXTES_VALEURS_LONGS,TEXTES_VALEURS_COURTS,TEXTES_ENSEIGNES_LONGS,TEXTES_ENSEIGNES_COURTS,carte_cachée)

        ligne+='|'
        if j==1:
            ligne+=' '+str(4-i)+' '
        else:
            ligne+='   '
        ligne+='\n'
        axe+=ligne
    return axe


def ajouter_une_carte(tableau_cartes,k,j,i,carte_enlevee,TEXTES_VALEURS_LONGS,TEXTES_VALEURS_COURTS,TEXTES_ENSEIGNES_LONGS,TEXTES_ENSEIGNES_COURTS,carte_cachée):
    '''
    Ajoute une carte spécifique à une ligne du tapis de jeu en fonction de son état.

    Cette fonction génère la représentation d'une carte individuelle sur le tapis. Si la carte est retournée, elle affiche sa valeur et son enseigne ; si elle est cachée, elle affiche un symbole spécifique ; si elle a été retirée, elle est également représentée par un autre symbole.

    Arguments:
        tableau_cartes (list): Le tableau représentant les cartes du jeu et leur état (retournées ou non).
        k (int): L'indice de la carte dans la ligne (de 0 à 12).
        j (int): L'indice indiquant si la carte est pour la première ou la deuxième partie de la ligne.
        i (int): L'indice de la ligne dans le tableau (de 0 à 3).
        carte_enlevee (str): Le symbole représentant une carte enlevée du tapis.
        TEXTES_VALEURS_LONGS (list): Liste des représentations longues des valeurs des cartes.
        TEXTES_VALEURS_COURTS (str): Liste des symboles courts pour les valeurs des cartes.
        TEXTES_ENSEIGNES_LONGS (tuple): Liste des représentations longues des enseignes des cartes.
        TEXTES_ENSEIGNES_COURTS (tuple): Liste des symboles courts pour les enseignes des cartes.
        carte_cachée (str): Le symbole représentant une carte cachée.

    Returns:
        str: La représentation d'une carte selon son état (retournée, cachée ou enlevée).
    '''

    carte=''
    if tableau_cartes[3-i][k] is None:
        carte+=carte_enlevee
    elif tableau_cartes[3-i][k][1] is True:
        enseigne_ou_valeur=tableau_cartes[3-i][k][0][j]
        if j==0:
            carte+=TEXTES_VALEURS_LONGS[TEXTES_VALEURS_COURTS.index(enseigne_ou_valeur)]
        else:
            carte+=TEXTES_ENSEIGNES_LONGS[TEXTES_ENSEIGNES_COURTS.index(enseigne_ou_valeur)]
    elif tableau_cartes[3-i][k][1] is False:
        carte+=carte_cachée
    return carte


def afficher_tapis(tableau_cartes:list):
    '''
    Affiche le tapis de jeu avec les cartes visibles ou cachées, selon leur état.

    Cette fonction génère une représentation visuelle du tapis de jeu en utilisant des symboles pour chaque carte. 
    Les cartes cachées sont représentées par un symbole spécifique, et les cartes retournées sont affichées avec leur valeur et enseigne correspondantes.

    Arguments:
        tableau_cartes (list): Le tableau représentant le tapis de jeu contenant les cartes et leur état (retournée ou non).

    Returns:
        None: Affiche le tapis de jeu dans la console.
    '''

    abscisses='      A     B     C     D     E     F     G     H     I     J     K     L     M   \n'
    barre='   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n'
    carte_cachée='| ~~~ '
    carte_enlevée='|     '
    tapis=''
    TEXTES_ENSEIGNES_COURTS = tuple('PCKT')
    TEXTES_ENSEIGNES_LONGS = ('| PIQ ', '| COE ', '| CAR ', '| TRE ')
    TEXTES_VALEURS_COURTS = 'A23456789XVDR'
    TEXTES_VALEURS_LONGS = ['|  AS ','|  2  ','|  3  ','|  4  ','|  5  ','|  6  ','|  7  ','|  8  ','|  9  ','|  10 ','| VAL ','| DAM ','| ROI ']
    tapis+=abscisses

    for i in range(4):
        tapis+=ajouter_une_ligne(barre,tableau_cartes,carte_enlevée,i,TEXTES_VALEURS_LONGS,TEXTES_ENSEIGNES_COURTS,TEXTES_VALEURS_COURTS,TEXTES_ENSEIGNES_LONGS,carte_cachée)
        
    tapis+=barre+abscisses
    print(tapis)