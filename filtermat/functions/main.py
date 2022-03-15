from .other import performance_any, join_symbols


def check(
    words, ignore_replace=False, ignore_form=False,
    ignore_translate=False, regex=True, array=False
):

    mats = []

    for word in join_symbols(words.replace("_", " ")).split():

        if performance_any(
            word, ignore_form=ignore_form,
            ignore_translate=ignore_translate,
            regex=regex
        ):
            mats.append(word)

        elif "*" in word:

            if ignore_replace:
                continue

            for letter in LETTERS:

                if performance_any(word, letter, ignore_form, ignore_translate, regex):
                    mats.append(word)

    if array:
        return mats

    if mats:
        return True

    return False

