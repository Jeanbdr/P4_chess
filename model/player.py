from db import database


class Player:
    """Création d'une fiche joueur"""

    def __init__(self, first_name, last_name, birthdate, gender, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = 0
        self.played_against = []
        self._id = self.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def serialized_player(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "ranking": self.ranking,
            "score": self.score,
        }

    def save(self):
        player_table = database.table("players")
        return player_table.insert(self.serialized_player)

    def update_elo(self, new_elo):
        database.update({"ranking": new_elo}, doc_ids=self._id)
