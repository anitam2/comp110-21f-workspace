"""A number guessing game where a player wins points for guessing a randomly generated number between 0 and 5 inclusive.

The game has normal mode where you earn 5 points for each correct guess, and wager mode where incorrect guesses means you 
lose points and correct guesses earn points.
"""

__author__ = "730408275" 

from random import randint

points: int = 0
player: str = ""
guess: int
EMOJI: str = "\U0001f600"
EMOJI1: str = "\U0001F60D"


def greet() -> None:
    """Greet function that greets player with options."""
    print("In this game, you will try to guess a randomly generated number between 0 and 5 inclusive.")
    print("You can play normal mode and earn points for every correct guess or play wager mode where you can wager some of your existing points.")
    global player
    player = input("What is your name: ")


def option_one() -> None:
    """First option in game (normal mode)."""
    global points
    print(f"Hi {player} {EMOJI}!")
    print("In this mode, every time you guess the number correctly you will gain 5 points.")
    guess = int(input("What is your guess: "))

    random_number: int = randint(0, 5)
    print(random_number)
    if guess == random_number:
        points += 5


def option_two(a: int) -> int:
    """Second option in game (wager mode)."""
    global points
    print(f"Hi {player} {EMOJI}!")
    print(f"In this mode, you can wager your existing points {EMOJI1}. If you guess the number incorrectly, you will lose 3 points.")
    print("Guess correctly and you gain 8 points.")
    
    guess = int(input("What is your guess: "))

    random_number: int = randint(0, 5)
    print(random_number)
    if guess == random_number:
        points += 8
    else:
        points -= 3
    return points


def main() -> None:
    """Program's entrypoint."""
    global points
    greet()
    choice: str = ""
    
    while choice != "exit":
        print(f"Your total number of points is: {points}")
        choice = input("Would you like to exit the game, enter normal mode, or enter wager mode (exit, normal, or wager): ")
        if choice == "exit":
            print(f"Goodbye, thanks for playing! You scored {points} total points {EMOJI}!")
        elif choice == "normal":
            option_one()
        elif choice == "wager":
            points = option_two(points)


if __name__ == "__main__":
    main()
