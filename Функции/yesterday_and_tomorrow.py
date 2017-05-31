"""
Функция yesterday_and_tomorrow принимает аргумент-строку date (текущий день) и возвращает кортеж из двух элементов:
предыдущий день и следующий день, относительно переданного.

Аргумент date передается в виде строки формата ДД.ММ.ГГГГ.
Возвращаемый кортеж также содержит даты в виде строк в формате ДД.ММ.ГГГГ
Функция не учитывает того, является ли год високосным или нет.
"""


def yesterday_and_tomorrow(date):
    date = date.split(".")
    today, month, year = date[:]

    yesterday = str(int(date[0])-1)
    yesterday_date = yesterday + "." + month + "." + year

    tomorrow = str(int(date[0])+1)
    tomorrow_date = tomorrow + "." + month + "." + year
    tomorrow_and_yesterday = (yesterday_date, tomorrow_date)
    return tomorrow_and_yesterday


"""
Пример использования
"""
result = yesterday_and_tomorrow('12.03.2016')
print(result)  # ('11.03.2016', '13.03.2016')
