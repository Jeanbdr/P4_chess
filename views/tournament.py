from model.tournament import ROUND_NUMBERS, PARTICIPANTS, TODAY


class CreateTournament:  # NOM A CHANGER
    """Demande à l'utilisateur les informations nécessaires pour la création d'un tournoi"""

    def input_tournament(self):

        name = input("Saisissez le nom du tournoi: ")
        place = input("Saisissez le lieu du tournoi: ")
        while True:
            try:
                time_control = int(
                    input(
                        f"Choisissez le type de tournoi : \n"
                        f"0 >> Bullet \n"
                        f"1 >> Coup rapide \n"
                        f"2 >> Blitz \n"
                        f">>> "
                    )
                )
            except ValueError:
                print("Choix non valable merci de choisir entre 0, 1 ou 2")
            if time_control not in (0, 1, 2):
                print(
                    "Le type de tournoi n'est pas valide merci de choisir entre 0, 1 ou 2"
                )
            elif time_control == 0:
                time_control = "Bullet"
                break
            elif time_control == 1:
                time_control = "Coup rapide"
                break
            elif time_control == 2:
                time_control = "Blitz"
                break
            else:
                break

        while True:
            try:
                participants = int(
                    input("Saisissez le nombre de joueurs dans le tournoi: ")
                )
            except ValueError:
                print("Erreur : Merci de saisir une valeur numérique")

            else:
                if participants < PARTICIPANTS:
                    print(
                        "Nombre de participants trop faible le tournoi ne peut être crée. (8 minimum)"
                    )
                    continue
                break

        description = input("Saisissez une description du tournoi (optionnelle): ")
        return {
            "name": name,
            "place": place,
            "time_control": time_control,
            "participants": participants,
            "today": TODAY,
            "round_number": ROUND_NUMBERS,
            "description": description,
        }

    def print_leaderboard(self, players):
        print()
        for player in sorted(players, key=lambda player: player.score, reverse=True):
            print(f"{player} avec un score de {player.score} ")
        print()
