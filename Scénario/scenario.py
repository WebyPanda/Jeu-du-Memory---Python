from afficher_tapis import*
from initialiser_le_tapis import*
from faire_choisir_paire import*
from vérifier_paire import*

def scénario():
    '''
    Simule une partie de Memory avec un jeu de 52 cartes, en effectuant plusieurs actions pour illustrer le processus du jeu.

    Cette fonction effectue les étapes suivantes dans l'ordre :
    1. Crée un jeu de 52 cartes et le mélanger.
    2. Affiche les cartes du jeu.
    3. Distribue les cartes sur le tapis et affiche le tapis de jeu.
    4. Retourne certaines cartes du tapis, sélectionnées par leurs positions.
    5. Affiche de nouveau le tapis avec les cartes retournées.
    6. Retire certaines cartes du jeu (supposées formant des paires).
    7. Affiche à nouveau le tapis après le retrait des cartes.
    '''
    #Crée un jeu de 52 cartes, le bat
    tableau_cartes=initialiser_le_tapis()

    #Affiche le jeu de carte
    jeu='Jeu : '
    for i in range(4):
        for elt in tableau_cartes[i]:
            jeu+=str(elt[0])+' '
    print(jeu)

    #Distribue les cartes sur le tapis et l'affiche
    afficher_tapis(tableau_cartes)

    #Retourne les cases F1, J2, M4 et A3
    cartes_choisies=[('F1'),('J2'),('M4'),('A3')]
    changer_état_cartes(tableau_cartes,cartes_choisies)

    #Affiche le tapis
    afficher_tapis(tableau_cartes)

    #Retire les cartes J2, M4, D1 et K3
    #Suposons que J2 et M4 forment une paire comme D1 et K3
    retirer_cartes('J2','M4',tableau_cartes)
    retirer_cartes('D1','K3',tableau_cartes)

    #Affiche le tapis
    afficher_tapis(tableau_cartes)

scénario()