from game import Game
from word import Word
from checkedletter import CheckedLetter 

def test_letters_remaining() -> None: 

    game = Game()

    word_match = [
        CheckedLetter("s", "absent"),
        CheckedLetter("l", "absent"),
        CheckedLetter("a", "absent"),
        CheckedLetter("t", "absent"),
        CheckedLetter("e", "absent")
    ]

    game.update_letters_remaining(word_match)
    result = game.letters_remaining
    assert len(result) == 21

