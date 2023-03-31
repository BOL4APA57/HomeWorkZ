# Задача 1. Календарь

# Что нужно сделать
# Мы продолжаем разрабатывать удобный календарь для смартфона. Функцию определения високосного года мы добавили,
# но забыли ещё много разных очевидных вещей.

# Напишите программу, которая принимает от пользователя день недели в виде строки и выводит его номер на экран.

# Пример:
# Введите день недели: вторник
# Номер дня недели: 2

# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);
# переменные имеют значащие имена, не только a, b, c, d (видео 2.3).

# Советы и рекомендации
# Рекомендуется использовать цикл for и список/кортеж для представления дней недели

# for day in (‘понедельник’, ‘вторник’, ‘среда’...):

week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

day = input('Введите день недели: ')
if day not in week:
    print('Введены некорректные данные.')
else:
    print('Номер введенного дня недели:', week.index(day) + 1)