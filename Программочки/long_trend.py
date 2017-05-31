"""
Программа long_trend.py запрашивает и должна получить набор целых чисел, разделенных пробелами.
После вычисляется самый продолжительных тренд из этих чисел и выводится на экран.

Учитывается, что одно и то же число может попадать сразу в два тренда.
Например, из последовательности 1 2 3 4 3 2 можно выделить два тренда 1 2 3 4 и 4 3 2 — 4 попадает сразу в оба тренда.
"""


the_str = input('Введите набор целых чисел, разделенных пробелами (например, "1 2 3 4 3 2"): ')
numbers = the_str.split(" ")
#for number in numbers[-1::-1]:    # перебор в обратную сторону
    #print(number)
# <Изменяем типы всех значений. STRING TWO INT
counter = 0
while counter < len(numbers):
    numbers[counter] = int(numbers[counter])
    counter += 1
# </Изменяем типы всех значений. STRING TO INT
counter = 1
new_numbers = list()
new_numbers_reverse = list()
while counter < len(numbers):
    if numbers[counter]-1 == numbers[counter-1]:
        new_numbers.append(numbers[counter-1])
        new_numbers.append(numbers[counter])
    if numbers[counter]+1 == numbers[counter-1]:
        new_numbers_reverse.append(numbers[counter-1])
        new_numbers_reverse.append(numbers[counter])
    counter += 1

new_numbers = list(set(new_numbers))
new_numbers_reverse = list(set(new_numbers_reverse))
finish_numbers = list()
if len(new_numbers) > len(new_numbers_reverse):
    finish_numbers = new_numbers
    finish_numbers.sort()
elif len(new_numbers) < len(new_numbers_reverse):
    finish_numbers = new_numbers_reverse
    finish_numbers.sort()
    finish_numbers.reverse()

# <Изменяем типы всех значений. INT TO STRING
counter = 0
while counter < len(finish_numbers):
    finish_numbers[counter] = str(finish_numbers[counter])
    counter += 1
# </Изменяем типы всех значений. INT TO STRING
finish_numbers = " ".join(finish_numbers)
print(finish_numbers)
