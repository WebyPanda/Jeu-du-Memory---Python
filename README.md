# Jeu du Memory - Python

Projet réalisé en prépa dans le cadre d'un projet d'informatique.
Il s'agit d'une implémentation complète du célèbre jeu de Memory, 
jouable directement dans le terminal ou sur éditeur python et codé depuis VSCode.

## Fonctionnalités

- **Moteur de jeu complet** : Gestion d'un paquet de 52 cartes, mélange aléatoire et distribution sur un tapis de 4x13.
- **Affichage dynamique** : Rendu visuel du tapis en mode texte (ASCII) avec mise à jour en temps réel de l'état des cartes (cachées, révélées ou retirées).
- **Deux modes de jeu** :
    - `Humain` : Jouez manuellement en saisissant les coordonnées des cartes (ex: A1, F3).
    - `Ordinateur` : Simulation où l'IA joue contre elle-même avec une gestion de mémoire pour optimiser ses coups.
- **Niveaux de difficulté** : Paramétrage de l'intelligence de l'ordinateur.
- **Scénario de démonstration** : Script inclus pour illustrer le déroulement d'une partie.

## Structure du Projet

L'architecture est modulaire pour séparer la logique métier de l'affichage :

- `memory_humain.py` : Point d'entrée pour une partie interactive.
- `memory_ordi.py` : Point d'entrée pour la simulation d'IA.
- `afficher_tapis.py` : Logique d'affichage graphique en console.
- `scenario.py` : Script de démonstration des fonctionnalités (initialisation, retournement, retrait).
- `tapis.py`, `paires.py`, `ordinateur.py` (etc.) : Modules de gestion des données et de l'IA.

## Comment jouer ?

### Prérequis
- Python 3.x installé.

### Lancement
Pour lancer une partie humaine :
```bash
python memory_humain.py
