from controler.database import save_db, update_player_rank, load_db, update_player
from model.player import Player
from views.players import CreatePlayer


def create_player():
    user_entries = CreatePlayer().display_menu()
    player = Player(
        user_entries["first_name"],
        user_entries["name"],
        user_entries["birthdate"],
        user_entries["gender"],
        user_entries["ranking"],
    )
    serialized_player = player.save_serialized_player()
    save_db("players", serialized_player)
    return player


def update_rankings(player, ranking, score=True):
    if score:
        player.tournament_score
    player.ranking = ranking
    serialized_player = player.save_serialized_player(save_tournament_score=True)
    update_player_rank("players", serialized_player)
    print(
        f"Update du rang de {player}:\nScore total: {player.tournament_score}\nRang: {player.ranking}"
    )


def update_ranking_menu():
    all_player = load_db("players")
    print("Choisir un joueur à update:")
    for player in all_player:
        print(f"{player['first_name']} {player['name']}")
    player_firstname = input("Prénom du joueur choisis: ")
    player_name = input("Nom du joueur choisis: ")
    new_ranking = int(input("Nouveau ranking du joueur: "))
    update_player(
        db_name="players",
        player_firstname=player_firstname,
        player_name=player_name,
        new_ranking=new_ranking,
    )
