# Задача 1. Тайны археологии

# Что нужно сделать
# Археолог Ирина в последней экспедиции нашла древнюю глиняную табличку с числами 114 12 14 10605 4907 450.
# Ирина предположила, что это шифр, который можно расшифровать с помощью компьютерной программы.
# Помогите Ирине — напишите программу, которая будет выводить на экран числа, соответствующие следующему условию:
# они чётные и не делятся на три. Для подходящих чисел программа выводит сообщение «Число подходит».
# Для неподходящих под условие — «Число не подходит».

# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# на экран выведено число и текст «Число подходит» / «Число не подходит»;
# переменные имеют значащие имена, не только a, b, c, d (смотрите видео из занятия 2.3);
# задача решена с помощью конструкции for.

n = int(input('Введите количество исследуемых чисел: '))
for _ in range(n):
    num = int(input('Введите исследуемое число: '))
    if num % 2 == 0 and num % 3 != 0:
        print('Число подходит')
    else:
        print('Число не подходит')