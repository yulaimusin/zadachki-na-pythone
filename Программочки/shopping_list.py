# -*- coding: utf-8 -*-

"""
Вы отправились в магазин и попросили друзей составить список покупок и прислать его вам. Каждый из друзей написал свой
список и в итоге вам прислали три файла: shopping_list_1.txt, shopping_list_2.txt и shopping_list_3.txt.
Когда вы открыли списки покупок, то сразу заметили, что некоторые товары повторяются, поэтому вы решили составить свой
собственный нормализованный список, где продукты не повторяются и записаны по алфавиту.

Программа shopping_list.py читает строки из трех файлов: shopping_list_1.txt, shopping_list_2.txt и
shopping_list_3.txt, а затем создает новый файл shopping_list.txt, в который помещает все прочитанные строки
без повторов и в алфавитном порядке.
"""


f1 = open("shopping_list_1.txt", "r", encoding='UTF8').read()
f2 = open("shopping_list_2.txt", "r", encoding='UTF8').read()
f3 = open("shopping_list_3.txt", "r", encoding='UTF8').read()
f1 = f1.strip().split("\n")
f2 = f2.strip().split("\n")
f3 = f3.strip().split("\n")
finish4 = list(set(f1 + f2 + f3))
finish4.sort()
finish4 = "\n".join(finish4)
f4 = open("shopping_list.txt", "w+", encoding='UTF8')
f4.write(finish4 + "\n")
