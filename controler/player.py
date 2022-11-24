from controler.database import save_db, update_player_rank, load_db
from model.player import Player
from views.players import CreatePlayer
from views.verification import View


def create_player():

    # Récupération des infos du joueur
    user_entries = CreatePlayer().display_menu()
    player = Player(
        user_entries["first_name"],
        user_entries["name"],
        user_entries["birthdate"],
        user_entries["gender"],
        user_entries["total_score"],
        user_entries["ranking"],
    )

    # serialization et sauvegarde du joueur:
    serialized_player = player.save_serialized_player()
    # print(serialized_player)
    save_db("players", serialized_player)

    return player


def update_rankings(player, ranking, score=True):
    if score:
        player.total_score += player.tournament_score
    player.ranking = ranking
    serialized_player = player.save_serialized_player(save_tournament_score=True)
    # print(serialized_player['name'])
    update_player_rank("players", serialized_player)
    print(
        f"Update du rang de {player}:\nScore total: {player.total_score}\nRang: {player.ranking}"
    )


def update_ranking_menu():
    all_player = load_db("players")
    display_msg = "Choisir un joueur à update:\n"
    assertions = []
    for player in all_player:
        display_msg = (
            display_msg + f"{str(+1)} - {player['first_name']} {player['name']}\n"
        )
        assertions.append(str(+1))

    user_input = int(
        View().get_user_entry(
            msg_display=display_msg,
            msg_error="Veuillez entrer un choix parmis ceux de la liste",
            value_type="selection",
            assertions=assertions,
        )
    )
    print(assertions)
    update_rankings(player, user_input, score=False)
