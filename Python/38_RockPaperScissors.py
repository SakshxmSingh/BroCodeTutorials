import random

while True:
    choices = ("rock", "paper", "scissors")
    computer = random.choice(choices)

    player = ""
    while player not in choices:
        player = input("rock, paper, scissors?: ").lower()
        if player not in choices:
            print("Write appropriate option!!")

    print("player: "+player)
    print("computer: "+computer)

    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "scissors":           #elif player == "rock":
        print("YOU WIN!!!")                                     #    if computer == "scissors":
    elif player == "scissors" and computer == "paper":          #        print("YOU WIN!!!")
        print("YOU WIN!!!")                                     #    elif computer == "paper":
    elif player == "paper" and computer == "rock":              #        print("YOU LOSE!!!")
        print("YOU WIN!!!")                                     # --------------------------
    elif player == "scissors" and computer == "rock":           # same as above for rest
        print("YOU LOSE!!!")                                    #
    elif player == "paper" and computer == "scissors":          #
        print("YOU LOSE!!!")                                    #
    elif player == "rock" and computer == "paper":              #
        print("YOU LOSE!!!")                                    #

    play_again = input("Play again? (yes/no): ").lower()
    if play_again == "no":
        print("Thanks for playing!!")
        break
    elif play_again == "yes":
        print("Playing again!!")
        pass
    else:
        print("Unknown response, quitting the game. \nThanks for playing!!")
        break
