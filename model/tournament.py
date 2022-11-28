from model.round import Round

ROUND_NUMBERS = 4


class Tournoi:
    """Classe permettant la création d'un tournoi"""

    def __init__(
        self, name, place, date, time_control, players, nb_rounds=ROUND_NUMBERS, desc=""
    ):
        self.name = name
        self.place = place
        self.date = date
        self.time_control = time_control
        self.players = players
        self.nb_rounds = nb_rounds
        self.rounds = []
        self.desc = desc

    def __str__(self):
        return f"Tournoi : {self.name}"

    def create_round(self, round_number):
        players_pairs = self.create_pairs(current_round=round_number)
        round = Round("Round" + str(round_number + 1), players_pairs)
        self.rounds.append(round)

    def create_pairs(self, current_round):
        player_pair = []
        if current_round == 0:
            sorted_players = sorted(self.players, key=lambda x: x.ranking, reverse=True)
            top_half = sorted_players[: len(sorted_players) // 2]
            bottom_half = sorted_players[len(sorted_players) // 2 :]
            for i, player in enumerate(top_half):
                x = 0
                while True:
                    try:
                        player_2 = bottom_half[i + x]
                    except IndexError:
                        player_2 = bottom_half[i]
                        player_pair.append((player, player_2))
                        break
                    else:
                        player_pair.append((player, player_2))
                        break
            print(player_pair)
            return player_pair
        else:
            sorted_players = sorted(
                self.players,
                key=lambda x: (x.tournament_score, x.ranking),
                reverse=True,
            )
            p1 = sorted_players[0::2]
            print(p1)
            p2 = sorted_players[1::2]
            print(p2)
            for p1, p2 in zip(p1, p2):
                player_pair.append((p1, p2))
            return player_pair

    def get_rankings(self, by_score=True):
        if by_score:
            sorted_players = sorted(
                self.players, key=lambda x: x.tournament_score, reverse=True
            )
        else:
            sorted_players = sorted(self.players, key=lambda x: x.ranking, reverse=True)

        return sorted_players

    def save_serialized_tournament(self, save_rounds=False):
        serialized_tournament = {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "time_control": self.time_control,
            "players": [
                player.save_serialized_player(save_tournament_score=True)
                for player in self.players
            ],
            "nb_rounds": self.nb_rounds,
            "rounds": [round.get_serialized_round() for round in self.rounds],
            "desc": self.desc,
        }
        if save_rounds:
            serialized_tournament["rounds"] = [
                round.get_serialized_round() for round in self.rounds
            ]
        return serialized_tournament


"""
    def create_pairs(self, current_round): #SOFIEN 
        all_pairs =[]
        pairs = []
        if current_round == 0:
            print('current round 0 chacal')
            sorted_players = sorted(self.players, key=lambda player: player.ranking, reverse=True)
            top = sorted_players[:len(sorted_players)//2]
            print(top)
            bottom = sorted_players[len(sorted_players)//2:]
            print(bottom)
            for player_1, player_2 in zip(top, bottom):
                pairs.append((player_1, player_2))
        else:
            sorted_players = sorted(self.players, key=lambda player:(player.tournament_score), reverse=True) #ranking
            print('pas round 1')
            already_in_pair =[]
            for i in range(len(sorted_players)):
                print('range faite')
                player_1 = sorted_players[i]
                print(f"player1 {player_1}")
                if player_1 in already_in_pair:
                    continue
                for j in range(i+1, len(sorted_players)):
                    player_2=sorted_players[j]
                    print(f"player2 {player_2}")
                    if player_2 in already_in_pair or (player_1, player_2) in all_pairs:
                        continue
                    pairs.append((player_1, player_2))
                    already_in_pair.append((player_1, player_2)) #extend
                    print('tes la')
        return pairs

            already_in_pairs = []
            sorted_players = []
            score_sorted_players = sorted(
                self.players, key=lambda player: player.tournament_score, reverse=True
            )
            while True:
                for i, player in enumerate(score_sorted_players): #range
                    sorted_players.append(player)
                    x = 0
                    player_1 = sorted_players[i+x]
                    print(f"player1{player}")
                    already_in_pairs.append(player)
                    if player_1 in already_in_pairs:
                        x += 1
                        #player = sorted_players[player+1]
                    for j, player in enumerate(sorted_players):
                        x=0
                        player_2 = sorted_players[j+x]
                        print(f"player2{player_2}")
                        already_in_pairs.append(player_2)
                        if player_2 in already_in_pairs:
                            x+=1
                            #player_2 = sorted_players[j+1]
                        player_pair.append((player_1,player_2))
                return player_pair




"""
