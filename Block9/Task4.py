# Задача 4. Крест
# Что нужно сделать
# Напишите программу, которая выводит на экран крест из символов ^
# (символы выводятся по диагоналям воображаемого квадрата).

# Что оценивается
# Задание считается успешно выполненным, если:

# input содержит корректное приглашение для ввода;
# Формат вывода соответствует примеру.

num = int(input('Введите высоту фигуры: '))

# Формирование верхней части.
for i in range(num // 2):
    print(' ' * i, '^', ' ' * (num - 2 - i*2), '^', sep='')

# Проверка четности и "рисование" оси.
if num % 2 != 0:
    print(' ' * (num // 2 -1), '^')

# Формирование нижней части.
for i in range(num // 2 - 1, -1, -1):
    print(' ' * i, '^', ' ' * (num - 2 - i*2), '^', sep='')