"""
В файле sum_of_negative_numbers.txt в одну строку через пробелы записаны целые числа.
Программа считает и печатает сумму всех отрицательных чисел из этого файла.
"""

file = numbers = open("sum_of_negative_numbers.txt", "r", encoding="UTF-8").read()
numbers = numbers.split(" ")
sum = 0
for number in numbers:
    number = int(number)
    if number < 0 and sum < 0:
        sum = sum + number
    elif number < 0 and sum == 0:
        sum = number

print(sum)
