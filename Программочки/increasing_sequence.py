"""
Программа increasing_sequence.py читает файл increasing_sequence.txt, а затем на экран выводит:
True – если в файле записана возрастающая последовательность целых чисел и каждый элемент последовательности в файле
записыван с новой строки;
False – если последовательность не возрастающая.

Если внутри возрастающей последовательности встречаются одинаковые элементы идущие друг за другом, то
последовательность, в целом, считается возрастающей.
"""


file = "increasing_sequence.txt"
sequence_of_number = open(file, "r", encoding="UTF-8").read()
sequence_of_number = sequence_of_number.split("\n")
length = len(sequence_of_number)
counter = 0
for item in sequence_of_number[1:]:
    if item >= sequence_of_number[counter]:
        the_increasing = True
    else:
        the_increasing = False
        break

    counter += 1

print(the_increasing)
