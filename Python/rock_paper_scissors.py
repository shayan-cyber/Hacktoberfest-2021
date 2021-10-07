from random import randint

a = ["Rock", "Paper", "Scissors"]

computer = a[randint(0, 2)]

player = True

while player == True:
    player = input("Rock, Paper, Scissors? ")

    print("Opponent chose {}".format(computer))

    if player == computer:
        print("It's a tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose :(", computer, "covers", player)
        else:
            print("You win!", player, "breaks", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose :(", computer, "cuts", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose :(", computer, "breaks", player)
        else:
            print("You win!", player, "cuts", computer)
    else:
        print("Oops, please check your spelling!")

    player = True
    computer = a[randint(0, 2)]