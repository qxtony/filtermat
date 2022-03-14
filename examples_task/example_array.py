from filtermat import check

text = input("Введите мат, или текст с матом: ")
result = " ".join(check(text, array=True))

print(f"Найденные маты в тексте: {result}")

