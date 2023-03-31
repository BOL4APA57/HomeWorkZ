# Задача 4. Календари
# Что нужно сделать
# Ваня увлекается историей, в особенности календарями. Он изучает календари разных времён, эпох и народностей.
# Для исследования ему нужно посчитать, у кого сколько было месяцев с чётным количеством дней.
# Напишите программу, которая считает количество только чётных чисел в последовательности
# (последовательность заканчивается при вводе нуля) и выводит ответ на экран.

# Что оценивается
# input содержит корректное приглашение для ввода;
# результат вычислений корректен, ввод осуществляется внутри цикла;
# при вводе 0 происходит выход из цикла;
# переменные имеют значащие имена, не только a, b, c, d (видео 2.3);
# правильное употребление пробелов после запятых и при бинарных операциях.

month = 1
count = 0

while month != 0:
    if month % 2 == 0:
        count += 1
    month = int(input('Введите количество дней в месяце: '))

print('Месяцев с четным количеством дней: ', count)