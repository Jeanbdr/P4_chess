from db import db_player


class Player:
    """Création d'une fiche joueur"""

    def __init__(self, first_name, last_name, birthdate, gender, ranking, total_score):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.total_score = total_score
        self.score = 0
        self.played_against = []
        self._id = self.save()

    def __str__(self):  # VALIDE
        return f"{self.first_name} {self.last_name} id {self.player_id}"

    def save_serialized_player(self, save_tournament_score=False):  # VALIDE
        serialized_players = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "ranking": self.ranking,
            "total_score": self.total_score,
            "score": self.score,
        }
        if save_tournament_score:
            serialized_players["score"] = self.score
        return serialized_players

    def save(self):  # EN COURS
        return db_player.insert(self.save_serialized_player())
