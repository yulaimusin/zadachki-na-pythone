"""
Функция ticket_type получает номер билета в виде строки из шести цифр и возвращает его тип:
счастливый, встречный, пьяный или обычный.
Счастливым называют такой билет, что сумма первых трех цифр его номера равна сумме последний трех цифр.
Встречным называют тот билет, что сумма первых трех цифр его номера отличается на единицу от суммы последних трех цифр.
Пьяным называется билет, в котором сумма первых трех цифр его номера отличается на двойку от суммы последних трех цифр.
Обычными называют все остальные билеты.
"""


def ticket_type(input_number):
    if type(input_number) == int:
        input_number = str(input_number)
    if type(input_number) == str and input_number.isdigit():
        counter = 0
        number = list()
        while counter < len(input_number):
            number.append(input_number[counter])
            number[counter] = int(number[counter])
            counter += 1
        if sum(number[:3]) == sum(number[3:]):
            return "счастливый"
        elif sum(number[:3])+1 == sum(number[3:]) or sum(number[:3])-1 == sum(number[3:]):
            return "встречный"
        elif sum(number[:3])+2 == sum(number[3:]) or sum(number[:3])-2 == sum(number[3:]):
            return "пьяный"
        else:
            return "обычный"

    elif type(input_number) not in [int]:
        raise TypeError


print(ticket_type("123321"))  # счастливый
print(ticket_type(123322))  # встречный
print(ticket_type(123323))  # пьяный
print(ticket_type(987654))  # обычный
