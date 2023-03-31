# Задача 8. Сумма ряда

# Что нужно сделать
# Пользователь вводит действительное число х и точность precision. Напишите программу, которая по числу х вычисляет сумму ряда в точности до precision.
# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# def start
def step(x, count):
    delim, delit = 1, 1
    for i in range(1, count + 1):
        delim *= x
        delit *= i

    return (delim / delit)


# def stop

digit, prec = input("Введите число:"), input("Введите точность:")
result, check = 1, 0
if digit.isnumeric():
    digit, check = int(digit), check + 1
else:
    print("Введено не целое число!")

if prec.isnumeric():
    prec, check = int(prec), check + 1
else:
    print("Введено не целое число!")
if check == 2:
    for a in range(1, prec + 1):
        if a / 2 == a // 2:
            result -= step(digit, a * 2)
        else:
            result += step(digit, a * 2)

    print("Сумма ряда: ", result)