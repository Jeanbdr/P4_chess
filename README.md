# Projet 04 OpenClassRooms : Developpez un prog python (echec)

## Mise en place du projet :
    
    - Cliquer le bouton vert code puis télécharger le zip de ce code
    - Déziper le et placer le dans le dossier de votre choix

### Création de l'environnement virtuel :

    - python<version> -m venv <nom_env>

    Pour l'activer :

            - source <nom_env>/bin/activate
    
    Pour le désactiver :

            - deactivate/

### Installation des packages nécessaires :

    - python<version> install -r requirements.txt

### Execution du script :

    - python<version> main.py

### Comment utiliser le programme :

    - Une fois lancée un menu apparaîtra vous proposant plusieurs
    options comme consulter un rapport, créer un tournoi, ajouter des 
    joueurs etc. En saisissant une des options proposées vous pourrez
    profiter du programme.

### Génerer un rapport flake-8

    - Dans le terminal une fois situé dans le dossier contenant le
    programme, tapez la commande suivante :

        flake8 --format=html --htmldir=report-flake

    Le rapport sera crée dans le dossier report-flake