from controler.controler import Controler


class MainMenu:
    """Demande à l'utilisateur ce qu'il souhaite faire avant de le rediriger"""

    def input_menu(self):
        while True:
            try:
                menu = int(
                    input(
                        f""
                        f">>> BIENVENUE FAITE VOTRE CHOIX PARMIS LES OPTIONS POSSIBLE <<< \n"
                        f"0 : Créer un profil joueur \n"
                        f"1 : Créer un tournoi \n"
                        f"2 : Modifier l'elo d'un joueur \n"
                        f">>>"
                        f""
                    )
                )
            except ValueError:
                print("Choix non valable merci de faire un choix entre 0 et 2")
            if menu == 0:
                Controler().create_one_player()
            elif menu == 1:
                Controler().run()
            elif menu == 2:
                Controler().update_player_elo()
            else:
                pass
