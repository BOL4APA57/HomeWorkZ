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
# Первая пара: Привет - Здравствуйте
#
# Вторая пара: Печально - Грустно
#
# Третья пара: Весело - Радостно
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

# count = int(input("Введите количество пар слов: "))
# sin = {}
# for i in range(count):
#     pair = input("Введите пару: ")
#     sin[i] = []
#     sin[i].append(pair[:pair.index(" ")])
#     sin[i].append(pair[pair.index(" ") + 3:])

# while not check:
# word = input("Введите слово: ")
# check = False
#     for i in range(count):
#         if sin[i][0].upper() == word.upper():
#             print("Синоним:", sin[i][1])
#             check = True
#             break
#         elif sin[i][1].upper() == word.upper():
#             print("Синоним:", sin[i][0])
#             check = True
#             break
#     if not check:
#         print("Такого слова в словаре нет.")

# TO DO программа сваливается в бесконечный цикл, очень усложнен ввод пары, обращение внутри словаря идет по индексам,
# что не есть хорошо. Смысл задачи в том, что первое слово, которое вводится, явлется ключем словаря,
# а второе - его значением

# upd. Больше не сваливается)))


count = int(input("Введите количество пар слов: "))
sin = {}
for i in range(count):
    string = input("Введите пару: ")
    pair = string.split(" - ")
    sin[pair[0].capitalize()], sin[pair[1].capitalize()] = pair[1].capitalize(), pair[0].capitalize()

# Чтобы не получить головняк с поиском по значениям, и потом - выводом ключа, увеличил количество ключей.

check = False
while not check:
    word = input("Введите слово: ").capitalize()
    check = False
    if word in sin:
        print("Синоним:", sin[word])
        check = True
    else:
        print("Такого слова в словаре нет.")

#TO DO не работает, если мы задаем слово, которе является значением словаря
# Введите количество пар слов: 2
# Введите пару: привет - пока
# Введите пару: хай - здорова
# Введите слово:
# Такого слова в словаре нет.
# Введите слово: здорова
# Такого слова в словаре нет.
# строка sin[pair[0]], sin[pair[1]] = pair[1], pair[0] может быть заменена на sin[pair[0]], sin[pair[1]] = pair
# зачОт