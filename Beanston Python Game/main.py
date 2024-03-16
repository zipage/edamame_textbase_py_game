# INTRODUCE PLAYER TO THE GAME
# if player select "start new game"
# https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3
# https://grantjenks.com/docs/freegames/


def game():
    # starts the game for the player
    # gameStart = input("You begin your adventure...")

    # ARE YOU READY TO START THE GAME
    gameStart = input("Are you ready to start our adventure, Bean? (y / n): ")

    # player selects yes:
    if gameStart.lower() == "y":
        print("Perfect! let's get ready for our adventure.")
        start = True
        inventory = []

    # to allow a player to select and view their inventory at any point

    # The game flow is controlled by the start variable. If start is True, the game will continue, otherwise, it will restart back to the main menu
    print(
        "Welcome to Edamame in the realm of Urad. You come to here after graduation to start your first adventures."
    )

    print(
        "Although you don't know exactly what, you plan on seeing what the realm has to offer."
    )

    # START THE TALE
    print(
        "*You found a small inn to stay at while to make your bearings in this new town. You step outside your room door.*"
    )

    # the choice variable will be used every single time the player has to make as choice
    # the answer variable will be used to create a boolean (if/else)

    choice = input(
        "do you go LEFT (left) to the FRONT DESK or go RIGHT (right) to go OUTSIDE? (left / right): "
    )

    # if the player goes the LEFT
    if choice.lower() == "left":
        print(
            "*you take a right and walk towards the front desk. You speak with the reception and you are give a Map.*"
        )
        print("###--- You have been given a MAP OF URAD ---###")

    # add a map to the players inventory
    inventory.append("Map of Urad")

    # if the play goes to the RIGHT
    if choice == False:
        print(
            "*you head outside and are greeted with the sun shining and busy market sounds in the distance.*"
        )
        print(
            "*you follow the sounds of and make your way towards the market place. You see a stranger approach you.*"
        )
