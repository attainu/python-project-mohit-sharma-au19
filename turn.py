from random import randint
from ladders import Ladders
from snakes import Snakes


class Turn:
    def turn(player, score):  # Turn function
        print()
        print("Its", player, "turn.")
        roll2 = input("Press enter to Roll the dice")
        print()
        if roll2 == "":
            a = randint(1, 6)  # player dice roll
            print(player, "rolled the dice")
            print(player, "It is a", a)
            score += a
            if score <= 100:
                lad = Ladders.ladders(score)  # checking for ladders for player
                if lad != score:
                    print("There's a ladder!", player, "climbed up.")
                    score = lad
                snk = Snakes.snakes(score)
                if snk != score:  # checking for snakes for player
                    print(player, "Got a bite from a snake!", player, "fall down!")
                    score = snk
                print(player, "is now at ", score)
            else:  # checks if player score is not grater than 100
                score -= a
                print(player, "can't move.")
                print(player, "is still on box", score)
            if score == 100:
                print()
                print(player, "Wins! , A big Congratulations")

            return score