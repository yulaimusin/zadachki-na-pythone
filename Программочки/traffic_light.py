"""
Работа светофора для пешеходов запрограммирована следующим образом: с начала каждого часа, в течение N минут горит
зеленый сигнал, затем в течение M минут горит красный сигнал. Потом снова N минут горит зеленый и тд.

Программа traffic_light.py запрашивает у пользователя и получает три параметра: N, M и T, где T - это время в минутах,
прошедшее с начала очередного часа. После программа выводит green или red в зависимости от того,
сигнал какого цвета горит для пешехода в этот момент.

Примеры:
Время в минутах, в течении которого должен гореть зеленый сигнал: 4
Время в минутах, в течении которого должен гореть красный сигнал: 2
Время в минутах, прошедшее с начала очередного часа: 3
green

Время в минутах, в течении которого должен гореть зеленый сигнал: 4
Время в минутах, в течении которого должен гореть красный сигнал: 2
Время в минутах, прошедшее с начала очередного часа: 4
red
"""


N = int(input('Введите время в минутах, в течении которого должен гореть зеленый сигнал: '))
M = int(input('Введите время в минутах, в течении которого должен гореть красный сигнал: '))
T = int(input('Введите время в минутах, прошедшее с начала очередного часа: '))
time = 0
NM_time = 0
while time <= T:
    if NM_time / (N + M) == 1:
        NM_time = 0
    if NM_time >= 0 and NM_time < N:
        light = "green"
    if NM_time >= N and NM_time < N+M:
        light = "red"

    NM_time += 1
    time += 1

print(light)
