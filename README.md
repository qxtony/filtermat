<h1 align="center" name="name">Library FilterMat</h1>
<p align="center">
    <em>This library allows you to find the mat in the text.</em>
</p>

<p align="center">
    <a href="https://github.com/qxtony/filtermat/issues">
        <img src="https://img.shields.io/github/issues/qxtony/filtermat" alt="Issues">
    </a>
    <a href="https://pypi.org/project/filtermat/">
        <img src="https://img.shields.io/pypi/v/filtermat?colorB=brightgreen" alt="Package version">
    </a>
    <a href="https://github.com/qxtony/filtermat/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/qxtony/filtermat.svg" alt="License">
    </a>
</p>

## Installation

Stable version:

```bash
pip install -U filtermat
```
## Quickstart
The first program to search for a mate in a sentence.
```python
from filtermat import check

text = input("Введите предложение: ")

if check(text):
    result = "В тексте есть маты"

else:
    result = "Матов не обнаружено"

print(result)
```


As well as a code that shows exactly which mats are found:
```python
from filtermat import check

text = input("Введите предложение: ")
result = ", ".join(check(text, array=True))

print(f"В тексте найдены маты: {result}")
```
You can also remove some text checks. There are only 4 text transformations: Search for an asterisk in the text; Formation of the word in the initial form, singular, nominative; Translation of transliteration into plain text; Checking with regular expressions.

Examples:
```python
from filtermat import check

text = input("Введите предложение: ")
result = ", ".join(check(text, ignore_replace=True)) # Ignore search for an asterisk in the text.

print(f"В тексте найдены маты: {result}")
```
```python
from filtermat import check

text = input("Введите предложение: ")
result = ", ".join(check(text, ignore_form=True)) # Ignore formation of the word in the initial form, singular, nominative.

print(f"В тексте найдены маты: {result}")
```
```python
from filtermat import check

text = input("Введите предложение: ")
result = ", ".join(check(text, ignore_translate=True)) # Ignore translation of transliteration into plain text.

print(f"В тексте найдены маты: {result}")
```
```python
from filtermat import check

text = input("Введите предложение: ")
result = ", ".join(check(text, regex=False)) # Ignore checking with regular expressions.

print(f"В тексте найдены маты: {result}")
```

