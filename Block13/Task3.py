# Задача 3. Число наоборот 2

# Что нужно сделать
# Пользователь вводит два числа — N и K. Напишите программу, которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке, затем складывает их, снова переворачивает и выводит ответ на экран.

# Пример:
# Введите первое число: 102
# Введите второе число: 123
# Первое число наоборот: 201
# Второе число наоборот: 321
# Сумма: 522
# Сумма наоборот: 225

# Что оценивается
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# формат вывода соответствует примеру;
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);

# def start
def reverse(num):
    count = len(str(num)) - 1
    result = 0
    while num > 0:
        result += (num % 10) * (10 ** count)
        count -= 1
        num //= 10
    return result

# def end

N, K = int(input("Введите первое число: ")), \
       int(input("Введите второе число: "))
print("Первое число наоборот:", reverse(N), "\nВторое число наоборот:", reverse(K), "\nСумма:", (N + K), "\nСумма наоборот:", reverse(N + K))