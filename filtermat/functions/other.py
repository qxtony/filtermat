from regex import findall

from ..configurations import (
    TRANSLITE_SYMBOLS,
    TRANSLATE_RUSSIAN, MORPH, FILTER_MAT
)

from ..files import mats

def array_mats():
    return mats.mats


def standard_form(word):
    analysis = MORPH.parse(word)[0]
    return analysis.normal_form


def format_translate(word):
    return "".join(
        map(
            lambda x: TRANSLITE_SYMBOLS.get(x) or x,
            word
        )
    )


def translate(word):

    data = "".join(map(lambda x: TRANSLATE_RUSSIAN.get(x) or x, word))
    return data


def join_symbols(words):
    return "".join(
        map(
            lambda x: x if x.isalpha() else f" {x}",
            words
        )
    )


def re_find(word):
    return findall(FILTER_MAT, word)


def performance_any(
    word, letter="*", ignore_form=False,
    ignore_translate=False, regex=True
):

    word = format_translate(word.replace("*", letter))

    if not ignore_translate:
        word = translate(word)

    if not ignore_form:
        word = standard_form(word)

    if not word in array_mats() and regex:
        return re_find(word)

    return word in array_mats()

