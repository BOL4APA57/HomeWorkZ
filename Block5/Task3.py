# Задача 3. Слишком большие числа
# Что нужно сделать
# У неудачливого бухгалтера всё опять идёт наперекосяк: ему приносят такие большие счета, что числа не помещаются на бумаге.
# Напишите программу, которая считала бы для него, сколько десятичных цифр (знаков) во вводимом числе.

# Что оценивается
# input содержит корректное приглашение для ввода;
# результат вывода корректен, правильно подсчитано количество цифр в числе;
# переменные имеют значащие имена, не только a, b, c, d (видео 2.3);
# правильное употребление пробелов после запятых и при бинарных операциях;
# используется цикл while;
# решение не использует работу со строками и операции над ними.

num = int(input('Введите число: '))
count = 0

# Проверка введенного нуля.
while num == 0:
    num = int(input('Введен ноль! Введите большее число. \nВведите число: '))

print('В числе', num, end=' ')

while num != 0:
    count += 1
    num = num // 10

print(count, 'цифр.')