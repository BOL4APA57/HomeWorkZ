# Задача 9. ...Теперь можно посчитать и свою
# Что нужно сделать
# Пока бухгалтер считала среднюю зарплату сотрудников, ей стало интересно, а не зря ли она работает столько времени на одном месте?
# Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.
# Пользователь вводит десять чисел. Напишите программу, которая проверяет, упорядочены ли они по возрастанию.

# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержат корректные приглашения для ввода;
# в выводе есть один окончательный ответ, который отвечает на поставленный вопрос о возрастании зарплаты;
# переменные имеют значащие имена, не только a, b, c, d.

check = True
pred = 0
for _ in range(10):
    month = int(input('Введите зарплату за месяц:'))
    if month < pred:
        check = False
    pred = month

print() # разграничение ввода и вывода.
if check:
    print('Заработная плата стабильно увеличивается.')
else:
    print('Увеличение заработной платы нестабильно.')

# Второй вариант.
check = True
pred = 0
for _ in range(10):
    month = int(input('Введите зарплату за месяц:'))
    if month <= pred:
        check = False                                       # Срываем флаг проверки.
        print('Обнаружено неувеличение заработной платы!')  # Выводим сообщение о проблеме с ЗП.
        break                                               # Прерываем цикл, дабы не тратить время на уже ненужные итерации.
    pred = month

print() # разграничение ввода и вывода.
if check:
    print('Заработная плата стабильно увеличивается.')