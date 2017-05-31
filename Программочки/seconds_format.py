"""
Программа seconds_format.py запрашивает и получает от пользователя количество секунд, которое прошло с начала дня.
Программа выводит отформатированное время в формате HH:MM:SS.
1.SS – число секунд от 0 до 59.
2.MM – число минут от 0 до 59.
3.HH – число часов от 0 до 23.
Все значения времени выводятся в двузначном формате. Если число занимает один знак, то перед ним ставится 0.
Если прошло меньше одного часа, то часы не выводятся. Если прошло меньше одной минуты, то минуты не выводятся.

Примеры:
Количество секунд, которое прошло с начала дня: 17
17

Количество секунд, которое прошло с начала дня: 89
01:19

Количество секунд, которое прошло с начала дня: 4589
01:16:29

Количество секунд, которое прошло с начала дня: 46799
12:59:59
"""


seconds = int(input('Введите количество секунд, которое прошло с начала дня: '))
minutes = 0
hours = 0

while seconds >= 60:
    minutes += 1
    seconds -= 60
    while minutes >= 60:
        hours += 1
        minutes -= 60

if minutes == 0 and hours == 0:
    minutes = ""
elif minutes == 0 and hours > 0:
    minutes = "00:"
elif 10 > minutes > 0:
    minutes = "0" + str(minutes) + ":"
else:
    minutes = str(minutes) + ":"

if hours == 0:
    hours = ""
elif 10 > hours > 0:
    hours = "0" + str(hours) + ":"
else:
    hours = str(hours) + ":"

if seconds == 0:
    seconds = "00"
elif 10 > seconds > 0:
    seconds = "0" + str(seconds)
else:
    seconds = str(seconds)

print(hours + minutes + seconds)
