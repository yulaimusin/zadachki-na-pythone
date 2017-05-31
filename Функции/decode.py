"""
Секретной службе удалось выяснить, что для кодирования секретных сообщений
Джеймс Бонд использует шифр Цезаря (https://ru.wikipedia.org/wiki/Шифр_Цезаря).
Еще аналитики узнали, что Бонд каждый раз меняет ключ сдвига, а также подписывает
все исходные сообщения тремя цифрами — 007, например так «Завтра в 8 часов на заброшенном складе. 007»
Универсальная функция decode расшифровывает сообщения Бонда.
Функция принимает один аргумент — зашифрованный текст и возвращает результат.
"""


def decode(coded_text):
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюяѐАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !,-0123456789"
    code_alphabet = list(alphabet)
    key = len(alphabet)
    while key > 0:
        var = code_alphabet.pop(-1)
        code_alphabet.insert(0, var)
        key -= 1

        encoded_text = list()
        for symbol in coded_text:
            counter = 0

            while counter < len(alphabet):
                if symbol in alphabet[counter]:
                    encoded_text.append(code_alphabet[counter])

                counter += 1

        encoded_text = "".join(encoded_text)
        if "007" in encoded_text:
            return encoded_text

    return "Расшифровка не удалась"


print(decode("Бджоу!118-!тспшоп!гькейуж!об!тгѐиэ"))  # Агент, срочно выйдите на связь! 007
