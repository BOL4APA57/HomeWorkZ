# Задача 10. Пропавшая карточка
# Что нужно сделать
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась.
# Напишите программу, которая поможет найти потерянную карточку, если номера оставшихся известны.
# Найдите её, зная номера оставшихся карточек.

# Введите число карточек — N.
# Затем последовательно введите N – 1 номера оставшихся карточек.

# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержат корректные приглашения для ввода;
# переменные имеют значащие имена, не только a, b, c, d.

# Решение без списка.

n = int(input('Введите исходное количество карточек: '))
count = 0
for i in range(1, n + 1):
    count += i
for _ in range(n - 1):
    test = int(input('Введите номер проверяемой карточки: '))
    count -= test
print()
print('Номер потерянной карточки:', count)