# Задание 7. Три списка
# Что нужно сделать
# Даны три списка.
#
# array_1 = [1, 5, 10, 20, 40, 80, 100]
#
# array_2 = [6, 7, 20, 80, 100]
#
# array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
#
# Нужно выполнить две задачи:
# найти элементы, которые есть в каждом списке;
# найти элементы из первого списка, которых нет во втором и третьем списках.
# Каждую задачу нужно выполнить двумя способами:
#
# без использования множеств;
# с использованием множеств.
# Пример выполнения на других данных:
#
# array_1 = [1, 2, 3, 4]
#
# array_2 = [2, 4]
#
# array_3 = [2, 3]
#
# Вывод:
#
# Задача 1:
#
# Решение без множеств: 2
#
# Решение с множествами: 2
#
# Задача 2:
#
# Решение без множеств: 1
#
# Решение с множествами: 1
#
# Что оценивается
# Результат вычислений корректен.
# Обе задачи решены двумя предложенными способами.
# Один из способов — обязательно с использованием множеств и операций над множествами.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельной функции.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
answer_pos, answer_neg = [], []
for i in array_1:
    if i in array_2 and i in array_3:
        answer_pos.append(i)
    if i not in array_2 and i not in array_3:
        answer_neg.append(i)
print("Решение без множеств.\nЗадача 1:", *answer_pos,"\nЗадача 2:", *answer_neg)

mnog = {i for i in array_1}
set_pos = set.intersection(mnog, array_2, array_3)
set_neg = set.difference(mnog, array_2, array_3)
print("\nРешение c множеством.\nЗадача 1:", *set_pos,"\nЗадача 2:", *set_neg)
#зачОт