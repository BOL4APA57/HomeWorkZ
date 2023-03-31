# Задача 3. Кривой мессенджер

# Что нужно сделать
# При передаче сообщений в одном мессенджере иногда возникают неполадки и в сообщение попадает лишний символ - звёздочка.
# Пользователям это изрядно надоело, и они начали просто уходить в другие мессенджеры.
# Хотя одному пользователю стало интересно, на каких обычно позициях появляется эта звёздочка.

# Чтобы это выяснить, пользователю необходимо подготовить строки в которых символ “*” встречается ровно один раз.
# Напишите программу, которая определяет порядковый номер этого символа в строке.

# Пример:
# Введите текст: Пр*ивет как дела
# Символ ‘*’ стоит на позиции 3

# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);
# Переменные имеют значащие имена, не только a, b, c, d (видео 2.3)

request = input('Введите текст: ')
if '*' not in request:
    print('Символ "*" не найден.')
else:
    print('Символ ‘*’ стоит на позиции', request.index('*') + 1)