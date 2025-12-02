# word class
class Word:
    _text: str
    _letter_list: list[str]

    def __init__(self, t: str) -> None:
        self._text = t
        self.split_word(self._text)

    def split_word(self, t: str) -> None:
        self._letter_list = []
        for c in t:
            self._letter_list.append(c)

    def get_text(self) -> str:
        return self._text

    def get_letter_list(self) -> list[str]:
        return self._letter_list

    def contains_letter(self, letter: str) -> bool:
        for c in self._letter_list: 
            if c == letter:
                return True
            
        return False

    def index_match(self, letter: str, index: int) -> bool:
        if letter == self._letter_list[index]:
            return True
        else:
            return False
        

