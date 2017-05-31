"""
Функция intersecting_rectangles() принимает два списка.
Каждый из списков содержит по 4 числа – координаты левого верхнего (x1, y1)
и правого нижнего (x2, y2) углов прямоугольника.
Функция возвращает True если прямоугольники пересекаются и False в противном случае.
Прямоугольники считаются пересекающимися, если у них есть хотя бы одна общая точка.
Стороны прямоугольников параллельны осям координат.
Картинка: intersecting_rectangles.jpg
"""


def intersecting_rectangles(rectangle1, rectangle2):
    rectangle1_lefttop_X = rectangle1[0]
    rectangle1_lefttop_Y = rectangle1[1]
    rectangle1_rightbottom_X = rectangle1[2]
    rectangle1_rightbottom_Y = rectangle1[3]

    rectangle2_lefttop_X = rectangle2[0]
    rectangle2_lefttop_Y = rectangle2[1]
    rectangle2_rightbottom_X = rectangle2[2]
    rectangle2_rightbottom_Y = rectangle2[3]

    if rectangle1_lefttop_Y < rectangle2_rightbottom_Y\
            or rectangle1_rightbottom_Y > rectangle2_lefttop_Y\
            or rectangle1_rightbottom_X < rectangle2_lefttop_X\
            or rectangle1_lefttop_X > rectangle2_rightbottom_X:
        return False  # "Прямоугольники НЕ пересекаются"
    else:
        return True  # "Прямоугольники пересекаются"


"""
Пример вызова функции:
"""
result = intersecting_rectangles([-5, 2, 3,-2], [4, 8, 5, 1])
print(result)  # False
result = intersecting_rectangles([-5, 2, 3,-2], [2, 6, 5, 1])
print(result)  # True
