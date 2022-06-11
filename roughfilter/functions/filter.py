from typing import List, Optional

from roughfilter.bases import kit_rough_words
from roughfilter.functions.word import Word


class RoughFilter:
    def __init__(self, word: Word) -> None:
        self.word = word

    def get_rough_words(self) -> List[str]:
        return kit_rough_words.words

    def find_vulgar_words(self) -> Optional[str]:

        word = (
            self.word.replace_identically_looking_letters().revert_transcription()
        )

        if response := word.search_in_kit_words(self.get_rough_words()):
            return response

        elif response := (word.to_base_form().find_vulgar_words()):
            return response

    def overall_performance(self) -> Optional[str]:
        return self.find_vulgar_words()
