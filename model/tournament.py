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
        player_pair = []
        play_with = []
        if current_round == 0:
            sorted_players = sorted(self.players, key=lambda x: x.ranking, reverse=True)
            top_half = sorted_players[: len(sorted_players) // 2]
            bottom_half = sorted_players[len(sorted_players) // 2:]
            for player_1, player_2 in zip(top_half, bottom_half):
                player_pair.append((player_1, player_2))
                play_with.append(player_1)
                play_with.append(player_2)
            return player_pair
        else:
            sorted_players = sorted(
                self.players,
                key=lambda x: (x.tournament_score, x.ranking),
                reverse=True,
            )
            odd_players = sorted_players[0::2]
            even_players = sorted_players[1::2]
            for player_1, player_2 in zip(odd_players, even_players):
                player_pair.append((player_1, player_2))
                play_with.append(player_1)
                play_with.append(player_2)
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
