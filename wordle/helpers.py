# helper functions

import random
from word import Word
from checkedletter import CheckedLetter

class Helpers:
    _dictionary: list[str]

    def __init__(self) -> None:
        self.open_dict()

    def open_dict(self) -> None:
        with open("dictionary.txt", "r") as f:
            self._dictionary = f.read().splitlines()

    def dict_word(self) -> str:
        return random.choice(self._dictionary)

    def is_word(self, t: str) -> bool:
        for i in self._dictionary:
            if t == i:
                return True
        
        return False

    def win(self, wm: list[CheckedLetter]) -> bool:
        for i in wm:
            if i.status != "match":
                return False
        return True

    def compare_word(self, 
                     user_word: Word, 
                     target_word: Word
                     ) -> list[CheckedLetter]:
        user_word_letters = user_word.get_letter_list()
        word_match = []
        for i in range(len(user_word_letters)):
            letter = user_word_letters[i]
            status = "absent"
            if target_word.contains_letter(letter):
                status = "present"
                if  target_word.index_match(letter, i):
                    status = "match"

            word_match.append(CheckedLetter(letter, status))

        return word_match

    
    def output_graphic(self, wm: list[CheckedLetter]) -> str:
        output_word = []

        for i in wm:
            if i.status == "absent":
                output_word.append(i.letter)
            elif i.status == "present":
                output_word.append(f"({i.letter})")
            elif i.status == "match":
                output_word.append(f"[{i.letter}]")

        output_msg = "".join(output_word)

        return output_msg





