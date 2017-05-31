"""
Функция encode кодирует переданную в неё строку с помощью шифра Цезаря (https://ru.wikipedia.org/wiki/Шифр_Цезаря).
Функция принимает два аргумента:
1.текст для кодирования;
2.необязательный аргумент key (ключ сдвига) со значением по умолчанию 1.
"""


def encode(text_007, key=1):
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюяѐАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !,-0123456789"
    code_alphabet = list(alphabet)
    """
    Если нужно сдвинуть в обратную сторону, то есть назад:
    while key > 0:
        var = code_alphabet.pop(-1)
        code_alphabet.insert(0, var)
        key -= 1
    """
    while key > 0:
        var = code_alphabet.pop(0)
        code_alphabet.append(var)
        key -= 1

    # Шифрование
    the_code = list()
    for symbol in text_007:
        counter = 0

        while counter < len(alphabet):
            if symbol in alphabet[counter]:
                the_code.append(code_alphabet[counter])

            counter += 1

    return "".join(the_code)


"""
Пример использования:
"""
text_007 = encode(text_007="Агент 007, срочно выйдите на связь")
print(text_007)  # Бджоу!118-!тспшоп!гькейуж!об!тгѐиэ
