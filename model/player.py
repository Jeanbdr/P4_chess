class Player:
    """Création d'une fiche joueur"""

    def __init__(self, first_name, name, birthdate, gender, total_score, ranking=0):
        self.first_name = first_name
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.total_score = total_score
        self.tournament_score = 0
        self.ranking = ranking
        self.played_with = []

    def __str__(self):  # VALIDE
        return f"{self.first_name} {self.name} [{self.tournament_score} pts]"

    def save_serialized_player(self, save_turnament_score=False):  # VALIDE
        serialized_players = {
            "first_name": self.first_name,
            "name": self.name,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "total_score": self.total_score,
            "ranking": self.ranking,
        }
        if save_turnament_score:
            serialized_players["tournament_score"] = self.tournament_score
        return serialized_players
