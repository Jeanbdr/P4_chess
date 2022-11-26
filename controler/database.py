from tinydb import TinyDB, Query, where
from tinydb import where
from model.player import Player
from model.tournament import Tournoi
from model.round import Round
from model.match import Match


def save_db(db_name, serialized_data):
    db = TinyDB(f"data/{db_name}.json")
    db.insert(serialized_data)
    print(f"{serialized_data['name']} sauvegardé avec succès ")


def update_db(db_name, serialized_data):
    db = TinyDB(f"data/{db_name}.json")
    db.update(serialized_data, where("name") == serialized_data["name"])
    print(f"{serialized_data['name']} updaté avec succès.")


def update_player_rank(db_name, serialized_data):
    db = TinyDB(f"data/{db_name}.json")
    db.update(
        {
            "ranking": serialized_data["ranking"],
            # "total_score": serialized_data["total_score"],
        },
        where("name") == serialized_data["name"],
    )
    print(f"{serialized_data['name']} updaté avec succès.")


def load_db(db_name):
    db = TinyDB(f"data/{db_name}.json")
    return db.all()


def load_player(serialized_player, load_tournament_score=False):
    player = Player(
        serialized_player["first_name"],
        serialized_player["name"],
        serialized_player["birthdate"],
        serialized_player["gender"],
        # serialized_player["total_score"],
        serialized_player["ranking"],
    )
    if load_tournament_score:
        player.tournament_score = serialized_player["tournament_score"]
    return player


def load_tournament(serialized_tournament):
    loaded_tournament = Tournoi(
        serialized_tournament["name"],
        serialized_tournament["place"],
        serialized_tournament["date"],
        serialized_tournament["time_control"],
        [
            load_player(player, load_tournament_score=True)
            for player in serialized_tournament["players"]
        ],
        serialized_tournament["nb_rounds"],
        serialized_tournament["desc"],
    )
    loaded_tournament.rounds = load_rounds(serialized_tournament, loaded_tournament)
    return loaded_tournament


def load_rounds(serialized_tournament, tournament):
    loaded_rounds = []
    for round in serialized_tournament["rounds"]:
        players_pairs = []
        for pair in round["players_pairs"]:
            for player in tournament.players:
                if player.name == pair[0]["name"]:
                    pair_p1 = player
                elif player.name == pair[1]["name"]:
                    pair_p2 = player
            players_pairs.append((pair_p1, pair_p2))
        loaded_round = Round(round["name"], players_pairs, load_match=True)
        loaded_round.matchs = [
            load_match(match, tournament) for match in round["matchs"]
        ]
        loaded_round.start_date = round["start_date"]
        loaded_round.end_date = round["end_date"]
        loaded_rounds.append(loaded_round)
    return loaded_rounds


def load_match(serialized_match, tournament):
    for player in tournament.players:
        if player.name == serialized_match["player1"]["name"]:
            player1 = player
        elif player.name == serialized_match["player2"]["name"]:
            player2 = player

    loaded_match = Match(players_pair=(player1, player2), name=serialized_match["name"])
    loaded_match.score_player1 = serialized_match["score_player1"]
    loaded_match.score_player2 = serialized_match["score_player2"]
    loaded_match.winner = serialized_match["winner"]
    return loaded_match


def update_player(db_name, player_firstname, player_name, new_ranking):
    db = TinyDB(f"data/{db_name}.json")
    db.update(
        {"ranking": new_ranking},
        (where("first_name") == player_firstname) & (where("name") == player_name),
    )
