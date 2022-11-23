from datetime import date
from db import db_tournament

TODAY = date.today().strftime("%d/%m/%y")
ROUND_NUMBERS = 2
PARTICIPANTS = 4


class Tournoi:
    """Classe permettant la création d'un tournoi"""

    def __init__(  # VALIDE
        self,
        name,
        place,
        time_control,
        participants,
        today=TODAY,
        round_number=ROUND_NUMBERS,
        description="",
    ):
        self.name = name
        self.place = place
        self.time_control = time_control
        self.participants = participants
        self.today = today
        self.round_number = round_number
        self.description = description
        self.save()

    def __str__(self):  # VALIDE
        return f"{self.name} se jouant à {self.place} le {self.today}"

    def serialized_tournament(self):  # VALIDE
        return {
            "name": self.name,
            "place": self.place,
            "time control": self.time_control,
            "participants": self.participants,
            "today": self.today,
            "round number": self.round_number,
            "descriptions": self.description,
        }

    def save(self):  # EN COURS
        db_tournament.insert(self.serialized_tournament())
