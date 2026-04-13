from afficher_tapis import*
from initialiser_le_tapis import*
from verifier_carte_existe import*
from cartes_forment_paire import*
from retirer_cartes import*
from rester_paire import*
from faire_choisir_carte import*

def faire_choisir_une_paire_humain(cartes_choisies,tableau_cartes,abscisse,choix):
    """
    Permet à un joueur humain de choisir deux cartes et met à jour l'état du jeu.

    Arguments:
        cartes_choisies (list): Coordonnées des cartes déjà choisies.
        tableau_cartes (list): Plateau de jeu, indiquant la valeur et l'état des cartes.
        abscisse (list): Liste des abscisses du plateau (ex. ['A', 'B', ..., 'M']).
        choix (str): Dernière carte choisie ou 'Q' pour quitter.

    Return:
        str: Dernier choix effectué par le joueur ('Q' si la partie est abandonnée).
    
    """
    while len(cartes_choisies)<2 and choix!='Q':
        choix=faire_choir_carte(cartes_choisies,tableau_cartes)
        cartes_choisies.append(choix)

        if choix!='Q':
            for carte in cartes_choisies:               
                tableau_cartes[int(carte[1])-1][abscisse.index(carte[0])][1]=True

            afficher_tapis(tableau_cartes)
    return choix


def verifier_si_cartes_forment_paire(cartes_choisies,tableau_cartes,abscisse,compteur_coups):
    """
    Vérifie si les cartes choisies forment une paire et met à jour l'état du jeu.

    Arguments:
        cartes_choisies (list): Coordonnées des cartes choisies (ex. ['A1', 'B2']).
        tableau_cartes (list): Plateau de jeu, contenant la valeur et l'état (visible ou non) des cartes.
        abscisse (list): Liste des abscisses du plateau (ex. ['A', 'B', ..., 'M']).
        compteur_coups (int): Nombre de coups joués.

    Return:
        int: Compteur de coups mis à jour.
    """
    if cartes_choisies[-1]=='Q':
        for i in range (4):
                for j in range (13):
                    tableau_cartes[i][j][0]=None
        afficher_tapis(tableau_cartes)
        print ('La partie a été abandonnée !')

    elif cartes_forment_paire(cartes_choisies,tableau_cartes):
        compteur_coups += 1
        input("Bravo!     Appuyer 'Return' pour continuer...")
        retirer_cartes(cartes_choisies[0],cartes_choisies[1],tableau_cartes)
    
    else:
        input("Pas de paire.     Appuyer 'Return' pour continuer...")
        compteur_coups += 1
        tableau_cartes[int(cartes_choisies[0][1])-1][abscisse.index(cartes_choisies[0][0])][1]=False
        tableau_cartes[int(cartes_choisies[1][1])-1][abscisse.index(cartes_choisies[1][0])][1]=False
        cartes_choisies=[]
    return compteur_coups
    

def jouer_memory_humain():
    """
    Lance une partie de Memory pour un joueur humain.

    La fonction initialise le plateau, permet au joueur de choisir des cartes, 
    vérifie les paires, et continue jusqu'à ce que toutes les paires soient trouvées 
    ou que le joueur abandonne.

    Return:
        None
    """
    #initialiser tapis
    tableau_cartes=initialiser_le_tapis()
    compteur_coups = 0

    
    #Tant que Rester des paires à trouver
    while rester_paire(tableau_cartes):


        #afficher tapis
        afficher_tapis(tableau_cartes)
        cartes_choisies=[]
        choix=''
        abscisse='ABCDEFGHIJKLM'


        #Faire choisir une paire à l’humain
        choix=faire_choisir_une_paire_humain(cartes_choisies,tableau_cartes,abscisse,choix)
            

        #Verifier si les cartes forment une paire
        compteur_coups=verifier_si_cartes_forment_paire(cartes_choisies,tableau_cartes,abscisse,compteur_coups)
        

    #Terminer le jeu
    if cartes_choisies[-1] !='Q':
        print(f"Félicitations ! Vous avez terminé le jeu en {compteur_coups} coups.")


jouer_memory_humain()