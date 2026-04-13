from ordinateur import*
from tapis import*
from choisir_carte import*
def faire_choisir_paire_o(tableau_cartes:list,mémoire:list,niveau_ordi:int):
    '''
    Permet à un ordinateur de choisir une paire de cartes à partir du tableau de cartes et de la mémoire.

    Args:
        tableau_cartes (list): Le tableau contenant les cartes à partir duquel l'ordinateur choisit des cartes.
        mémoire (list): La mémoire contenant les cartes mémorisées, pour que l'ordinateur puisse en tenir compte.
        niveau_ordi (int): Le niveau de l'ordinateur, qui peut influencer la manière dont il choisit les cartes.

    Returns:
        tuple: Un tuple contenant deux éléments :
            - Une liste des cartes choisies par l'ordinateur.
            - La mémoire mise à jour après le choix des cartes.
    '''
    #R2: Comment “Faire choisir une paire à l’ordi” ?
    cartes_choisies=[]
    for i in range(2):
        afficher_mémoire(mémoire,niveau_ordi)
        faire_choisir_carte(cartes_choisies,tableau_cartes,mémoire,niveau_ordi)
        if i==0:
            print('Première carte : '+cartes_choisies[0])
        if i==1:
            print('Deuxième carte : '+cartes_choisies[1])
        afficher_tapis(tableau_cartes)
    return cartes_choisies, mémoire