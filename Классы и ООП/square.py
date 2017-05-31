"""
Класс Square моделирует квадрат в прямоугольной системе координат на плоскости.
Так как квадрат — это частный случай прямоугольника, то Square наследуется от Rectangle.
Конструктор Square принимает 3 аргумента: x, y, l:
- top_right_x, top_right_y — координаты правого верхнего угла квадрата;
- length — длина стороны квадрата.
"""
from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, top_right_x, top_right_y, length):
        x1 = top_right_x - length
        y1 = top_right_y
        x2 = top_right_x
        y2 = top_right_y - length
        super().__init__(x1, y1, x2, y2)


"""
Пример использования:
"""
square = Square(1, 4, 2)
print(square.get_length())  # 2
print(square.get_width())  # 2
print(square.get_area())  # 4
print(square.get_perimeter())  # 8
print(square.is_square())  # True
