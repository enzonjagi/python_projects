"""
Bagels, a deductive logic game.
Original Idea By Al Sweigart al@inventwithpython.com

Any modifications or ideas will be by me: Umar Ndungo
My Github: @enzonjagi
Email: omarnjagi@gmail.com
Main Email: amosndungo@gmail.com
"""

import random

NUM_DIGITS = 3  # Try Setting This to 1 or 10
MAX_GUESSES = 10  # Try changing to 1 or 100


def main():
    print(
        """
        Bagels, a deductive logic game.
        Original Idea By Al Sweigart al@inventwithpython.com

        Any modifications or ideas will be by me: Umar Ndungo
        My Github: @enzonjagi
        Email: omarnjagi@gmail.com
        Main Email: amosndungo@gmail.com

        I am thinking of a 3-digit number. Try to guess what it is.
        Here are some clues:
        When I say: That means:
        Pico        One digit is correct but in the wrong position.
        Fermi       One digit is correct and in the right position.
        Bagels      No digit is correct.

        For example, if the secret number was 248 and your guess was 843, the 
        clues would be Fermi Pico.""".format(
            NUM_DIGITS
        )
    )

    while True:
        # Main game loop

        # This Stores the secret number
        # the player needs to guess
        secretNum = getSecretNum()
        print("I have thought of a number.")
        print(f" You have {MAX_GUESSES} guesses to get it.")

        numGuesses = 1

        while numGuesses < MAX_GUESSES:
            guess = ""
            # Keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isalnum():
                print(f"Guess #{numGuesses}: ")
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # Correct guess
            if numGuesses >= MAX_GUESSES:
                print("You've run out of guesses")
                print(f"The answer was {secretNum}")

        # Ask player if they want to play again.
        print("Play Again?(yes/no)")
        if not input("> ").startswith("y"):
            break

    print("Thanks for playing!!")


def getSecretNum():
    """
    Returns a string made up of NUM_DIGITS unique random digits.
    """

    numbers = list(
        "0123456789abcdefghijklmnopqrstuvwxyz"
    )  # Create a list of digits from 0 to 9
    random.shuffle(numbers)  # Shuffle the numbers into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum


def getClues(guess, secretNum):
    """
    Returns a string with Pico, fermi, or bagels
    clues for a guess and secret number pair.

    """

    if guess == secretNum:
        return "You got it."

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit in correct position.
            clues.append("Fermi")
        elif guess[i] in secretNum:
            # A correct guess in wrong position.
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels."
    else:
        # Sort the clues into alphabetical order so their
        # original order doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues
        return " ".join(clues)


if __name__ == "__main__":
    # if the program is run(instead of imported), run the game:
    main()
