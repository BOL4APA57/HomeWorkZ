# Задание 5. Словарь синонимов
# Что нужно сделать
# Одна библиотека поручила вам написать программу для оцифровки словарей синонимов.
# На вход в программу подаётся N пар слов. Каждое слово является синонимом для своего парного слова.
#
# Реализуйте код, который составляет словарь синонимов (все слова в словаре различны),
# затем запрашивает у пользователя слово и выводит на экран его синоним. Обеспечьте контроль ввода:
# если такого слова нет, выведите ошибку и запросите слово ещё раз.
# При этом проверка не должна зависеть от регистра символов.
#
# Пример
#
# Введите количество пар слов: 3
#
# Первая пара: Привет — Здравствуйте
#
# Вторая пара: Печально — Грустно
#
# Третья пара: Весело — Радостно
#
# Введите слово: интересно
#
# Такого слова в словаре нет.
#
# Введите слово: здравствуйте
#
# Синоним: Привет
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

count = int(input("Введите количество пар слов: "))
sin = {}
for i in range(count):
    pair = input("Введите пару: ")
    sin[i] = []
    sin[i].append(pair[:pair.index(" ")])
    sin[i].append(pair[pair.index(" ") + 3:])
word = input("Введите слово: ")
check = False
while not check:
    for i in range(count):
        if sin[i][0].upper() == word.upper():
            print("Синоним:", sin[i][1])
            check = True
        elif sin[i][1].upper() == word.upper():
            print("Синоним:", sin[i][0])
            check = True
    if not check:
        print("Такого слова в словаре нет.")