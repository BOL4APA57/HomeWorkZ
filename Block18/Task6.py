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
while True:
    count = int(input("Введите количество заказов: "))
    if count <= 0:
        print('Должен быть хотя бы один заказ!\n')
    else:
        break

for i in range(count):
    order = input("Введите заказ: ")
    details = order.split()
    person, pizza, num = details[0], details[1], details[2]

    if person in table and pizza in table[person]:
        table[person][pizza] += int(num)
    elif person in table and pizza not in table[person]:
        table[person][pizza] = int(num)
    else:
        table[person] = {}
        table[person][pizza] = int(num)

print("\nСписок заказов:")
for men in sorted(table):
    print("\n", men)
    for food in table[men]:
        print(f"{food}: {table[men][food]}")


#TO DO я знаю, ты такое не любишь, но:
# вот код мой, он опитимальнее с точки зрения обращения по индексам и не создает дублирующихся записей,
# увеличивая количество уже имеющихся заказов

# # order_dict = {}
#
# while True:
#     order_count = int(input('Введите кол-во заказов: '))
#     if order_count <= 0:
#         print('Должен быть хотя бы один заказ!\n')
#     else:
#         break
#
# count = 1
#
# # Т.к. отсутствуют какие-либо проверки ввода, в данном случае, лучше подойдёт цикл for.
# #  Количество строк кода будет меньше, избавимся от переменной count и лишних вычислений с ней.
# while order_count >= count:
#     new_order = input(f'{count} заказ: ').split()
#
#     customer, order, piz_count = new_order[0], new_order[1], int(new_order[2])
#
#     if not customer in order_dict:
#         order_dict[customer] = dict({order: piz_count})
#     elif order in order_dict[customer]:
#         order_dict[customer][order] += piz_count
#     else:
#         order_dict[customer][order] = piz_count
#     count += 1
#
# print()
#
# for member in sorted(order_dict.keys()):
#     print(f'{member}:')
#     for order in sorted(order_dict[member].keys()):
#         print(f'        {order}: {order_dict[member][order]}')


#зачОт