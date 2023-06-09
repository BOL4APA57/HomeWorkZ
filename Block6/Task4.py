# Задача 4. С заботой о природе
# Что нужно сделать
# Огромный заповедник поделён на большое количество секторов. Все сектора пронумерованы.
# Вы устроились на работу лесничим и отвечаете за группу секторов с номерами 30–35.
# В ваши обязанности входит:
# следить за тем, чтобы посетителей в каждом секторе было не больше десяти;
# фиксировать количество нарушений этого правила.
# Напишите программу, которая для каждого сектора запрашивает текущее количество людей в нём,
# и если оно больше десяти, то фиксирует нарушение. В конце выведите количество нарушений.

# Пример:
# Людей в 30-м секторе: 7
# Всё спокойно.
# Людей в 31-м секторе: 11
# Нарушение! Слишком много людей в секторе!
# Людей в 32-м секторе: 100
# Нарушение! Слишком много людей в секторе!
# Людей в 33-м секторе: 10
# Всё спокойно.
# Людей в 34-м секторе: 0
# Всё спокойно.
# Людей в 35-м секторе: 1
# Всё спокойно.
# Количество нарушений: 2

# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# формат вывода соответствует примеру;
# в итоговом выводе есть общее число нарушений;
# переменные имеют значащие имена, не только a, b, c, d;
# задача решена с помощью конструкции for.

warn = 0
for i in range(30, 36):
    humans = int(input(f'Людей в {i}-м секторе: '))
    if humans > 10:
        print('Нарушение! Слишком много людей в секторе!')
        warn += 1
    else:
        print('Всё спокойно.')
print() # Исключительно ради читабельности.
print('Количество нарушений:', warn)