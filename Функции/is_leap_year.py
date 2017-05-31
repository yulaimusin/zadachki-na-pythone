"""
Функция is_leap_year принимает год и возвращает True если год високосный и False в противном случае.
Год является високосным, если его номер кратен 4. Но из кратных 100 високосными являются лишь кратные 400.
То есть 2000 - високосный, а 1800 - нет.
"""


def is_leap_year(year):
    if not year % 4:
        if not year % 100:
            if not year % 400:
                return True
            else:
                return False
        return True
    return False


"""
Пример использования
"""
print(is_leap_year(1800))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(2012))  # True
print(is_leap_year(2013))  # False
print(is_leap_year(2014))  # False
print(is_leap_year(2015))  # False
print(is_leap_year(2016))  # True
print(is_leap_year(2017))  # False
print(is_leap_year(2018))  # False
