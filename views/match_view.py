class MatchView:
    def get_result(winner, player_1, player_2):  # VALIDE
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
