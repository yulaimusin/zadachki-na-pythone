"""
В файл complex_sentences_text.txt может быть записан любой текст. Программа находит в этом тексте предложения,
содержащие больше двух запятых или длина которых превышает 120 символов.

Для корректного определения конца предложения они должны оканчиваться знаком препинания (.?!) и
пробелом или переводом строки.
Найденные предложения программа записывает в файл complex_sentences.txt (если такого файла нет, то создает его) —
каждое предложение с новой строки.
"""


file = source_text = open("complex_sentences_text.txt", "r", encoding="UTF-8").read()

source_text = source_text.replace("? ", "?|").replace("! ", "!|").replace(". ", ".|")
source_text = source_text.replace("?\n", "?|").replace("!\n", "!|").replace(".\n", ".|")
source_text = source_text.replace("\n", "")
source_text = source_text.split("|")
next_text = list()
for part_of_the_text in source_text:
    comma = 0
    counter_of_symbols = 0
    for symbol in part_of_the_text:
        counter_of_symbols += 1
        if symbol == ",":
            comma += 1

    if counter_of_symbols >= 120 or comma > 2:
        next_text.append(part_of_the_text)

to_file = open("complex_sentences.txt", "w+", encoding="UTF-8")
to_file.write("\n".join(next_text))
