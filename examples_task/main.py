from filtermat import check

text = input("Введите текст ")

if check(text):
    result = "В тексте есть маты."

else:
    result = "Матов не обнаружено."

print(result)

