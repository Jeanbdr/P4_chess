from views.verification import View
from controler.database import load_db


class CreatePlayer(View):
    def display_menu(self):

        first_name = input("Prénom du joueur: ")

        name = input("Nom du joueur: ")

        birthdate = self.get_user_entry(
            msg_display="Date de naissance (format DD/MM/YYYY): ",
            msg_error="Veuillez entrer une date au format valide: DD/MM/YYYY",
            value_type="date",
        )

        gender = self.get_user_entry(
            msg_display="Sexe (M ou F): ",
            msg_error="Veuillez entrer M ou F",
            value_type="selection",
            assertions=["M", "m", "F", "f"],
        ).upper()

        ranking = self.get_user_entry(
            msg_display="Elo du joueur: ",
            msg_error="Veuillez entrer une valeur numérique valide.",
            value_type="numeric",
        )

        print(f"{first_name} {name} a été créé.")

        return {
            "first_name": first_name,
            "name": name,
            "birthdate": birthdate,
            "gender": gender,
            "ranking": ranking,
        }


class LoadPlayer(View):
    def display_menu(self, nb_players_to_load):

        all_players = load_db("players")
        serialized_loaded_players = []
        for i in range(nb_players_to_load):
            print(f"Plus que {str(nb_players_to_load - i)} joueurs à charger.")
            display_msg = "Choisir un joueur:\n"

            assertions = []
            for i, player in enumerate(all_players):
                display_msg = (
                    display_msg
                    + f"{str(i+1)} - {player['first_name']} {player['name']}\n"
                )
                assertions.append(str(i + 1))

            user_input = int(
                self.get_user_entry(
                    msg_display=display_msg,
                    msg_error="Veuillez entrer un nombre entier.",
                    value_type="selection",
                    assertions=assertions,
                )
            )
            if all_players[user_input - 1] not in serialized_loaded_players:
                serialized_loaded_players.append(all_players[user_input - 1])
            else:
                print("Joueur déjà chargé veuillez choisir un autre joueur.")
                nb_players_to_load += 1

        return serialized_loaded_players
