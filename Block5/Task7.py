# Задача 7. Обычный день на работе
# Что нужно сделать
# Максим программирует целый день на работе и вечером идёт домой. Каждый час начальство кидает ему несколько задач,
# которые нужно решить до следующего рабочего часа. Вдобавок каждый час Максиму звонит супруга.
# Он знает, что если он возьмёт трубку, то жена попросит зайти вечером в магазин.
# Напишите программу, в которой считается, сколько задач выполнил Максим за день (8 часов).
# Если он хоть раз взял трубку, то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».

# Пример:
# Начался 8-часовой рабочий день
# 1-й час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1 — да, 0 — нет):  0
# 2-й час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 3-й час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1 — да, 0 — нет):  0
# 4-й час
# Сколько задач решит Максим? 4
# Звонит жена. Взять трубку? (1 — да, 0 — нет):  1
# 5-й час
# Сколько задач решит Максим? 5
# Звонит жена. Взять трубку? (1 — да, 0 — нет):  0
# 6-й час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1 — да, 0 — нет):  0
# 7-й час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1 — да, 0 — нет):  1
# 8-й час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1 — да, 0 — нет):  0

# Рабочий день закончился. Всего выполнено задач: 21
# Нужно зайти в магазин.

# Что оценивается
# input содержит корректное приглашение для ввода;
# формат вывода соответствует примеру;
# число итераций не превосходит число рабочих часов;
# используется флаг для учёта факта звонка жены;
# переменные имеют значащие имена, не только a, b, c, d (видео 2.3);
# правильное употребление пробелов после запятых и при бинарных операциях.

wife = False
count = 0
print() # Исключительно ради эстетики вывода.
print('Начался 8-часовой рабочий день')

for i in range(1, 9):
    print() # Для удобочитаемости и разделения по часам.
    print(i,'-й час', sep='')
    work = int(input('Сколько задач решит Максим? '))
    count += work
    call = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    if call == 1:
        wife = True
print()
print() # Для удобочитаемости.
print('Рабочий день закончился. Всего выполнено задач: ', count)
if wife == True:
    print('Нужно зайти в магазин.')