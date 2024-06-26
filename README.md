# python_projects

## Disclaimer

I didn't come up with these projects originally as this repo is my own personal practical record of the projects from the following books:

- [Big Book Small Python Projects by AL SWEIGART](https://inventwithpython.com/bigbookpython/)
- [djangoprojectscookbook: Release 2.0 Agiliq](https://books.agiliq.com/projects/djenofdjango/en/latest/)

# Projects

## Python Project 1: [Bagels](/Python_proj_book/bagels.py)

A deductive logic game

- Goal: to guess a secret three digit number based on clues.
- Number of tries: 10

### Hints

- "Pico" when your guess has correct digit in the wrong place
- "Fermi": when your guess has a correct digit in the correct place.
- "Bagels": if your guess has no correct digits.

When you run bagels.py, the output will look like this:

```
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
Pico One digit is correct but in the wrong position.
Fermi One digit is correct and in the right position.
Bagels No digit is correct.
I have thought up a number.
You have 10 guesses to get it.
Guess #1:
> 123
Pico
Guess #2:
> 456
Bagels
Guess #3:
> 178
Pico Pico
--snip--
Guess #7:
> 791
Fermi Fermi
Guess #8:
> 701
You got it!
Do you want to play again? (yes or no)
> no
Thanks for playing!
```

Took me this long to get a 5 digit number with a 100 limit

```
Guess #41:
> 94187
You got it.
```

## Django Project 1: [A Personal CD Library](Django_proj_book/djen_project/cd_library/)

The First Django Project of The series from the [Django Cookbook by Agiliq](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/)
