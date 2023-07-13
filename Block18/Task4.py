# Задание 4. Гистограмма частоты — 2
# Что нужно сделать
# Вы уже писали программу для лингвистов, которая получала на вход текст и считала, сколько раз каждый символ
# встречается в строке. Теперь задание изменилось: максимальную частоту выводить не нужно, но необходимо написать
# функцию, которая будет инвертировать полученный словарь. То есть в качестве ключа будет частота,
# а в качестве значения — список символов с этой частотой.
#
# По итогу нужно реализовать следующие подзадачи:
#
# получить текст и создать из него оригинальный словарь частот;
# создать новый словарь и заполнить его данными из оригинального словаря частот,
# используя количество повторов в качестве ключей, а буквы — в качестве значений, добавляя их в список для хранения.
# Пример
#
# Введите текст: здесь что-то написано
#
# Оригинальный словарь частот:
#
# : 2
#
# - : 1
#
# З : 1
#
# а : 2
#
# д : 1
#
# е : 1
#
# и : 1
#
# н : 2
#
# о : 3
#
# п : 1
#
# с : 2
#
# т : 2
#
# ч : 1
#
# ь : 1
#
# Инвертированный словарь частот:
#
# 1 : ['З', 'д', 'е', 'ь', 'ч', '-', 'п', 'и']
#
# 2 : ['с', ' ', 'т', 'н', 'а']
#
# 3 : ['о']
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

line = input("Введите текст: ")
data, rev_data = {}, {}
maxfr = 0
for s in line:
    if s in data:
        data[s] += 1
        if maxfr < data[s]:
            maxfr = data[s]
    else:
        data[s] = 1
print(data)
print("\nИнвертированный словарь частот:")
for i in range(1, maxfr + 1):
    if i in data.values():
        rev_data[i] = []
        for s in data:
            if data[s] == i:
                rev_data[i].append(s)
        print(i, ":", rev_data[i])
#зачОт