from helpers import Helpers
from word import Word
from checkedletter import CheckedLetter

def test_compare_word_all_different_letters() -> None:
    helpers = Helpers()
    word1 = Word("adapt")
    word2 = Word("being")
    
    word_match = helpers.compare_word(word1, word2)

    for i in range(len(word_match)):
        assert word_match[i].letter == word1.get_letter_list()[i]
        assert word_match[i].status == "absent"

def test_compare_word_all_same_letters() -> None:

    helpers = Helpers()
    word1 = Word("slate")
    word2 = Word("slate")

    word_match = helpers.compare_word(word1, word2)

    for i in range(len(word_match)):
        assert word_match[i].letter == word1.get_letter_list()[i]
        assert word_match[i].letter == word2.get_letter_list()[i]
        assert word_match[i].status == "match"

def test_compare_word_mixed_letters() -> None:

    helpers = Helpers()

    word1 = Word("wreck")
    word2 = Word("water")

    word_match = helpers.compare_word(word1, word2)

    assert word_match[0].status == "match"
    assert word_match[1].status == "present"
    assert word_match[2].status == "present"
    assert word_match[3].status == "absent"
    assert word_match[4].status == "absent"

def test_is_word() -> None: 
    helpers = Helpers()

    word = helpers.is_word("watts")
    word2 = helpers.is_word("stand")

    not_word = helpers.is_word("blaby")
    not_word2 = helpers.is_word("blurp")

    assert word == True
    assert word2 == True
    assert not_word == False
    assert not_word2 == False

def test_output_graphic() -> None:
    helpers = Helpers()

    word_match = [
        CheckedLetter("a", "absent"),
        CheckedLetter("b", "present"),
        CheckedLetter("c", "match")
    ]


    result = helpers.output_graphic(word_match)

    assert result == "a(b)[c]"

def test_win_true() -> None: 
    helpers = Helpers()

    word_match = [
        CheckedLetter("a", "match"),
        CheckedLetter("b", "match"),
        CheckedLetter("c", "match")
    ]

    result = helpers.win(word_match)

    assert result == True

def test_win_false() -> None: 
    helpers = Helpers()

    word_match = [
        CheckedLetter("a", "absent"),
        CheckedLetter("b", "present"),
        CheckedLetter("c", "match")
    ]

    result = helpers.win(word_match)

    assert result == False







    





