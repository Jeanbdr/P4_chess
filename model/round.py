from model.tournament import ROUND_NUMBERS


class Round:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)
