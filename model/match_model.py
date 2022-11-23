class Match:  # VALIDE
    """Class permettant la création d'un match"""

    def __init__(self, player_pair):
        # self.player_1 = player_1
        # self.player_2 = player_2
        self.player_1 = player_pair[0]
        self.player_2 = player_pair[1]
        # self.player_pair = player_pair
        self.winner = None

    def update_winner(self, winner):
        self.winner = winner
        if winner:
            winner.score += 1
        else:
            self.player_1.score += 0.5
            self.player_2.score += 0.5
