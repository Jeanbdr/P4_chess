from datetime import date
from db import db_tournament
from model.round import Round

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
        self.rounds = []
        self.save()

    def __str__(self):  # VALIDE
        return f"{self.name} se jouant à {self.place} le {self.today}"

    def create_round(self, round_number):
        players_pairs = self.create_players_pairs(current_round=round_number)
        round = Round("Round" + str(round_number + 1), players_pairs)
        self.rounds.append(round)

    def create_pairs(self, current_round):
        if current_round == 0:
            sorted_players = sorted(
                self.participants, key=lambda player: player.ranking, reverse=True
            )
        else:
            sorted_players = []
            score_sorted = sorted(
                self.participants, key=lambda player: player.total_score, reverse=True
            )
            for i, player in enumerate(score_sorted):
                try:
                    sorted_players.append(player)
                except player.total_score == score_sorted[i + 1].total_score:
                    if player.ranking > score_sorted[i + 1].ranking:
                        best_player = player
                        worst_player = score_sorted[i + 1]
                    else:
                        best_player = score_sorted[i + 1]
                        worst_player = player
                    sorted_players.append(best_player)
                    sorted_players.append(worst_player)
        top_half = sorted_players[len(sorted_players) // 2 :]
        bottom_half = sorted_players[: len(sorted_players) // 2]

        player_pair = []

        for i, player in enumerate(top_half):
            x = 0
            while True:
                try:
                    player_2 = bottom_half[i + x]
                except IndexError:
                    player_2 = bottom_half[i]
                    player_pair.append((player, player_2))
                    player.played_against.append(player_2)
                    player_2.played_against.append(player)
                    break
                if player in player_2.played_against:
                    x += 1
                    continue
                else:
                    player_pair.append((player, player_2))
                    player.played_against.append(player_2)
                    player_2.played_against.append(player)
                    break
        return player_pair

    def tournament_result(self, by_score=True):
        if by_score:
            sorted_player = sorted(
                self.participants, key=lambda player: player.score, reverse=True
            )
        else:
            sorted_player = sorted(
                self.participants, key=lambda player: player.ranking, reverse=True
            )
        return sorted_player

    def save_serialized_tournament(self, save_rounds=False):  # VALIDE
        serialized_tournament = {
            "name": self.name,
            "place": self.place,
            "time control": self.time_control,
            "participants": [
                player.save_serialized_player(save_tournament_score=True)
                for player in self.participants
            ],
            "today": self.today,
            "round number": self.round_number,
            "descriptions": self.description,
            "rounds": [round.serialized_round() for round in self.rounds],
        }
        if save_rounds:
            serialized_tournament["rounds"] = [
                round.serialized_round() for round in self.rounds
            ]
        return serialized_tournament

    def save(self):  # EN COURS
        db_tournament.insert(self.serialized_tournament())
