# Задача 5. Песни
# Что нужно сделать
#
# Мы пишем приложение для удобного прослушивания музыки. У Вани есть список из девяти песен группы Depeche Mode.
# Каждая песня состоит из названия и продолжительности с точностью до долей минут:
#
# violator_songs = [
#     ['World in My Eyes', 4,86],
#     ['Sweetest Perfection', 4,43],
#     ['Personal Jesus', 4,56],
#     ['Halo', 4,9],
#     ['Waiting for the Night', 6,07],
#     ['Enjoy the Silence', 4,20],
#     ['Policy of Truth', 4,76],
#     ['Blue Dress', 4,29],
#     ['Clean', 5,83]
# ]
#
#
# Из этого списка Ваня хочет выбрать N песен и закинуть их в особый плейлист с другими треками.
# И при этом ему важно, сколько времени в сумме эти N песен будут звучать.
#
# Напишите программу, которая запрашивает у пользователя количество песен из списка и затем названия этих песен,
# а на экран выводит общее время их звучания.
#
#
#
# Пример:
#
# Сколько песен выбрать? 3
#
# Название 1-й песни: Halo
#
# Название 2-й песни: Enjoy the Silence
#
# Название 3-й песни: Clean
#
# Общее время звучания песен: 14,93 минуты
#
#
#
# Что оценивается
#
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3)

# def start
def song(name):
    time = 0
    for point in violator_songs:
        if name == point[0]:
            time += point[1]
    return time

# def end
violator_songs = [
     ['World in My Eyes', 4.86],
     ['Sweetest Perfection', 4.43],
     ['Personal Jesus', 4.56],
     ['Halo', 4.9],
     ['Waiting for the Night', 6.07],
     ['Enjoy the Silence', 4.20],
     ['Policy of Truth', 4.76],
     ['Blue Dress', 4.29],
     ['Clean', 5.83]
]
num = int(input("Сколько песен выбрать? "))
summary, count = 0, 1
while count <= num:
    title = input(f"Название {count}-й песни: ")
    if song(title) == 0:
        print("Ошибка! Такой песни нет в базе. Повторите ввод.")
    else:
        summary += song(title)
        count += 1
print(f"Общее время звучания песен: {summary} минуты")
#ЗачОт