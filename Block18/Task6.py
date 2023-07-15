# Задание 6. Пицца
# Что нужно сделать
# В базе данных интернет-магазина PizzaTime хранятся сведения о том, кто, что и сколько заказывал у них в
# определённый период. Вам нужно структурировать эту информацию и определить, сколько всего пицц купил каждый заказчик.
#
# На вход в программу подаётся N заказов. Каждый заказ представляет собой строку вида
# «Покупатель — название пиццы — количество заказанных пицц». Реализуйте код, который выводит список покупателей
# и их заказов по алфавиту. Учитывайте, что один человек может заказать одну и ту же пиццу несколько раз.
#
# Пример
#
# Введите количество заказов: 6
#
# Первый заказ: Иванов Пепперони 1
#
# Второй заказ: Петров Де-Люкс 2
#
# Третий заказ: Иванов Мясная 3
#
# Четвёртый заказ: Иванов Мексиканская 2
#
# Пятый заказ: Иванов Пепперони 2
#
# Шестой заказ: Петров Интересная 5
#
# Иванов:
#
# Мексиканская: 2
#
# Мясная: 3
#
# Пепперони: 3
#
# Петров:
#
# Де-Люкс: 2
#
# Интересная: 5
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру (перед названием пиццы пять пробелов).
# Переменные и функции имеют значимые имена, не только a, b, c, d.

# table = {}
# count = int(input("Введите количество заказов: "))
# for i in range(count):
#     order = input("Введите заказ: ")
#     person = order[:order.index(" ")]
#     pizza = order[order.index(" ") + 1:order.rindex(" ")]
#     num = int(order[order.rindex(" "):])
#
#     if person in table and pizza in table[person]:
#        table[person][pizza] += num
#     elif person in table and pizza not in table[person]:
#         table[person][pizza] = num
#     else:
#         table[person] = {}
#         table[person][pizza] = num
#
# print("\nСписок заказов:")
# for men in sorted(table):
#     print("\n", men)
#     for food in table[men]:
#         print(f"{food}: {table[men][food]}")

# TO DO аналогично предыдущему заданию: очень усложнен ввод заказа, обращение внутри словаря идет по индексам,
# что не есть хорошо. Смысл задачи в том, что нужно создать два словаря с, где значение первого будет ключем для второго

table = {}
count = int(input("Введите количество заказов: "))
for i in range(count):
    order = input("Введите заказ: ")
    details = order.split()
    if details[0] in table and details[1] in table[details[0]]:
        table[details[0]][details[1]] += int(details[2])
    elif details[0] in table and details[1] not in table[details[0]]:
        table[details[0]][details[1]] = int(details[2])
    else:
        table[details[0]] = {}
        table[details[0]][details[1]] = int(details[2])

print("\nСписок заказов:")
for men in sorted(table):
    print("\n", men)
    for food in table[men]:
        print(f"{food}: {table[men][food]}")
