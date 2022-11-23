from model.tournament import ROUND_NUMBERS
from datetime import datetime
from model.match import Match


class Round:
    def __init__(self, round_name, player_pairs, load_match: False):
        self.round_name = round_name
        self.player_pairs = player_pairs
        if load_match:
            self.matchs = []
        else:
            self.matchs = self.create_matchs()
        self.start_date = datetime.now()
        self.end_date = ""

    def __str__(self):
        return self.round_name

    def create_matchs(self):
        matchs = []
        for i, pair in enumerate(self.player_pairs):
            matchs.append(Match(name=f"Match {i}", player_pair=pair))
        return matchs

    def mark_done(self):
        self.end_date = datetime.now()
        print(f"Round {self.name} terminé {self.end_date}")
        print("Saisir résultats des matchs:")
        for match in self.matchs:
            match.play_match()

    def serialized_round(self):
        serialized_pair = []
        for pair in self.player_pairs:
            serialized_pair.append(
                pair[0].save_serialized_player(save_tournament_score=True),
                pair[1].save_serialized_player(save_tournament_score=True),
            )
