# tests for the word class

from word import Word
from helpers import Helpers

helpers = Helpers()

def test_initial_state_dict_word() -> None:
    no_input_word = Word(helpers.dict_word())

    result_text = no_input_word.get_text()
    result_letter_list = no_input_word.get_letter_list()

    assert type(result_text) is str
    assert isinstance(result_letter_list, list)
    assert all(isinstance(x, str) for x in result_letter_list) 

def test_initital_state_with_input() -> None:
    input_word1 = Word('fire')

    result_text1 = input_word1.get_text()

    result_letter_list1 = input_word1.get_letter_list()

    assert type(result_text1) is str

    assert isinstance(result_letter_list1, list)
    assert all(isinstance(x, str) for x in result_letter_list1)


