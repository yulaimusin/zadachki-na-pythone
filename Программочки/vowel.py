"""
Программа vowel.py запрашивает у пользователя слово на английском языке,
удаляет из него все согласные буквы и выводит оставшиеся гласные.
"""


the_word = input('Введите слово на английском (например, "programming"): ')
vowel = "aeiouy"
only_vowel_symbols = list()
for symbol in the_word:
    if symbol in vowel:
        only_vowel_symbols.append(symbol)

print("".join(only_vowel_symbols))
