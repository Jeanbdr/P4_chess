from controler.database import save_db, update_player_rank, load_db, search_player
from model.player import Player
from views.players import CreatePlayer
from views.verification import View


def create_player():
    # Récupération et sauvegarge des infos du joueur
    user_entries = CreatePlayer().display_menu()
    player = Player(
        user_entries["first_name"],
        user_entries["name"],
        user_entries["birthdate"],
        user_entries["gender"],
        user_entries["total_score"],
        user_entries["ranking"],
    )
    serialized_player = player.save_serialized_player()
    save_db("players", serialized_player)
    return player


def update_rankings(player, ranking, score=True):
    if score:
        player.total_score += player.tournament_score
    player.ranking = ranking
    serialized_player = player.save_serialized_player(save_tournament_score=True)
    update_player_rank("players", serialized_player)
    print(
        f"Update du rang de {player}:\nScore total: {player.total_score}\nRang: {player.ranking}"
    )


def update_ranking_menu():
    all_player = load_db("players")
    display_msg = "Choisir un joueur à update:\n"
    for player in all_player:
        display_msg = display_msg + f"{player['first_name']} {player['name']}\n"
        print(display_msg)
        player_firstname = input("Prénom du joueur choisis: ")
        player_name = input("Nom du joueur choisis: ")
        new_ranking = int(input("Nouveau ranking du joueur: "))
    search_player(
        db_name="players",
        player_firstname=player_firstname,
        player_name=player_name,
        new_ranking=new_ranking,
    )
