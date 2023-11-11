from Briscola import Briscola, BriscolaGameActions


if __name__ == "__main__":
    #BriscolaGame = Briscola()
    #BriscolaGame.main_game()

    BriscolaGame = BriscolaGameActions()
    BriscolaGame.test_modus = True

    for i in range(2):
        print("RUNDOWN :", i)
        BriscolaGame.play_game()
        print(BriscolaGame.game_result_points)
