<h1 align="center" name="name">RoughFilter</h1>
<p align="center">
    <em>
        With this library, you can easily catch rude expressions in text.<br>
        Two technologies are used: Regular expressions, as well as manual search through the list words.
    </em>
</p>

<p align="center">
    <a href="https://github.com/qxtony/roughfilter/issues">
        <img src="https://img.shields.io/github/issues/qxtony/roughfilter" alt="Issues">
    </a>
    <a href="https://pypi.org/project/roughfilter/">
        <img src="https://img.shields.io/pypi/v/roughfilter?colorB=brightgreen" alt="Package version">
    </a>
    <a href="https://github.com/qxtony/roughfilter/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/qxtony/roughfilter.svg" alt="License">
    </a>
</p>

## Installation

Stable version:

```bash
pip install -U roughfilter
```
## Quickstart
An example of a program for a simple search for rough expressions.

```python
from roughfilter import search_obscene_words


def main():
    sentences = input()
    print(search_obscene_words(sentences))


if __name__ == "__main__":
    main()

```


As well as using the library to display the found rough expressions:
```python
from roughfilter import search_obscene_words


def main():
    sentences = input()
    found_rough_expressions = search_obscene_words(sentences, get_list_words=True)
    print(" ".join(found_rough_expressions))


if __name__ == "__main__":
    main()

```
