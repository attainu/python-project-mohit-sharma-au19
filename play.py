from random import randint
from turn import Turn
from snakes import Snakes
from ladders import Ladders


class Play:
    while True:
        print()
        print("-------------------------SNAKES N LADDERS-------------------------")
        print()
        print("---Game Developed by Mohit Sharma---")
        play = input("Press Enter to Play or type Exit to quit the game: ")
        if play == "":
            # mode Selection
            print("Choose your mode (Single player/Multiplayer)")
            mode = input("Enter \"S\" for single player and \"M\" for multiplayer: ")
            if mode == "S" or mode == "s":
                player2 = "Computer"
                num_players = 2
            else:
                num_players = int(input("Enter number of players: "))
            player1 = input("Enter player 1 name: ")
            if (mode == "M" or mode == "m") and 5 > num_players > 1:
                player2 = input("Enter player 2 name: ")
            if 5 > num_players > 2:
                player3 = input("Enter player 3 name: ")
            if 5 > num_players > 3:
                player4 = input("Enter player 4 name: ")
                print()
            print("Thanks for Playing , Good Luck!")
            print()
            while True:
                play2 = input("Press Enter to start.")
                if play2 == "":
                    player1_score = player2_score = player3_score = player4_score = 0
                    while True:
                        if 5 > num_players > 1:
                            player1_score = Turn.turn(player1, player1_score)
                            if player1_score == 100:
                                break
                            player2_score = Turn.turn(player2, player2_score)
                            if player2_score == 100:
                                break
                        if 5 > num_players > 2:
                            player3_score = Turn.turn(player3, player3_score)
                            if player3_score == 100:
                                break
                        if 5 > num_players > 3:
                            player4_score = Turn.turn(player4, player4_score)
                            if player4_score == 100:
                                break
                    print("________________________________________________________________")

                break
        elif play == "exit" or play == "Exit":
            break
            quit
