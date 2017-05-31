"""
В файле matrix_transposition_source.txt содержится матрица M x N.
Программа transpose.py транспонирует матрицу и сохраняет результат в файл matrix_transposition_result.txt.
"""


source_matrix = open("matrix_transposition_source.txt", "r", encoding="UTF-8").read()
rows_of_matrix = source_matrix.split("\n")
new_rows_of_matrix = list()
counter = 0
while counter < len(rows_of_matrix):
    elements_of_row = list()
    elements_of_row = rows_of_matrix[counter].split(" ")
    new_rows_of_matrix.append(elements_of_row)
    counter += 1

supercounter = 0
NEW = list()
while supercounter < len(new_rows_of_matrix[0]):
    counter = 0
    #print("super bla")
    NEW.append(list())
    while counter < len(new_rows_of_matrix):
        #print("blabla", new_rows_of_matrix[counter][supercounter])
        NEW[supercounter].append(new_rows_of_matrix[counter][supercounter])
        counter += 1
    supercounter += 1

to_file = open("matrix_transposition_result.txt", "w+", encoding="UTF-8")
for row in NEW:
    to_file.write(" ".join(row) + "\n")
print(NEW)
