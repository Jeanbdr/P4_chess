from db import database, Query


class Player:
    """Création d'une fiche joueur"""

    def __init__(
        self, first_name, last_name, birthdate, gender, ranking, player_id
    ):  # VALIDE
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.player_id = player_id
        self.score = 0
        self.played_against = []
        self._id = self.save()

    def __str__(self):  # VALIDE
        return (
            f"{self.first_name} {self.last_name} avec l'id {self.player_id} a été crée"
        )

    def serialized_player(self):  # VALIDE
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "ranking": self.ranking,
            "player_id": self.player_id,
            "score": self.score,
        }

    def save(self):  # EN COURS
        player_table = database.table("players")
        player_table.insert(self.serialized_player())
        return player_table

    def update_elo(self, new_elo):  # EN COURS
        database.update({"ranking": new_elo}, doc_ids=self._id)
