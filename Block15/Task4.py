# Задача 4. Вечеринка
# Что нужно сделать
#
# В честь своего дня рождения Артём решил закатить вечеринку у себя на даче. Он не стал рассылать приглашения,
# а просто сообщил всем: «Если хотите — приходите и своих друзей тоже зовите». В ходе вечеринки люди приходили и уходили,
# ночевать остались не все. К тому же и сама дача не резиновая — на ней помещается всего шесть человек.
#
# Дан изначальный список гостей — имена тех, кто пришёл к началу:
#
# guests = [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]
# Напишите программу, которая спрашивает у пользователя, ушёл человек или пришёл новый гость, и,
# исходя из ответа, добавляет в список или удаляет из него нужное имя. При этом гостей может быть не больше шести.
# Имена запрашиваются до тех пор, пока пользователь не введёт сообщение «Пора спать».
#
# Пример:
#
# Сейчас на вечеринке 5 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]
# Гость пришёл или ушёл? пришёл
#
# Имя гостя: Алекс
#
# Привет, Алекс!
#
#
#
# Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
#
# Гость пришёл или ушёл? пришёл
#
# Имя гостя: Гоша
#
# Прости, Гоша, но мест нет.
#
#
#
# Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
#
# Гость пришёл или ушёл? ушёл
#
# Имя гостя: Ваня
#
# Пока, Ваня!
#
#
#
# Сейчас на вечеринке 5 человек: [‘Петя’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
#
# Гость пришёл или ушёл? Пора спать
#
#
#
# Вечеринка закончилась, все легли спать.
#
# Что оценивается
#
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]

print(f"\nСейчас на вечеринке {len(guests)} человек:", guests)
ask = input("\nГость пришёл или ушёл? \n1 - Пришел\n2 - Ушел\n0 - Пора спать\n")

while ask != "0":
    name = input("Имя гостя: ")
    if ask == "1" and len(guests) == 6:
        print(f"Прости, {name}, но мест нет.")
    elif ask == "1":
        print(f"Привет, {name}!")
        guests.append(name)
    elif ask == "2":
        if name in guests:
            print(f"Пока, {name}!")
            guests.remove(name)
        else:
            print("Такого человека у нас нет...")
    else:
        print("Ошибка ввода. Повторите.")
    print(f"\nСейчас на вечеринке {len(guests)} человек:", guests)
    ask = input("\nГость пришёл или ушёл? \n1 - Пришел\n2 - Ушел\n0 - Пора спать\n")

print("Вечеринка закончилась, все легли спать.")
#TO DO Программа работает не верно. она только один раз запрашивает пришел гость или ушел,
# а потом бесконечно запрашивает имя гостя
# Check | Done Работает. Забыл повторный ввод добавить...
#ЗачОт
