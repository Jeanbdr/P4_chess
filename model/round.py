from model.match import Match
from utilitairs.timestamp import get_date


class Round:
    def __init__(self, name, player_pairs, load_match: bool = False):
        self.name = name
        self.player_pairs = player_pairs
        if load_match:
            self.matchs = []
        else:
            self.matchs = self.create_matchs()
        self.start_date = get_date()
        self.end_date = ""

    def __str__(self):
        return self.name

    def create_matchs(self):
        matchs = []
        for i, pair in enumerate(self.player_pairs):
            matchs.append(Match(name=f"Match {i}", players_pair=pair))
        return matchs

    def mark_done(self):
        self.end_date = get_date()
        print(f"Round {self.name} terminé {self.end_date}")
        print("Saisir résultats des matchs:")
        for match in self.matchs:
            match.play_match()

    def get_serialized_round(self):
        ser_players_pair = []
        for pair in self.player_pairs:
            ser_players_pair.append(
                pair[0].save_serialized_player(save_tournament_score=True),
                pair[1].save_serialized_player(save_tournament_score=True),
            )
        return {
            "name": self.name,
            "players_pairs": ser_players_pair,
            "matchs": [match.save_serialized_player() for match in self.matchs],
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
