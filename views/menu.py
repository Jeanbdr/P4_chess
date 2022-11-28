from controler.database import save_db, load_tournament
from controler.player import update_rankings, update_ranking_menu
from controler.tournament import create_tournament, play_tournament

from views.players import CreatePlayer
from views.report import Report
from views.tournament import LoadTournament
from views.verification import View


class MainMenu(View):
    def display_main_menu(self):

        while True:
            print()
            user_input = self.get_user_entry(
                msg_display="Bienvenue veuillez faire un choix\n"
                "0 - Créer un tournoi\n"
                "1 - Charger un tournoi\n"
                "2 - Créer des joueurs\n"
                "3 - Voir les rapports\n"
                "4 - Update le classement d'un joueur\n"
                "q - Quitter\n> ",
                msg_error="Veuillez entrer une valeur valide",
                value_type="selection",
                assertions=["0", "1", "2", "3", "4", "q"],
            )

            if user_input == "0":
                tournament = create_tournament()
                break

            elif user_input == "1":
                serialized_tournament = LoadTournament().display_menu()
                if serialized_tournament:
                    tournament = load_tournament(serialized_tournament)
                    break
                else:
                    print("Aucun tournoi sauvegardé !")
                    continue

            elif user_input == "2":
                user_input = self.get_user_entry(
                    msg_display="Nombre de joueurs à créer:\n> ",
                    msg_error="Veuillez entrer une valeur numérique valide ",
                    value_type="numeric",
                )
                for i in range(user_input):
                    serialized_new_player = CreatePlayer().display_menu()
                    save_db("players", serialized_new_player)

            elif user_input == "3":
                while True:
                    user_input = self.get_user_entry(
                        msg_display="0 - Joueurs\n1 - Tournois\nr - Retour\n> ",
                        msg_error="Veuillez faire un choix valide.",
                        value_type="selection",
                        assertions=["0", "1", "r"],
                    )

                    if user_input == "r":
                        break

                    elif user_input == "0":
                        while True:
                            user_input = self.get_user_entry(
                                msg_display="Voir le classement:\n"
                                "0 - Par rang\n"
                                "1 - Par ordre alphabétique\n"
                                "r - Retour\n> ",
                                msg_error="Veuillez faire un choix valide.",
                                value_type="selection",
                                assertions=["0", "1", "r"],
                            )
                            if user_input == "r":
                                break
                            elif user_input == "0":
                                sorted_players = Report().sort_players(
                                    Report().players, by_rank=True
                                )
                                Report().display_players_report(players=sorted_players)
                            elif user_input == "1":
                                sorted_players = Report().sort_players(
                                    Report().players, by_rank=False
                                )
                                Report().display_players_report(players=sorted_players)

                    elif user_input == "1":
                        Report().display_tournaments_reports()

            elif user_input == "4":
                update_ranking_menu()

            else:
                quit()

        print()
        user_input = self.get_user_entry(
            msg_display="0 - Jouer le tournoi\n" "q - Quitter\n> ",
            msg_error="Veuillez entrer une valeur valide",
            value_type="selection",
            assertions=["0", "q"],
        )

        if user_input == "0":
            rankings = play_tournament(tournament, new_tournament_loaded=True)
        else:
            quit()

        # Print final result
        print()
        print(f"Tournoi {tournament.name} terminé !\nRésultats:")
        for i, player in enumerate(rankings):
            print(f"{str(i + 1)} - {player}")

        # Update player's ranking
        print()
        user_input = self.get_user_entry(
            msg_display="Mise à jour des classements\n"
            # "0 - Automatiquement\n"
            "1 - Manuellement\n" "q - Quitter\n> ",
            msg_error="Veuillez entrer une valeur valide",
            value_type="selection",
            assertions=["1", "q"],  # "0"
        )
        """
        if user_input == "0":
            for i, player in enumerate(rankings):
                print(player.name)
                update_rankings(player, i + 1)
        """

        if user_input == "1":
            for player in rankings:
                rank = self.get_user_entry(
                    msg_display=f"Rang de {player}:\n> ",
                    msg_error="Veuillez entrer un nombre entier.",
                    value_type="numeric",
                )
                update_rankings(player, rank)

        else:
            quit()
