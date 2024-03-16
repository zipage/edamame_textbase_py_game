import pygame


# start of the game here
def start_game_menu():
    print("EDAMAME ADVENTURES")
    print("1. start new game")
    print("2. continue saved game")
    print("3. quit")

    # let play chose via 1/2/3
    choice = input("how shall we begin, Adventurer? (1/2/3): ")
    return choice


# if player select "start new game"
def game():
    # ARE YOU READY TO START THE GAME
    gameStart = input("STRANGER: Are you ready to start our adventure, Bean? (y / n): ")

    # player selects yes:
    if gameStart.lower() == "y":
        print("STRANGER: Perfect! let's get ready for our adventure.")

        # The game flow is controlled by the start variable. If start is True, the game will continue, otherwise, it will restart back to the main menu
        start = True
        inventory = []

    # player selects no:
    else:
        print(
            "STRANGER: Alright, no hard feeliings! You can find me when you change your mind."
        )


def main():
    while True:

        # start_game_menu the function for a menu to the player to start a new game, continue saved game, or quit
        # choice variable has the players choice and 'game' function is clal when player wants to start a new game
        choice = start_game_menu()
        if choice == "1":
            game()
        elif choice == "2":
            print("Saved game not implemented")
        elif choice == "3":
            print("Thanks for playing! Come back any time, Adventurer.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
# if the player says no then restart the game back to the main menu
# if the player says yes then the story continues as follows
# https://blackbox.ai/share/0febc8ac-e60a-468e-94c0-2f459690aef7 > contiune game code
