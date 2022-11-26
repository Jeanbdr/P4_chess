from model.tournament import Tournoi
from views.verification import View
from views.tournament import CreateTournament, LoadTournament
from views.players import LoadPlayer
from controler.player import create_player, update_rankings
from controler.database import save_db, update_db, load_player, load_tournament


def create_tournament():

    menu = View()
    # Récupération des infos du tournoi
    user_entries = CreateTournament().display_menu()

    # Choix chargement joueurs:
    user_input = menu.get_user_entry(
        msg_display="0 - Créer des joueurs\n1 - Charger des joueurs\n>>> ",
        msg_error="Saisir 0 ou 1",
        value_type="selection",
        assertions=["0", "1"],
    )

    # Load and creation of players
    if user_input == "1":
        players = []
        user_input = menu.get_user_entry(
            msg_display="Nombre de joueurs à charger : ",
            msg_error="Veuillez saisir une valeur numérique",
            value_type="numeric",
        )
        serialized_players = LoadPlayer().display_menu(nb_players_to_load=user_input)
        for serialized_player in serialized_players:
            player = load_player(serialized_player)
            players.append(player)

    else:
        print(f"Création de {str(user_entries['nb_players'])} joueurs.")
        players = []
        while len(players) < user_entries["nb_players"]:
            players.append(create_player())

    # Creation and save of tournament
    tournament = Tournoi(
        user_entries["name"],
        user_entries["place"],
        user_entries["date"],
        user_entries["time_control"],
        players,
        user_entries["nb_rounds"],
        user_entries["desc"],
    )

    save_db("tournaments", tournament.save_serialized_tournament())

    return tournament


def play_tournament(tournament, new_tournament_loaded=False):
    menu = View()
    print()
    print(f"Début du tournoi {tournament.name}")
    print()

    while True:
        # Number of round to play if tournament has been loaded
        a = 0
        if new_tournament_loaded:
            for round in tournament.rounds:
                if round.end_date == "":
                    a += 1
            nb_rounds_to_play = tournament.nb_rounds - a
            new_tournament_loaded = False
        else:
            nb_rounds_to_play = tournament.nb_rounds

        for i in range(nb_rounds_to_play):
            tournament.create_round(round_number=i + a)
            current_round = tournament.rounds[-1]
            print()
            print(current_round.start_date + " : Début du " + current_round.name)
            while True:
                print()
                user_input = menu.get_user_entry(
                    msg_display="0 - Round suivant\n"
                    "1 - Voir les classements\n"
                    "2 - Mettre à jour les classements\n"
                    "3 - Sauvegarder le tournoi\n"
                    "4 - Charger un tournoi\n> ",
                    msg_error="Veuillez choisir un élément de la liste",
                    value_type="selection",
                    assertions=["0", "1", "2", "3", "4"],
                )
                print()
                if user_input == "0":
                    current_round.mark_done()
                    break
                elif user_input == "1":
                    print(f"Classement du tournoi {tournament.name}\n:")
                    for i, player in enumerate(tournament.get_rankings()):
                        print(f"{str(i + 1)} - {player}")
                elif user_input == "2":
                    for player in tournament.players:
                        rank = menu.get_user_entry(
                            msg_display=f"Rang de {player}:\n> ",
                            msg_error="Veuillez entrer un nombre entier.",
                            value_type="numeric",
                        )
                        update_rankings(player, rank, score=False)
                elif user_input == "3":
                    rankings = tournament.get_rankings()
                    for i, player in enumerate(rankings):
                        for t_player in tournament.players:
                            if player.name == t_player.name:
                                t_player.ranking = str(i + 1)
                    update_db(
                        "tournaments",
                        tournament.save_serialized_tournament(save_rounds=True),
                    )
                elif user_input == "4":
                    serialized_loaded_tournament = LoadTournament().display_menu()
                    tournament = load_tournament(serialized_loaded_tournament)
                    new_tournament_loaded = True
                    break

            if new_tournament_loaded:
                break

        if new_tournament_loaded:
            continue

        else:
            break

    # sauvegarde du tournoi et on retourne les résultats
    rankings = tournament.get_rankings()
    for i, player in enumerate(rankings):
        for t_player in tournament.players:
            if player.name == t_player.name:
                t_player.tournament_score
                t_player.ranking = str(i + 1)
    update_db("tournaments", tournament.save_serialized_tournament(save_rounds=True))
    return rankings
