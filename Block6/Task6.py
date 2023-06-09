# Задача 6. Успеваемость в классе
# Что нужно сделать
# В классе N человек. Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
# Напишите программу, которая получает список оценок — N чисел — и выводит на экран сообщение о том, кого сегодня больше:
# отличников, хорошистов или троечников.
# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# в выводе присутствует сообщение о том, кого больше;
# для решения используется цикл for, а не встроенные функции или рекурсия;
# переменные имеют значащие имена, не только a, b, c, d.

children = int(input('Введите количество учеников: '))
n3, n4, n5 = 0, 0, 0
for i in range(children):
    mark = int(input('Введите оценку ученика: '))
    if mark == 3:
        n3 += 1
    elif mark == 4:
        n4 += 1
    elif mark == 5:
        n5 += 1
    else:
        print('Ввод некорректен!')

print() # разграничение ввода и вывода.
if n3 > n4 and n3 > n5:
    print('Сегодня больше троечников.')
elif n4 > n3 and n4 > n5:
    print('Сегодня больше хорошистов.')
else:
    print('Сегодня больше отличников.')