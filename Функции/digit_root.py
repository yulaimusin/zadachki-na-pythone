"""
Функция digit_root принимает целое число и находит его цифровой корень.
Цифровой корень числа – это сумма всех цифр, которые составляют это число.
Если полученная сумма содержит более одной цифры, то необходимо сложить цифры суммы и повторять операцию до тех пор,
пока не останется одна цифра. Она и называется цифровым корнем числа.
Например, цифровой корень числа 9999999 можно найти так:
9999999 -> 9 + 9 + 9 + 9 + 9 + 9 + 9 = 63
63 -> 6 + 3 = 9
Цифровой корень 9999999 равен 9.
"""


def digit_root(number):
    sum_ = 0
    counter = "go"
    while len(str(sum_)) != 1 or counter != "stop":
        sum_ = 0
        for one_number in str(number):
            sum_ += int(one_number)
        if len(str(sum_)) == 1:
            return sum_
        else:
            number = sum_

        counter = "stop"

    return sum_


"""
Пример использования
"""
print(digit_root(9999999))  # 9
