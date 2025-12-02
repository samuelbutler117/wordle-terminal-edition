from word import Word
from checkedletter import CheckedLetter
from helpers import Helpers

class Game:
    target_word: Word
    helpers: Helpers
    letters_remaining: list[str]
    letters_eliminated: list[str]


    def __init__(self) -> None:
        self.helper = Helpers()
        self.target_word = Word(self.helper.dict_word())
        self.letters_remaining = [
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "p", "w", "x", "y", "z", 
        ]
        self.letters_eliminated = []


    def play(self) -> None: 
        self.game_loop()

    def validate_input(self, prompt: str) -> str:
        while True:
            guess = input(prompt)
            if self.helper.is_word(guess):
                return guess
            else:
                print("Not in game dictionary, try a different word ")

    def update_letters_remaining(self, wm: list[CheckedLetter]) -> None:
        for l in wm:
            if l.letter in self.letters_remaining:
                if l.status == "absent":
                    self.letters_remaining.remove(l.letter)
                    self.letters_eliminated.append(l.letter) 
       
    def game_loop(self) -> None:
        print("Welcome to Wordle Terminal Edition! "
              "Guess the Wordle in 6 tries. \n"
              "Letters marked with [x] are in the Wordle "
              "and in the correct spot. \n"
              "Letters marked with (x) are in the Wordle, " 
              "but not in the right spot. \n"
              "Good luck! ")
        attempts = 0
        while attempts < 6:
            guess = self.validate_input("Enter a 5 letter word: ")
            user_word = Word(guess)
            word_match = self.helper.compare_word(user_word, self.target_word)
            output_msg = self.helper.output_graphic(word_match)
            print(output_msg)
            if self.helper.win(word_match):
                print("You win! ")
                return

            attempts += 1

            self.update_letters_remaining(word_match)
            print(f"you have eliminated: {self.letters_eliminated} ")
            print(f"Letters remaining: {self.letters_remaining} ")
            print(f"attempts remaining: {6-attempts} ")

            
        
        print("You ran out of attempts, you lose :(" )
        print(f"The word was {self.target_word.get_text()} ")





    
