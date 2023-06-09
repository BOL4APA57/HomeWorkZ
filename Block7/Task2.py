# Задача 2. Долги

# Что нужно сделать
# «МирПрогБанк» наконец-то разделил законопослушных граждан и должников и поместил их в разные базы.
# Но банк не торопится сильно давить на неплательщиков. Операторам банка дали задание позвонить каждому пятому должнику из списка
# (нумерация начинается с нуля) и уточнить, какую сумму каждый из них задолжал банку.
# Напишите программу, которая получает данные о количестве должников, а затем спрашивает у каждого пятого (начиная с 0) его долг.
# В конце выводится общая сумма долгов.

# Пример 1:
# Введите количество должников: 13
# Должник с номером 0
# Сколько должны? 1000
# Должник с номером 5
# Сколько должны? 5000
# Должник с номером 10
# Сколько должны? 2000
# Общая сумма долга: 8000

# Пример 2:
# Введите количество должников: 10
# Должник с номером 0
# Сколько должны? 1000
# Должник с номером 5
# Сколько должны? 5000
# Общая сумма долга: 6000

# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# в выводе присутствует общая сумма долга;
# формат вывода соответствует примеру (не выведены числа без описания);
# для решения использован цикл for и range c шагом;
# переменные имеют значащие имена, не только a, b, c, d.

count = int(input('Введите количество должников: '))
dolg = 0
for i in range(0, count, 5):
    print('Должник с номером', i)
    dolg += int(input('Сколько должны? '))
print('Общая сумма долга: ', dolg)