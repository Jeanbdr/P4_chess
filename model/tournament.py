from model.round import Round

ROUND_NUMBERS = 4


class Tournoi:
    """Classe permettant la création d'un tournoi"""

    def __init__(
        self, name, place, date, time_control, players, nb_rounds=ROUND_NUMBERS, desc=""
    ):
        self.name = name
        self.place = place
        self.date = date
        self.time_control = time_control
        self.players = players
        self.nb_rounds = nb_rounds
        self.rounds = []
        self.desc = desc

    def __str__(self):
        return f"Tournoi : {self.name}"

    def create_round(self, round_number):
        players_pairs = self.create_pairs(current_round=round_number)
        round = Round("Round" + str(round_number + 1), players_pairs)
        self.rounds.append(round)

    def create_pairs(self, current_round):
        if current_round == 0:
            sorted_players = sorted(self.players, key=lambda x: x.ranking, reverse=True)
        else:
            sorted_players = []
            score_sorted = sorted(
                self.players, key=lambda x: x.total_score, reverse=True
            )
            for i, player in enumerate(score_sorted):
                try:
                    sorted_players.append(player)
                except player.total_score == score_sorted[i + 1].total_score:
                    if player.ranking > score_sorted[i + 1].ranking:
                        best_player = player
                        worst_player = score_sorted[i + 1]
                    else:
                        best_player = score_sorted[i + 1]
                        worst_player = player
                    sorted_players.append(best_player)
                    sorted_players.append(worst_player)
        top_half = sorted_players[len(sorted_players) // 2 :]
        bottom_half = sorted_players[: len(sorted_players) // 2]

        player_pair = []

        for i, player in enumerate(top_half):
            x = 0
            while True:
                try:
                    player_2 = bottom_half[i + x]
                except IndexError:
                    player_2 = bottom_half[i]
                    player_pair.append((player, player_2))
                    player.played_with.append(player_2)
                    player_2.played_with.append(player)
                    break
                if player in player_2.played_with:
                    x += 1
                    continue
                else:
                    player_pair.append((player, player_2))
                    player.played_with.append(player_2)
                    player_2.played_with.append(player)
                    break
        return player_pair

    def get_rankings(self, by_score=True):
        if by_score:
            sorted_players = sorted(
                self.players, key=lambda x: x.tournament_score, reverse=True
            )
        else:
            sorted_players = sorted(self.players, key=lambda x: x.ranking, reverse=True)

        return sorted_players

    def save_serialized_tournament(self, save_rounds=False):
        serialized_tournament = {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "time_control": self.time_control,
            "players": [
                player.save_serialized_player(save_tournament_score=True)
                for player in self.players
            ],
            "nb_rounds": self.nb_rounds,
            "rounds": [round.get_serialized_round() for round in self.rounds],
            "desc": self.desc,
        }
        if save_rounds:
            serialized_tournament["rounds"] = [
                round.get_serialized_round() for round in self.rounds
            ]
        return serialized_tournament
