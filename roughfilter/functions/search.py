from typing import List, Union

from roughfilter.functions.filter import RoughFilter
from roughfilter.functions.word import Word


def search_obscene_words(
    text: str, get_list_words: bool = False
) -> Union[List[str], bool]:

    obscene_words = []

    for word in text.lower().split():
        word_instance = Word(word)
        check = RoughFilter(word_instance)

        if check.overall_performance():
            obscene_words.append(word)

    return make_a_return(obscene_words, get_list_words)


def make_a_return(obscene_words, get_list_words):
    if get_list_words:
        return obscene_words

    return any(obscene_words)
