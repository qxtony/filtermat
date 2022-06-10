from roughfilter import search_obscene_words


def main():
    sentences = input()
    print(search_obscene_words(sentences))


if __name__ == "__main__":
    main()
