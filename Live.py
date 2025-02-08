import GuessGame
import MemoryGame
import CurrencyRouletteGame


def get_valid_number(parameter, min_number, max_number):
    number = parameter
    while not number.isdigit() or int(number) < min_number or int(number) > max_number:
        number = (input(f"Please choose a number between {min_number} and {max_number}: "))
    return number


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game():
    print("Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have t guess it back.\n"
          "2. Guess Game - guess a number and see if you chose like the computer.\n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n")
    game_choice = input()
    if get_valid_number(game_choice, 1, 3):
        print("Please choose game difficulty from 1 to 5: ")
        difficulty_level = input()
        get_valid_number(difficulty_level, 1, 5)
        if game_choice == 1:
            MemoryGame.play(difficulty_level)
        elif game_choice == 2:
            GuessGame.play(difficulty_level)
        else:
            CurrencyRouletteGame.play(difficulty_level)

