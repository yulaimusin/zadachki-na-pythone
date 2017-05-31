"""
Программа palindrome.py запрашивает и получает у пользователя число или слово, а затем выводит:
True — если число является палиндромом, или
False — если таковым не является.
Палиндром (https://ru.wikipedia.org/wiki/Палиндром) — одинаково читающееся в обоих направлениях слово, число или фраза.
Например, 8228, ABBA.
"""


var = input('Введите число или слово (например, "82822828" или "ABCDFEkEFDCBA"): ')
length = len(var)
if length % 2 != 0:
    counter = int(length/2-0.5)
else:
    counter = int(length/2)

length = length-1
counter_begin = 0
counter_end = -1
while counter > 0:
    counter = counter-1
    if var[counter_begin] == var[counter_end]:
        result = True
    else:
        result = False
        break

    counter_end -= 1
    counter_begin += 1

print(result)
