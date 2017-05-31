"""
ВЫРЕЗАЕМ ЛИШНИЕ СИМВОЛЫ
Люди часто, когда пишут комментарии в интернете, ставят несколько восклицательных или вопросительных знаков.
Текст от этого становится громоздким и его трудно читать.

Функция cut_extra_characters первым параметром принимает текст комментария,
а вторым - набор символов, повторы которых нужно убирать.
"""


def cut_extra_characters(text, marks):
    mark_counter = 0
    while mark_counter < len(marks):
        double_mark = marks[mark_counter] + marks[mark_counter]
        text_counter = 0
        while text_counter < len(text):
            text = text.replace(double_mark, marks[mark_counter])
            text_counter += 1
        mark_counter += 1

    return text


"""
Пример использования
"""
text = cut_extra_characters("Какой милый котик!!! Где вы его купили??? Хочу такого же)))", "?!")
print(text)  # Какой милый котик! Где вы его купили? Хочу такого же)))
