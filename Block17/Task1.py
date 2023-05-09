# Задание 1. Меню ресторана
# Что нужно сделать
# Ресторан заказал вам приложение, которое в один клик отображает пользователю меню.
# Для работы ресторан предоставил вам свой сайт, где можно найти меню в виде идущих подряд названий блюд.
#
# Напишите программу, которая выводит меню на экран. На вход подаётся строка из названий блюд, разделённых символом «;»,
# а на выходе названия перечисляются через запятую и пробел.
#
# Пример:
#
# Доступное меню: утиное филе;фланк-стейк;банановый пирог;плов.
#
# Сейчас в меню есть: утиное филе, фланк-стейк, банановый пирог, плов.
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

menu = input("Доступное меню: ").split(";")
menu = ", ".join(menu)
print("Сейчас в меню есть:", menu)

#зачОт