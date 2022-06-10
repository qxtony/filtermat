from typing import List

from regex import findall

from roughfilter.configurations import (
    morph,
    re_filter,
    transcriptions,
    translations,
)


class Word:
    def __init__(self, word: str) -> None:
        self.word_tested = word

    def to_base_form(self) -> str:
        parsed_word = morph.parse(self.word_tested)[0]
        self.word_tested = parsed_word.normal_form

        return self

    def replace_identically_looking_letters(self) -> str:
        def get_symbol(symbol: str) -> str:
            return transcriptions.get(symbol) or symbol

        self.word_tested = "".join(map(get_symbol, self.word_tested))
        return self

    def revert_transcription(self) -> str:
        def get_symbol(symbol: str) -> str:
            return translations.get(symbol) or symbol

        self.word_tested = "".join(map(get_symbol, self.word_tested))
        return self

    def find_vulgar_words(self) -> List[str]:
        if result := findall(re_filter, self.word_tested):
            self.word_tested = result
            return self

    def is_startswith_or_endswith(self, rough_words: List[str]) -> bool:
        for word in rough_words:
            if (
                self.word_tested.startswith(word) or
                self.word_tested.endswith(word)
            ):
                return True

    def search_in_kit_words(self, rough_words: List[str]):
        if self.word_tested in rough_words:
            return self

        elif self.is_startswith_or_endswith(rough_words):
            return self
 