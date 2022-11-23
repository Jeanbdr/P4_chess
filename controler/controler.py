from views.tournament import CreateTournament
from model.tournament import Tournoi

from views.players import PlayerView
from model.player import Player

from model.round import Round
from model.match import Match

from views.match_view import MatchView

from db import where, db_player, db_tournament, database


class Controler:
    def __init__(self):  # VALIDE
        self.tournament = None
        self.players = []
        self.current_round = None
        self.tournament_view = CreateTournament()
        self.player_view = PlayerView()

    def run(self):  # VALIDE
        self.tournament = self.create_tournament()
        self.create_players()
        self.create_rounds()
        self.tournament_view.print_leaderboard(self.players)

    def create_tournament(self):  # VALIDE
        tournament_info = self.tournament_view.input_tournament()

        tournament = Tournoi(
            tournament_info["name"],
            tournament_info["place"],
            tournament_info["time_control"],
            tournament_info["participants"],
            tournament_info["today"],
            tournament_info["round_number"],
            tournament_info["description"],
        )
        print(tournament)
        return tournament

    def create_one_player(self):  # VALIDE
        player_info = PlayerView().input_player()
        player = Player(
            player_info["first_name"],
            player_info["last_name"],
            player_info["birthdate"],
            player_info["gender"],
            player_info["ranking"],
            player_info["player_id"],
            player_info["total_score"],
        )
        player.save_serialized_player()
        self.players.append(player)
        return player

    def create_players(self):  # EN COURS
        for _ in range(int(self.tournament.participants)):
            self.create_one_player()
            # chargement joueur

    def create_rounds(self):  # VALIDE
        for _ in range(self.tournament.round_number):
            self.create_one_round()

    def create_one_round(self):  # VALIDE
        self.current_round = Round()
        self.create_matches()
        self.create_pairs()
        self.create_matches()

    def create_pairs(self):
        if self.current_round == 0:
            sorted_player = sorted(
                self.players, key=lambda player: player.ranking, reverse=True
            )
        else:
            sorted_player = []
            score_sorted = sorted(
                self.players, key=lambda player: player.score, reverse=True
            )
            for i, player in enumerate(score_sorted):
                try:
                    sorted_player.append(player)
                except player.total_score == score_sorted[i + 1].total_score:
                    if player.ranking > score_sorted[i + 1].ranking:
                        good_player = player
                        bad_player = score_sorted[i + 1]
                    else:
                        good_player = score_sorted[i + 1]
                        bad_player = player
                    sorted_player.append(good_player)
                    sorted_player.append(bad_player)

        best_half = sorted_player[len(sorted_player) // 2 :]
        worst_half = sorted_player[: len(sorted_player) // 2]
        player_pair = []
        for i, player in enumerate(best_half):
            p = 0
            while True:
                try:
                    player_2 = worst_half[i + p]
                except IndexError:
                    player_2 = worst_half[i]
                    player_pair.append((player, player_2))
                    player.played_against.append(player_2)
                    player_2.played_against.append(player)
                    break
                if player in player_2.played_against:
                    p += 1
                    continue
                else:
                    player_pair.append((player, player_2))
                    player.played_against.append(player_2)
                    player_2.played_against.append(player)
                    break
        return player_pair

    def create_matches(self):
        match = Match(player_pair=self.create_pairs())
        winner = MatchView().get_result(match)
        match.update_winner(winner)
        self.current_round.matches.append(match)

    def update_player_elo(self):  # A VALIDER
        searched_player = self.player_view.search_player()
        pre_change = db_player.search(where("player_id") == searched_player)
        print(pre_change)
        new_elo = self.player_view.change_elo()
        db_player.update({"ranking": new_elo}, where("player_id") == searched_player)
        post_change = db_player.search(where("player_id") == searched_player)
        print(post_change)
