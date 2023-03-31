# Задача 8. НОД

# Что нужно сделать
# Напишите функцию, вычисляющую наибольший общий делитель двух чисел.

# Что оценивается
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

# def start
def NOD(max, min):
    while min != 0:
        max, min = min, max % min
    print("Наибольший общий делитель: ", max)

# def end
a, b = int(input("Введите первое число: ")), int(input('Введите второе число: '))
if b > a:
    a, b = b, a
NOD(a, b)