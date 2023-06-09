# Задача 7. Контейнеры
# Что нужно сделать

# Контейнеры на складе лежат в ряд в порядке невозрастания (меньше либо равно) массы в килограммах.
# На склад привезли ещё один контейнер, который тоже нужно положить на определённое место.
# Напишите программу, которая получает на вход невозрастающую последовательность натуральных чисел.
# Они означают массу каждого контейнера в ряду. После этого вводится число X — масса нового контейнера.
# Программа выводит номер, под которым будет лежать новый контейнер. Если в ряде есть контейнеры с массой,
# как у нового, то его нужно положить после них.
# Обеспечьте контроль ввода: все числа не превышают 200.

# Пример:
# Количество контейнеров: 8
# Введите вес контейнера: 165
# Введите вес контейнера: 163
# Введите вес контейнера: 160
# Введите вес контейнера: 160
# Введите вес контейнера: 157
# Введите вес контейнера: 157
# Введите вес контейнера: 155
# Введите вес контейнера: 154

# Введите вес нового контейнера: 162
# Номер, который получит новый контейнер: 3

# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

# def start
def check(data):
    while not data.isnumeric():
        data = input("Ошибка! Введенное число должно быть натуральным.\nПовторите ввод: ")
    return int(data)

def check_weight(cont):
    if cont <= 0 or cont > 200:
        cont = check(input("Некорректный ввод! Вес контейнера не может быть отрицательным, нулевым, и должен весить не более 200 кг.\nВведите вес контейнера: "))
        while cont <= 0 and cont > 200:
            cont = check(input("Некорректный ввод! Вес контейнера не может быть отрицательным, нулевым, и должен весить не более 200 кг.\nВведите вес контейнера: "))
    return cont
# def end

num = check(input("Введите количество контейнеров: "))
order, previous = [], 200
for i in range(num):
    weight = check_weight(check(input("Введите вес контейнера: ")))

    if weight > previous:
        while weight > previous:
            weight = check_weight(check(input("Контейнер должен весить меньше предыдущего! \nПовторите ввод: ")))
    order.append(weight)
    previous = weight


new_weight = check(input("Введите вес нового контейнера: "))
for i in range(num - 1):
    if order[i] >= new_weight > order[i + 1]:
        print("Номер, который получит новый контейнер: ", i + 2)
        break
