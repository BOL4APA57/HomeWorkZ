# Задача 2. Коллекторы
# Что нужно сделать
# Напишите робота для коллекторов. В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор, пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга робот сообщает об этом пользователю и благодарит его.

# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!

# Рекомендация
# Обратите внимание — считать сумму внесённых средств не нужно, это не соответствует условию задачи.

# Что оценивается
# input содержит корректное приглашение для ввода;
# результат вывода корректен;
# переменные имеют значащие имена, не только a, b, c, d (видео 2.3);
# правильное употребление пробелов после запятых и при бинарных операциях.

name = input('Введите имя должника:')
cost = int(input('Введите сумму долга:'))

print(name, ', ваша задолженность составляет ', cost, ' рублей.', sep='')
money = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?'))

while money < cost:
    print('Маловато, ', name, '. Давайте ещё раз.', sep='')
    money = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?'))

print('Отлично, ', name, '! Вы погасили долг. Спасибо!', sep='')