"""
Класс Rectangle моделирует прямоугольник в прямоугольной системе координат на плоскости.
Конструктор класса принимает четыре аргумента: x1, y1, x2, y2:
- x1 и y1 отвечают за левую верхнюю точку прямоугольника;
- x2 и y2 за правую нижнюю точку.
Класс содержит следующие методы:
- get_length()
- get_width()
- get_area()
- get_perimeter()
- is_square()
Для простоты считается, что все стороны прямоугольника параллельны осям координат.
"""


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.set(x1, y1, x2, y2)

    def set(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    """ Возвращает длину прямоугольника """
    def get_length(self):
        return self.x2 - self.x1

    """ Возвращает ширину прямоугольника """
    def get_width(self):
        return self.y1 - self.y2

    """ Возвращает площадь прямоугольника """
    def get_area(self):
        return self.get_width() * self.get_length()

    """ Возвращает периметр прямоугольника """
    def get_perimeter(self):
        return self.get_width()*2 + self.get_length()*2

    """ Возвращает True если прямоугольник является квадратом и False в противном случае """
    def is_square(self):
        if self.get_length() == self.get_width():
            return True
        else:
            return False


"""
Пример использования:
"""
rectangle = Rectangle(-3, 2, 4, -2)
print(rectangle.get_length())  # 7
print(rectangle.get_width())  # 4
print(rectangle.get_area())  # 28
print(rectangle.get_perimeter())  # 22
print(rectangle.is_square())  # False
