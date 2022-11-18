import datetime, re
from db import database
from model.player import Player


class NegativeValue(Exception):
    """Raised when elo is negative"""

    pass


class PlayerInput:
    """Affiche les vues"""

    def input_player(self):
        """Demande à l'utilisateur les informations permettant la création d'un joueur"""
        while True:
            first_name = input("Prénom du joueur: ")
            last_name = input("Nom du joueur: ")
            if re.search("[0-9]", first_name):
                print("Prénom invalide")
            elif re.search("[0-9]", last_name):
                print("Nom invalide")
            else:
                break
        while True:
            birthdate = input("Date de naissance du joueur (JJ/MM/AAAA): ")
            try:
                datetime.datetime.strptime(birthdate, "%d/%m/%Y")
            except ValueError:
                print("Date non valide merci d'utiliser le format JJ/MM/AAAA")
            else:
                break
        while True:
            gender = input("Genre du joueur (M ou F): ").upper()
            if gender not in ("M", "F"):
                print("Genre non valide merci de saisir un genre valide")
            else:
                break
        while True:
            try:
                ranking = int(input("Elo du joueur (valeur numérique positive): "))
                if ranking < 0:
                    raise NegativeValue("Veuillez saisir un elo positif")
            except ValueError:
                print("L'elo du joueur n'est pas valide merci de saisir un elo valide ")
            else:
                break

        return {
            "first_name": first_name,
            "last_name": last_name,
            "birthdate": birthdate,
            "gender": gender,
            "ranking": ranking,
        }

    def print_player(self):
        print(f"{Player} a été crée et posséde le numéro {Player.save()}")

    def get_result(winner, player_1, player_2):  # A DEPLACER DANS MATCH VIEW (à créer)
        while True:
            try:
                winner = int(
                    input(
                        f"Vainqueur du match : \n"
                        f"0 Match nul \n"
                        f"1 {player_1} \n"
                        f"2 {player_2} \n"
                        ">>>"
                    )
                )
            except ValueError:
                print("Choix non valable, veuillez saisir une des valeurs possibles")
            if winner not in (0, 1, 2):
                print(
                    "Choix non valable merci de choisir une des valeurs suivantes (0, 1 ou 2)"
                )
            else:
                break
        if winner == 0:
            print(f"{player_1} et {player_2} ont fait match nul")
            return None
        elif winner == 1:
            print(f"{player_1} à gagné")
            return player_1
        elif winner == 2:
            print(f"{player_2} à gagné")
            return player_2

    def search_player(self, players):
        print(players)
        player_ids = []  # {}
        text_to_display = f"Selectionner un joueur :\n"
        for player in players:
            text_to_display += f"{player} \n"
            player_ids = player
        text_to_display += ">>>"
        while True:
            try:
                player_id = int(input(text_to_display))
            except ValueError:
                print("Choix non valable, veuillez saisir une des valeurs possibles")
            if player_id not in player_ids:
                print("Choix non valable merci de choisir une des valeurs suivantes")
            else:
                break
        return player_ids[player_id]

    def change_elo(self):
        while True:
            try:
                new_elo = int(input(f"Nouvel ELO :\n" f">>>"))
            except ValueError:
                print("Elo non valide merci de saisir un elo valide")
            else:
                break
        return new_elo
