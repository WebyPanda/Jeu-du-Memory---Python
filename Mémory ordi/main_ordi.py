from tapis import*
from assertions import*
from paires import*
from choix_paire import*
from ordinateur import*

def jouer_mémory_ordi():
    '''
    Lance une partie de Memory où l'ordinateur joue contre lui-même.

    Cette fonction initialise le tapis de jeu avec des cartes placées aléatoirement, 
    fait choisir le niveau de l'ordinateur et fait tourner le jeu jusqu'à ce que toutes les cartes soient découvertes. 
    L'ordinateur choisit des paires de cartes et tente de les associer jusqu'à ce qu'il n'en reste plus.

    La fonction suit les étapes suivantes :
    - Initialisation du tapis de jeu avec les cartes.
    - L'ordinateur choisit une paire de cartes à chaque tour.
    - Vérification si une paire est correcte.
    - La boucle continue tant qu'il reste des paires à trouver.
    - À la fin, un message est affiché indiquant le nombre de coups nécessaires pour gagner.

    Args:
        None: Les arguments sont récupérés directement dans les fonctions internes.

    Returns:
        None: La fonction affiche le résultat de la partie dans la console.
    '''
    #R1:Comment “Faire une partie de memory” ?
    tableau_cartes=initialiser_le_tapis()
    mémoire=[]
    niveau_ordi=choisir_niveau_ordi()
    compteur_coups = 0

    while rester_des_paires(tableau_cartes):
        compteur_coups += 1
        afficher_tapis(tableau_cartes)
        cartes_choisies, mémoire=faire_choisir_paire_o(tableau_cartes,mémoire,niveau_ordi)
        vérifier_paire(tableau_cartes,cartes_choisies,mémoire)

    #R2: Comment “Terminer le jeu” ?
    afficher_tapis(tableau_cartes)
    print(f'J\'ai gagné en {compteur_coups} coups !')

jouer_mémory_ordi()