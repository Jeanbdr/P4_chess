from views.tournament import CreateTournament
from model.tournament import Tournoi

from views.players import PlayerInput
from model.player import Player

from model.round import Round
from model.match import Match

from db import database


class Controler:
    def __init__(self):
        self.tournament = None
        self.players = []
        self.current_round = None
        self.tournament_view = CreateTournament()
        self.player_view = PlayerInput()

    def run(self):
        self.tournament = self.create_tournament()
        self.create_players()
        self.create_rounds()
        self.tournament_view.print_leaderboard(self.players)

    def create_tournament(self):
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
        tournament.serialized_tournament()
        print(tournament)
        self.tournament_database(
            serialized_tournament=tournament.serialized_tournament()
        )
        return tournament

    def create_one_player(self):
        player_info = PlayerInput().input_player()
        player = Player(
            player_info["first_name"],
            player_info["last_name"],
            player_info["birthdate"],
            player_info["gender"],
            player_info["ranking"],
        )
        print(self.player_view.print_player())
        self.players.append(player)

    def create_players(self):
        for _ in range(int(self.tournament.participants)):
            self.create_one_player()
            # chargement joueur

    def create_rounds(self):
        for _ in range(self.tournament.round_number):
            self.create_one_round()

    def create_one_round(self):
        self.current_round = Round()
        self.create_matches()

    def create_matches(self):
        if self.current_round == 0:
            sorted_players = sorted(
                self.players, key=lambda player: player.ranking, reverse=True
            )
        else:
            sorted_players = sorted(
                self.players, key=lambda player: player.score, reverse=True
            )
        for i in range(len(sorted_players) - 1):
            match = Match(player_1=sorted_players[i], player_2=sorted_players[i + 1])
            # match = Match(player_1=sorted_players[i], player_2=sorted_players[i + (self.tournament.participants // 2)])
            print()
            winner = PlayerInput().get_result(match.player_1, match.player_2)
            match.update_winner(winner)
            self.current_round.matches.append(match)

    def update_player_elo(self):  # A VOIR AVEC SOFIEN
        searched_player = self.player_view.search_player(
            players=database.table("players")
        )
        new_elo = self.player_view.change_elo()
        Player().update_elo(new_elo)
        # choosen_player = db_player.get(doc_id=searched_player)
        # db_player.update({"ranking": new_elo}, doc_ids=choosen_player)
        # db_player.update({"ranking": new_elo}, doc_ids=player_elo)
