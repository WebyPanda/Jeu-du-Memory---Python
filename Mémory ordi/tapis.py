def initialiser_le_tapis():
    '''
    Initialise le tapis de jeu avec des cartes placées aléatoirement.

    Cette fonction crée un tableau de cartes (4 rangées de 13 cartes), chacune ayant une valeur et une enseigne. 
    Les cartes sont placées de manière aléatoire sur le tapis, avec des cartes du type Pioche (P), Coeur (C), Carreau (K), et Trèfle (T) et des valeurs de A à R.

    Args:
        Aucun argument.

    Returns:
        list: Un tableau représentant le tapis de jeu avec 4 rangées et 13 cartes par rangée, où chaque carte est un tableau de deux éléments :
              1. La carte sous forme de chaîne ('valeur'+'enseigne').
              2. Un booléen indiquant si la carte est retournée.

    Exemple:
        >>> tapis = initialiser_le_tapis()
        >>> len(tapis)
        4
        >>> len(tapis[0])
        13
    '''
    #R2: Comment “Initialiser le tapis ” ?
    import random
    TEXTES_ENSEIGNES_COURTS = tuple('PCKT')
    TEXTES_VALEURS_COURTS = 'A23456789XVDR'
    liste=[]

    for i in range(4):
        for j in range(13):
            liste.append(str(TEXTES_VALEURS_COURTS[j])+str(TEXTES_ENSEIGNES_COURTS[i]))

    x=0
    tableau_cartes=[[[None,False] for i in range(13)] for j in range(4)]
    for i in range(4):
        for j in range(13):
            if len(liste)>1:
                x=random.randint(0,len(liste)-1)
            else:
                x=0
            tableau_cartes[i][j][0]=liste[x]
            liste.pop(x)

    return tableau_cartes


def ajouter_une_ligne(barre,tableau_cartes,carte_enlevée,i,TEXTES_VALEURS_LONGS,TEXTES_ENSEIGNES_COURTS,TEXTES_VALEURS_COURTS,TEXTES_ENSEIGNES_LONGS,carte_cachée):
    '''
    Ajoute une ligne de cartes au tapis de jeu sous forme de texte.

    Cette fonction génère une ligne complète pour le tapis de jeu, en ajoutant les cartes dans leur état actuel, qu'elles soient retournées ou non. Chaque ligne contient 13 cartes et peut inclure des indices de lignes et des symboles pour les cartes enlevées ou retournées.

    Args:
        barre (str): Le symbole de barre à afficher pour la séparation des lignes.
        tableau_cartes (list): Le tableau représentant les cartes du jeu et leur état (retournées ou non).
        carte_enlevée (str): Le symbole représentant une carte enlevée du tapis.
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
    #R3: Comment “Ajouter au tapis une ligne de cartes”?
    for j in range(2):
        ligne=''
        if j==1:
            ligne+=' '+str(4-i)+' '
        else:
            ligne+='   '

        for k in range(13):
            ligne+=ajouter_une_carte(tableau_cartes,k,j,i,carte_enlevée,TEXTES_VALEURS_LONGS,TEXTES_VALEURS_COURTS,TEXTES_ENSEIGNES_LONGS,TEXTES_ENSEIGNES_COURTS,carte_cachée)

        ligne+='|'
        if j==1:
            ligne+=' '+str(4-i)+' '
        else:
            ligne+='   '
        ligne+='\n'
        axe+=ligne
    return axe


def ajouter_une_carte(tableau_cartes,k,j,i,carte_enlevée,TEXTES_VALEURS_LONGS,TEXTES_VALEURS_COURTS,TEXTES_ENSEIGNES_LONGS,TEXTES_ENSEIGNES_COURTS,carte_cachée):
    '''
    Ajoute une carte spécifique à une ligne du tapis de jeu en fonction de son état.

    Cette fonction génère la représentation d'une carte individuelle sur le tapis. Si la carte est retournée, elle affiche sa valeur et son enseigne ; si elle est cachée, elle affiche un symbole spécifique ; si elle a été retirée, elle est également représentée par un autre symbole.

    Args:
        tableau_cartes (list): Le tableau représentant les cartes du jeu et leur état (retournées ou non).
        k (int): L'indice de la carte dans la ligne (de 0 à 12).
        j (int): L'indice indiquant si la carte est pour la première ou la deuxième partie de la ligne.
        i (int): L'indice de la ligne dans le tableau (de 0 à 3).
        carte_enlevée (str): Le symbole représentant une carte enlevée du tapis.
        TEXTES_VALEURS_LONGS (list): Liste des représentations longues des valeurs des cartes.
        TEXTES_VALEURS_COURTS (str): Liste des symboles courts pour les valeurs des cartes.
        TEXTES_ENSEIGNES_LONGS (tuple): Liste des représentations longues des enseignes des cartes.
        TEXTES_ENSEIGNES_COURTS (tuple): Liste des symboles courts pour les enseignes des cartes.
        carte_cachée (str): Le symbole représentant une carte cachée.

    Returns:
        str: La représentation d'une carte selon son état (retournée, cachée ou enlevée).
    '''
    #R4: Comment “Ajouter chaque carte du tableau à sa place” ?
    carte=''
    if tableau_cartes[3-i][k]==None:
        carte+=carte_enlevée
    elif tableau_cartes[3-i][k][1]==True:
        enseigne_ou_valeur=tableau_cartes[3-i][k][0][j]
        if j==0:
            carte+=TEXTES_VALEURS_LONGS[TEXTES_VALEURS_COURTS.index(enseigne_ou_valeur)]
        else:
            carte+=TEXTES_ENSEIGNES_LONGS[TEXTES_ENSEIGNES_COURTS.index(enseigne_ou_valeur)]
    elif tableau_cartes[3-i][k][1]==False:
        carte+=carte_cachée
    return carte


def afficher_tapis(tableau_cartes:list):
    '''
    Affiche le tapis de jeu avec les cartes visibles ou cachées, selon leur état.

    Cette fonction génère une représentation visuelle du tapis de jeu en utilisant des symboles pour chaque carte. 
    Les cartes cachées sont représentées par un symbole spécifique, et les cartes retournées sont affichées avec leur valeur et enseigne correspondantes.

    Args:
        tableau_cartes (list): Le tableau représentant le tapis de jeu contenant les cartes et leur état (retournée ou non).

    Returns:
        None: Affiche le tapis de jeu dans la console.

    Exemple:
        >>> tableau = [[['A', False], ['K', True], ['X', False], ['A', True], ...], ...]
        >>> afficher_tapis(tableau)
        Affichage du tapis avec les cartes visibles et cachées.
    '''
    #R2: Comment “Afficher le tapis ” ?
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