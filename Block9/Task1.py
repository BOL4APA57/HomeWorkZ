# Задача 1. Тестовое задание
# Что нужно сделать
# Степан пришёл устраиваться на работу, где ему дали тестовое задание:
# проанализировать такую таблицу, понять, как она строится, и написать программу для вывода её на экран.
# Помогите Степану реализовать такую программу.

# Подсказка: номера столбцов. А ещё не забудьте про литерал \t для табуляции.

# Что оценивается
# Задание считается успешно выполненным, если:

# результат вывода соответствует условию;
# задача решена с помощь циклов for или while;
# формат вывода соответствует примеру.

side = int(input('Введите сторону квадрата: '))
for i in range(side):
    for j in range(i, (i + (side * 2 - 1)), 2):
        print(j, '\t', end='')
    print()