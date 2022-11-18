class Match:  # VALIDE
    """Class permettant la création d'un match"""

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = None

    def update_winner(self, winner):
        self.winner = winner
        if winner:
            winner.score += 1
        else:
            self.player_1.score += 0.5
            self.player_2.score += 0.5
