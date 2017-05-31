"""
В файле square_matrix_and_trace.txt содержится квадратная матрица N x N.
Программа вычисляет след матрицы (https://ru.wikipedia.org/wiki/След_матрицы) и выводит его на экран.
"""


file = matrix = open("square_matrix_and_trace.txt", "r", encoding="UTF-8").read()
matrix = matrix.split("\n")
counter = 0
the_sled = 0

for row_of_matrix in matrix:
    row_of_matrix = row_of_matrix.split("\t")
    the_sled += int(row_of_matrix[counter])
    counter += 1

print(the_sled)
