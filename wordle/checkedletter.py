# checkedletter class

class CheckedLetter:
    letter: str
    status: str

    def __init__(self, l: str, s: str) -> None:
        self.letter = l
        self.status = s
