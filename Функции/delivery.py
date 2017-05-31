"""
Функция delivery рассчитывает стоимость доставки техники по Москве и области.
Функция принимает один обязательный аргумент с ценой и 4 необязательных аргумента логического типа:
- region – принимает False если доставка по Москве и True если по области.
- big – принимает True если товар крупногабаритный и False для мелкогабаритной техники.
- time – принимает True если доставка назначена на определенное время.
- today – отвечает за доставку «День в день».
Все дополнительные аргументы по умолчанию установлены на False.

Функция delivery основана на ценах и условиях доставки с МВидео.
"""


def delivery(purchase_amount, region=False, big=False, time=False, today=False):
    if purchase_amount < 5000:
        delivery_price = 290
    else:
        delivery_price = 0

    if big is True:
        delivery_price = 490

    if today is True:
        delivery_price = 990
    if time is True:
        delivery_price += 190

    if region is True and big is False:
        delivery_price = 290
    elif region is True and big is True:
        delivery_price = 490

    return delivery_price


"""
Пример использования
"""
print(delivery(5000))
