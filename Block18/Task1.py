# Задание 1. Песни — 2
# Что нужно сделать
# Продолжим писать приложение для удобного прослушивания музыки, но теперь песни хранятся в виде словаря,
# а не в виде вложенных списков. Каждая песня состоит из названия и продолжительности с точностью до долей минут.
#
# violator_songs = {
# 'World in My Eyes': 4.86,
# 'Sweetest Perfection': 4.43,
# 'Personal Jesus': 4.56,
# 'Halo': 4.9,
# 'Waiting for the Night': 6.07,
# 'Enjoy the Silence': 4.20,
# 'Policy of Truth': 4.76,
# 'Blue Dress': 4.29,
# 'Clean': 5.83
# }
# Напишите программу, которая запрашивает у пользователя количество песен из списка и их названия,
# а на экран выводит общее время их звучания.
#
# Пример
#
# Сколько песен выбрать? 3
#
# Название первой песни: Halo
#
# Название второй песни: Enjoy the Silence
#
# Название третьей песни: Clean
#
# Общее время звучания песен: 14,93 минуты
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

# violator_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83
# }
#
# count = int(input("Сколько песен выбрать? "))
# sound = 0
# for i in range(count):
#     track = input("Введите название песни: ")
#     while track not in violator_songs:
#         track = input("Такой песни нет в списке! \nПовторите ввод: ")
#     sound += violator_songs[track]
# print(f"Общее время звучания песен: {sound} минут(-ы)")
#ЗачОт

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

count = int(input("Сколько песен выбрать? "))
sound, replay = 0, 0
while replay < count:
    track = input("Введите название песни: ")
    if track not in violator_songs:
        print("Такой песни нет в списке! \nПовторите ввод! ")
    else:
        sound += violator_songs[track]
        replay += 1
print(f"Общее время звучания песен: {sound} минут(-ы)")
#ЗачОт
