class MatchView:
    def get_result(winner, player_pair):  # VALIDE
        while True:
            try:
                winner = int(
                    input(
                        f"Vainqueur du match : \n"
                        f"0 Match nul \n"
                        f"1 {player_pair[0]} \n"
                        f"2 {player_pair[1]} \n"
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
            print(f"{player_pair[0]} et {player_pair[1]} ont fait match nul")
            return None
        elif winner == 1:
            print(f"{player_pair[0]} à gagné")
            return player_pair[0]
        elif winner == 2:
            print(f"{player_pair[1]} à gagné")
            return player_pair[1]

    selected_player = user_input
    selected_player.ranking = self.ranking
    serialized_player = self.selected_player.save_serialized_player(
        save_tournament_score=True
    )
    update_player_rank("players", serialized_player)
    print(
        f"Update du rang de {player}:\nScore total: {player.total_score}\nRang: {player.ranking}"
    )
