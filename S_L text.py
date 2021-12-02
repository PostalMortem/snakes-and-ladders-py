import random


def game():
    numberofplayers = getInt("Enter the number of players: ")
    counter = 0
    players = []
    while counter < numberofplayers:
        players.append(0)
        counter = counter + 1
    while True:
        counter = 1
        while counter <= len(players):
            print("Player", counter, "Turn.")
            players[counter-1] = roll(players[counter-1])
            print("Player", counter, "has landed on", players[counter-1])
            players[counter-1] = checkLocation(players[counter-1])
            if players[counter-1] == 100:
                print("Player", (counter), "Wins!")
                return
            else:
                counter = counter + 1



def instructions():
    print("Snakes and Ladders Rules:\nSnakes and Ladders is a simple board game where you roll a die to advance squares.")
    print("The first player to reach square #100 will win the game.\nBut watch out! The board is riddled with obstacles that can turn the tides.")
    input("If you land on a square that's at the base of a LADDER, you climb to the top.\nIf you land at the head of a SNAKE, you slide down to the bottom.\n Have fun!")


def checkLocation(spot):
    if spot == 17:
        print("You landed on a snake! You slid down to 7")
        return 7
    elif spot == 54:
        print("You landed on a snake! You slid down to 34")
        return 34
    elif spot == 62:
        print("You landed on a snake! You slid down to 64")
        return 18
    elif spot == 64:
        print("You landed on a snake! You slid down to 60")
        return 60
    elif spot == 87:
        print("You landed on a snake! You slid down to 24")
        return 24
    elif spot == 93:
        print("You landed on a snake! You slid down to 73")
        return 73
    elif spot == 95:
        print("You landed on a snake! You slid down to 75")
        return 75
    elif spot == 98:
        print("You landed on a snake! You slid down to 78")
        return 78
    elif spot == 4:
        print("You landed on a ladder! You climbed up to 14")
        return 14
    elif spot == 9:
        print("You landed on a ladder! You climbed up to 31")
        return 31
    elif spot == 20:
        print("You landed on a ladder! You climbed up to 38")
        return 38
    elif spot == 28:
        print("You landed on a ladder! You climbed up to 84")
        return 84
    elif spot == 40:
        print("You landed on a ladder! You climbed up to 59")
        return 59
    elif spot == 63:
        print("You landed on a ladder! You climbed up to 81")
        return 81
    elif spot == 71:
        print("You landed on a ladder! You climbed up to 91")
        return 91
    else:
        return spot


def roll(spot):
    input("Press enter to roll: ")
    roll = random.randint(1, 6)
    print("You rolled a", roll)
    if spot + roll > 100:
        print("You must roll to exactly 100 to win!")
        return spot
    else:
        spot = spot + roll
        return spot


def getInt(text):
    num = 0
    while True:
        try:
            num = input(text)
            num = int(num)
            if num > 1 and num <= 4:
                break
            else:
                print("Invalid number of players!")
        except:
            print("Input is not a number, try again.")
    return num

def menu(options):
    choice = ""
    print(options)
    choice = input("Enter your choice: ")
    return choice


def main():
    print("Snakes and Ladders")
    cont = "y"
    while cont.lower() == "y" or cont.lower() == "yes":
        selection = menu("1. Play ==>\n2. Instructions\nE. Exit")
        if selection == "1":
            game()
        elif selection == "2":
            instructions()
        elif selection == "e" or selection == "E":
            cont = "n"
        else:
            print("Wrong choice, try again.")

main()