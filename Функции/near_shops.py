"""
Функция near_shops находит все магазины в радиусе R от заданной точки.
Функция принимает три аргумента:
1.Координаты точки, вокруг которой будем искать. В виде кортежа из двух элементов (X, Y).
2.Радиус поиска - R.
3.Список магазинов из кортежей вида ("название магазина", (Координата_X, Координата_Y))

Функция возвращает список из кортежей вида ("название магазина", Расстояние_до_магазина).
Кортежи в списке отсортированы по расстоянию до магазина (от близких к дальним).
В список попадают только те магазины, которые расположены в пределах R.
"""
import math


def near_shops(coordinates, radius, shops):
    counter = 0
    closest_shops = list()
    while counter < len(shops):
        shop_distance = math.sqrt((coordinates[0] - shops[counter][1][0])**2 + (coordinates[1] - shops[counter][1][1])**2)
        if shop_distance <= radius:
            closest_shops.append((shops[counter][0], shop_distance))
        counter += 1

    closest_shops = sorted(closest_shops, key=lambda shop: shop[1])

    return closest_shops


"""
Пример использования
"""
shops = [
    ("Магазин 1", (1, 1)),
    ("Магазин 2", (-1, 0)),
    ("Магазин 3", (2, -1)),
    ("Магазин 4", (2, 4)),
    ("Магазин 5", (2, 0)),
]
my_shops = near_shops((2, 3), 3, shops)
print(my_shops)  # [('Магазин 4', 1.0), ('Магазин 1', 2.23606797749979), ('Магазин 5', 3.0)]
