import random
import re
from typing import List

from utils.string_utils import pluralize

HANGMAN_PICS = [
    """
   +---+
        |
        |
        |
       ===""",
    """
    +---+
    O   |
    |   |
        |
       ===""",
    """
    +---+
    O   |
   /|   |
        |
       ===""",
    """
    +---+
    O   |
   /|\\  |
        |
       ===""",
    """
    +---+
    O   |
   /|\\  |
   /    |
       ===""",
    """
    +---+
    O   |
   /|\\  |
   / \\  |
       ===""",
]


class Hangman:
    def __init__(self) -> None:
        """Hangman constructor"""
        self.__possible_words: List[str] = [
            "becode",
            "learning",
            "mathematics",
            "sessions",
        ]
        self.initialize_game()

    @property
    def error_count(self) -> int:
        return len(self.wrongly_guessed_letters)

    def initialize_game(self):
        self.word_to_find: List[str] = list(
            random.choice(self.__possible_words)
        )
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = list(
            len(self.word_to_find) * "_"
        )
        self.turn_count: int = 1
        self.wrongly_guessed_letters: List[str] = []

    def play(self) -> None:
        """This function is in charge of asking the user's input and process it
        and print the result of the turn
        """
        chosen_letter = input("Choose a letter : ").lower()
        if not re.match("^[A-z]$", chosen_letter):
            print("Please enter a valid letter")
            self.play()
        elif (
            chosen_letter in self.wrongly_guessed_letters
            or chosen_letter in self.correctly_guessed_letters
        ):
            print("You already tried this letter")
            self.play()
        else:
            if chosen_letter in self.word_to_find:
                # adding an empty line for more readability
                print("")
                print("Good guess")
                gen = (
                    i
                    for i in range(len(self.word_to_find))
                    if self.word_to_find[i] == chosen_letter
                )
                for i in gen:
                    self.correctly_guessed_letters[i] = chosen_letter

            else:
                # adding an empty line for more readability
                print("")
                print("Wrong guess")
                self.wrongly_guessed_letters.append(chosen_letter)
                self.lives -= 1

            self.turn_count += 1

    def game_over(self) -> None:
        """Function in charge of printing when the game is over"""
        print("game over...")

    def well_played(self) -> None:
        """function called when someone beat the game"""
        print(
            f"You found the word: {''.join(self.word_to_find)} in "
            f"{self.turn_count-1} turns with {self.error_count} error"
            f"{pluralize(self.error_count)}!"
        )

    def play_again(self) -> None:
        """This is in charge of Asking the user if he wants to play again or
        not and if yes to reinitialize the game
        """
        user_answer = input("Play again y/n: ").lower()
        if user_answer == "y":
            self.initialize_game()
            self.start_game()
        elif user_answer != "n":
            self.play_again()

    def start_game(self) -> None:
        """Function in charge of the game workflow"""
        print(self.correctly_guessed_letters)
        while self.lives > 0:
            print(f"turn {self.turn_count}")
            # this draws the Hangman
            print(HANGMAN_PICS[self.error_count])
            self.play()
            # adding an empty line for more readability
            print("")
            print(self.correctly_guessed_letters)
            print(f"Wrong guesses: {self.wrongly_guessed_letters}")
            print(f"{self.lives} live" f"{pluralize(self.lives)} left")
            print(f"{self.error_count} error" f"{pluralize(self.error_count)}")
            print("")
            if self.word_to_find == self.correctly_guessed_letters:
                break

        if self.lives == 0:
            print(HANGMAN_PICS[self.error_count])
            self.game_over()
        else:
            self.well_played()

        self.play_again()
