"""
Программа words_stat.py считает сколько раз в тексте встречаются слова.
Текст находится в файле words_stat_text.txt.
Также рядом с программой лежит файл words_stat_punctuation.txt, который содержит знаки препинания,
встречающиеся в тексте. Каждый знак записан с новой строки.

После запуска программа создает файл words_stat.txt с перечислением всех слов текста в алфавитном порядке
(сначала слова, начинающиеся с прописной буквы и лишь затем слова, начинающиеся со строчной буквы).
Аналогичную информацию выводит на экран.
После слова идет двоеточие, пробел и число — сколько раз это слово встречается в тексте.
"""


the_text = open("words_stat_text.txt", "r", encoding="UTF-8").read()
separator_symbols = open("words_stat_punctuation.txt", "r", encoding="UTF-8").read()
# <заменяем все знаки препинания и абзацы из файла на пробелы
for separator in separator_symbols:
    the_text = the_text.replace(separator, " ")
# </заменяем все знаки препинания и абзацы из файла на пробелы
# <удаляем лишние пробелы
the_text = the_text.replace("  ", " ").replace("  ", " ")
if the_text[-1] == " ":
    the_text = the_text[:-1]
# </удаляем лишние пробелы
the_text = the_text.split(" ")  # преобразуем строку в список
new_text = list()
for word in the_text:
    new_text.append(word + ": " + str(the_text.count(word)))

new_text = list(set(new_text))  # преобразуем список в множество и затем обратно в список
new_text.sort()    # сортируем список
#print(new_text)
to_file = open("words_stat.txt", "w+", encoding="UTF-8")
to_file.write("\n".join(new_text))
for word in new_text:
    print(word)
