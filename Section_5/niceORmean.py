#
# Python: 3.9.6
#
# Author: Kenzie M
#
# Purpose: The Tech Academy Python Course - Create a game and learn:
#          -How to pass variables from function to function
#          -Creating a functional, text-based game



def start(nice = 0, mean = 0, name = ""):
    # get users name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)


def describe_game(name):
    """
        check if this is a new game or not.
        if its new, get the user's name.
        if its old, thank the player for
        playing again and continue with the game.
    """
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("""\nIn this game, you will be greeted
by several different people. You can
choose to be nice or mean, but at the
end of the game your fate will be
sealed by your actions.""")
                    stop = False
    return name


def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a conversation. \nWill you be nice or mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("The stranger walks away smiling...")
            nice = nice + 1
            stop = False
        if pick == "m":
            print("The stranger glares at you menacingly and storms off...")
            mean = mean + 1
            stop = False
    score(nice, mean, name) # pass the three variables to score()


def show_score(nice, mean, name):
    print("\n{}, your current total: \n(Nice: {}, Mean: {})".format(name, nice, mean))


def score(nice, mean, name):
    # score function is being passed the values stored in the 3 variables
    if nice > 2: # if condition is valid, call win function and pass in variables
        win(nice, mean, name)
    if mean > 2: # if condition is valid, call lose function and pass vars
        lose(nice, mean, name)
    else:   # else, call nice_mean function and pass vars
        nice_mean(nice, mean, name)


def win(nice, mean, name):
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    again(nice, mean, name)


def lose(nice, mean, name):
    print("\nAhhh, too bad, game over! \n{}, you're a meanie and you lose!".format(name))
    again(nice, mean, name)


def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n): \n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (y) for 'YES' or (n) for 'NO'.")


def reset(nice, mean, name):
    nice = 0
    mean = 0
    # keep the name variable the same
    start(nice, mean, name)


    


if __name__ == "__main__":
    start()
