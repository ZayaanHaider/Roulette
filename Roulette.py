import random

# Game Intro
print("Welcome to Roulette")
print("Roulette starts with players making bets.")
print("The croupier (or dealer) throws a ball into the spinning roulette wheel. Players can still makes bets within the process.")
print("While the ball is rolling at the roulette wheel, the croupier/dealer announces: \"No more bets.\" At that point players are NOT allowed making bets The ball lands on a number IN the roulette wheel. If there are winners who bet the number, section OR color, they will be rewarded according of their betting odds.")

# Main Game Loop
keep_running = "yes"
while keep_running == "yes":

    # Ball Lands On...
    '''
    x = random.randint(0, 1)
    if x == 0:
        ball = "red"
    elif x == 1:
        ball = "black"
    '''
    # Zayaan, we will probably need to make a list
    # which will
    x = random.randint(0, 37)
    pocket = [
        "0",
        "00",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
        "31",
        "32",
        "33",
        "34",
        "35",
        "36"
    ]
    # TODO: Match Numbers & Colors in List Below
    color = [
        "green",
        "green",
    ]

    # Player Bets On...
    player_selection = input("Red or black?: ")

    # Display Outcome
    if ball == player_selection:
        print("You win!!!!!")
    else:
        print("YOU LOSE")

    # Keep Playing?
    keep_running = input("Would you like to continue? Enter 'yes' for yes, 'no' for no: ")

    # Say Goodbye
    if keep_running != "yes":
        print("Thanks for playing. Goodbye!")

    
