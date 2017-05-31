"""
Программа reverse.py запрашивает текст и меняет в нем порядок букв в словах на обратный.
Порядок слов сохраняется. Например: "яблоки вкусные" --> "иколбя еынсукв"')
"""

text = input("Введите текст из нескольких слов: ")
text = text.split(" ")
i = 0
text2 = []


"""
ВАРИАНТ 1:
"""
while i < len(text):
    text[i] = text[i][::-1]
    i += 1

print(" ".join(text))


"""
ВАРИАНТ 2:

for word in text:
    text2.append(word[::-1])
    i += 1
print(" ".join(text2))
"""
