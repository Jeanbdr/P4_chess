import datetime, re
from db import database, Query, where


class NegativeValue(Exception):
    """Raised when elo is negative"""

    pass


class IdExist(Exception):
    """Raised when ID already exist"""

    pass


class PlayerView:
    """Affiche les vues"""

    def input_player(self):  # VALIDE
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
        while (
            True
        ):  # L'IDEE LA C'EST DE CREER UN ID POUR RETROUVER LE JOUEUR SAUF QUE CA MARCHE PAS
            try:
                player_id = int(input("Id choisis par le joueur (exemple : 1234):"))
                if player_id in database.search(where("player_id") == player_id):
                    raise IdExist("Ca existe")
            except ValueError:
                print("L'id choisis n'est pas valide")
            else:
                break

        return {
            "first_name": first_name,
            "last_name": last_name,
            "birthdate": birthdate,
            "gender": gender,
            "ranking": ranking,
            "player_id": player_id,
        }

    def change_elo(self):
        while True:
            try:
                new_elo = int(input(f"Nouvel ELO :\n" f">>>"))
            except ValueError:
                print("Elo non valide merci de saisir un elo valide")
            else:
                break
        return new_elo

    def search_player(self):
        while True:
            try:
                player_id = int(input("ID du joueur recherhché \n >>>"))
            except ValueError:
                print("ID non valable merci de saisir un ID existant")
            else:
                break
        return player_id


"""
    def search_player(self, players):
        # print(players)
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
"""
