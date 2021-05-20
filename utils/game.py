import random


class Hangman:
    def __init__(self):
        self.__possible_words = ['becode', 'learning',
                                 'mathematics', 'sessions']
        self.word_to_find = list(random.choice(self.__possible_words))
        self.lives = 5
        self.correctly_guessed_letters = list(len(self.word_to_find)*"_")
        self.wrongly_guessed_letters = []
        self.turn_count = 1

    @property
    def error_count(self):
        return len(self.wrongly_guessed_letters)

    def play(self):
        chosen_letter = input("Choose a letter : ")
        if chosen_letter in self.wrongly_guessed_letters \
                or chosen_letter in self.correctly_guessed_letters:
            print("You already tried this letter")
        elif chosen_letter in self.word_to_find:
            print("")
            print("Good guess")
            gen = (i for i in range(len(self.word_to_find))
                   if self.word_to_find[i] == chosen_letter)
            for i in gen:
                self.correctly_guessed_letters[i] = chosen_letter

        else:
            print("")
            print("Wrong guess")
            self.wrongly_guessed_letters.append(chosen_letter)
            self.lives -= 1

        self.turn_count += 1

    def game_over(self):
        print("game over...")

    def well_played(self):
        print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count}"
              f" turns with {self.error_count} error"
              f"{'s' if self.error_count > 1 else ''}!")

    def start_game(self):
        print(self.correctly_guessed_letters)
        while self.lives > 0:
            print(f"turn {self.turn_count}")
            self.play()
            print("")
            print(self.correctly_guessed_letters)
            print(f"Wrong guesses: {self.wrongly_guessed_letters}")
            print(f"{self.lives} live"
                  f"{'s' if self.lives > 1 else ''} left")
            print(f"{self.error_count} error"
                  f"{'s' if self.error_count > 1 else ''}")
            print("")
            if self.word_to_find == self.correctly_guessed_letters:
                break

        if self.lives == 0:
            self.game_over()
        else:
            self.well_played()
