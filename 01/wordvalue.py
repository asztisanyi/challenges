from data import DICTIONARY, LETTER_SCORES
import re
TEST_WORDS = ('bob', 'julian', 'pybites', 'quit', 'barbeque')

def load_words():
    """Load dictionary into a list and return list"""
    loaded_w = open(DICTIONARY, "r")
    word_list = [re.sub('\W+', '', n.strip(), ) for n in list(loaded_w)]
    loaded_w.close()
    return word_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word = list(word.upper().strip())
    word_value = 0
    for letter in word:
        word_value += LETTER_SCORES[letter]
    return word_value


def max_word_value(list_of_words=None):
    if list_of_words is None:
        list_of_words = load_words()
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    values = [calc_word_value(n) for n in list_of_words]
    ind = values.index(max(values))
    word = list_of_words[ind].lower()
    return word

