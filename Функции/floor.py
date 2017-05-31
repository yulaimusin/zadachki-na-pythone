"""
Функция floor возвращает этаж, на котором живет пользователь.
Функция принимает два позиционных аргумента:
1.Номер квартиры.
2.Количество квартир на этаже.
"""


def floor(number_of_flat, flats_on_a_floor):
    counter = 1
    counter_of_flats_on_a_floor = 1
    while counter <= number_of_flat:
        if counter > 1 and (counter-1) % flats_on_a_floor == 0:
            counter_of_flats_on_a_floor += 1

        counter += 1

    return counter_of_flats_on_a_floor


"""
Пример использования
"""
print(floor(8, 3))  # 3
print(floor(24, 4))  # 6
