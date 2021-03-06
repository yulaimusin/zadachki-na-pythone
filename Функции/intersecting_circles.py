"""
Функция intersecting_circles() принимает два списка.
Каждый из списков содержит по 3 числа – координаты центра окружности (x, y) и её радиус (r).
Функция возвращает True если окружности пересекаются и False в противном случае.
Окружности считаются пересекающимися, если у них есть хотя бы одна общая точка.
Картинка: intersecting_circles.jpg
"""


def intersecting_circles(ring1, ring2):
    x1, y1, R1 = ring1
    x2, y2, R2 = ring2
    d = (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)
    if d < (R1+R2)*(R1+R2) and d > (R1-R2)*(R1-R2):
        return True  # "Пересекаются"
    else:
        return False  # "НЕ пересекаются"


"""
Пример использования
"""
print(intersecting_circles([-2, 2, 3], [3, 0, 4]))  # True
