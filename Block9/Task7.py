# Задача 7. Наибольшая сумма цифр
# Что нужно сделать

# Пользователь вводит N чисел. Среди натуральных чисел, которые были введены, найдите наибольшее по сумме цифр.
# Выведите на экран это число и сумму его цифр.

# Что оценивается
# Задание считается успешно выполненным, если:

# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

num, maxsum, result = int(input('Введите длину последовательности: ')), 0, 0

# Запрос чисел.
for i in range(num):
    check = 0
    var = int(input('Введите число: '))

# Суммирование цифр в числе.
    for s in str(var):
        check += int(s)

# Поиск числа с максимальной суммой цифр:
    if check >= maxsum:
        maxsum = check
        result = var

print('Число с максимальной суммой цифр в нем:', result, '. И эта сумма равна:', maxsum)