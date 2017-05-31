"""
Функция distance вычисляет расстояние между двумя точками на плоскости или в пространстве.
Функция принимает два аргумента.
Каждый аргумент - это кортеж из двух или трех элементов: X и Y для точки на плоскости
и X, Y, Z - для точки в пространстве.
"""
import math


def distance(first, second):
    if len(first) == len(second) and len(first) == 2:
        return math.sqrt((second[0]-first[0])**2 + (second[1]-first[1])**2)
    elif len(first) == len(second) and len(first) == 3:
        return math.sqrt((second[0]-first[0])**2 + (second[1]-first[1])**2 + (second[2]-first[2])**2)
    else:
        return "error"


"""
Пример использования
"""
print(distance((-1, 3), (6, 2)))  # 7.0710678118654755
print(distance((-1, 3, 3), (6, 2, -2)))  # 8.660254037844387
