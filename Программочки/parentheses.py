"""
Программа parentheses.py запрашивает строку, содержащую скобки, и проверяет правильно ли они расставлены.
Рассматриваются только круглые скобки.
Программа выводит:
True – если скобки расставлены правильно;
False – если порядок скобок нарушен.
"""

the_string = input('Введите строку, содержащую круглые скобки [например: "(2+3)()()"]: ')
parentheses_was_opened = False
for symbol in the_string:
    if symbol == "(":
        if parentheses_was_opened:
            it_is_right = False
            break
        parentheses_was_opened = True
        it_is_right = False
    elif symbol == ")":
        if parentheses_was_opened is False:
            it_is_right = False
            break
        elif parentheses_was_opened:
            parentheses_was_opened = False
            it_is_right = True

print(it_is_right)
