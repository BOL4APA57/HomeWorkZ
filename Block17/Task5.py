# Задание 5. Пароль
# Что нужно сделать
# При регистрации на сайте, помимо логина, нужно придумать пароль. Этот пароль должен состоять минимум
# из восьми символов, содержать хотя бы одну большую букву и не менее трёх цифр. Тогда он будет считаться надёжным.
#
# Напишите программу, которая просит пользователя придумать пароль до тех пор, пока этот пароль не станет надёжным.
# Должна использоваться латиница.
#
# Пример
#
# Придумайте пароль: qwerty.
#
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qwerty12.
#
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qwerty123.
#
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qWErty123.
#
# Это надёжный пароль.
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.


up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
check = False
while not check:
    password = input("Придумайте пароль: ")
    numcheck, upcheck = 0, False
    for s in password:
        if s in up:
            upcheck = True
        if s.isnumeric():
            numcheck += 1

    if len(password) > 8 and upcheck and numcheck >= 3:
        print("Это надёжный пароль.")
        check = True
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")


# TO DO строка password = input("Придумайте пароль: ") встречается в коде дважды, можно сделать так,
# чтобы она не повторялась, а то моветон-с)

# Done
#зачОт