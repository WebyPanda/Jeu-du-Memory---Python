def choisir_niveau_ordi():
    '''
    Demande à l'utilisateur de choisir un niveau de difficulté pour l'ordinateur.

    La fonction demande à l'utilisateur de saisir un nombre entre 0 et 5 pour définir le niveau de l'ordinateur. 
    Si l'entrée est invalide, elle redemande à l'utilisateur de faire un choix valide.

    Retourne :
        int : Le niveau choisi par l'utilisateur, sous forme d'un entier entre 0 et 5.
    '''
    niveau='str'
    while niveau not in ['0','1','2','3','4','5']:
        niveau=input('Choisissez le niveau de l ordinateur, entre 0 et 5.')
    return int(niveau)

def afficher_mémoire(mémoire:list,niveau_ordi:int):
    '''
    Affiche le contenu actuel de la mémoire du jeu, adapté au niveau de l'ordinateur.

    La fonction parcourt la mémoire et affiche les cartes mémorisées. Elle indique également 
    combien de cartes sont actuellement en mémoire et le nombre maximal de cartes mémorisables 
    (qui dépend du niveau de l'ordinateur).

    Paramètres :
        mémoire (list) : Une liste contenant les cartes mémorisées sous forme de tuples.
        niveau_ordi (int) : Le niveau de l'ordinateur, influençant la taille maximale de la mémoire.

    Exemple d'affichage :
        'Mémoire (3/6) : P3, T5, C7'
    '''
    ligne='Mémoire ('+str(len(mémoire))+'/'+str(5*niveau_ordi)+') :'
    for elt in mémoire:
        ligne+=' '+elt[0]
    print(ligne)