# Задание 2. Генерация
# Что нужно сделать
# Пользователь вводит целое число N. Вам необходимо написать программу, которая генерирует список из чисел от 0 до N
# (не включая N). Например, если N — это 5, то нужно работать со списком 0, 1, 2, 3, 4.
#
# Также есть дополнительное условие. При заполнении списка нужно выполнить одно из двух действий с каждым числом:
#
# если индекс числа чётный (или 0), то вместо числа необходимо взять 1;
# если индекс числа нечётный, то вместо числа необходимо взять остаток от деления этого числа на 5 (число % 5).
# Таким образом нужен следующий алгоритм:
#
# цикл по числам
#
#     если текущий индекс чётный
#
#         то в список добавляется 1
#
#     если текущий индекс нечётный
#
#         то в список добавляется (число % 5)
#
# Алгоритм нужно реализовать при помощи генератора списка (в одну строку).
#
# Пример:
#
# Введите длину списка: 10
#
# Результат: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует указанному в задаче.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

print("Результат:", [1 if (i % 2 == 0) else (i % 5) for i in range(int(input("Введите длину списка: ")))])

#ЗачОт, но если когда-то будешь писать что-то серьезное - инпут лучше вывести в отдельную строку, кровь из глаз