"""
Класс Point моделирует поведение точки в прямоугольной системе координат на плоскости.
Конструктор класса принимает два аргумента, которые отвечают за координаты точки.
Изменение координат точки происходит с помощью свойств (property). Каждая координата - это отдельное свойство точки.
С помощью метода set можно изменить обе координаты.
Значения координат хранятся как float, однако класс принимает координаты представленные как числами (int, float),
так и строками (str), которые преобразуются к float.
"""


class Point:
    def __init__(self, x_, y_):
        self.set(x_, y_)

    @property
    def x(self):
        return self.fact_getter(self.x_)
    @property
    def y(self):
        return self.fact_getter(self.y_)
    @x.setter
    def x(self, x_):
        self.x_ = float(x_)
    @y.setter
    def y(self, y_):
        self.y_ = float(y_)

    def fact_getter(self, number):
        if (number).is_integer():
            return int(number)
        else:
            return float(number)

    def set(self, x_, y_):
        self.x = x_
        self.y = y_


"""
Пример использования
"""
point = Point(12.34, "15.46")
print(type(point.x))  # <type 'float'>
print(type(point.y))  # <type 'float'>
point.x = "4"
point.y = 5.4
print(point.x)  # 4
print(point.y)  # 5.4
point.set(7, "99.8")
print(point.x)  # 7
print(point.y)  # 99.8
