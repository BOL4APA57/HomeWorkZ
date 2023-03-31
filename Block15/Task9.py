# Задача 9. Друзья
# Что нужно сделать
#
# N друзей постоянно берут в долг друг у друга деньги. В какой-то момент им надоело забывать, кто, кому и сколько должен,
# и они придумали систему долговых расписок. И, чтобы начать новый год «с чистого листа»,
# друзья решили оплатить все долговые расписки, которые накопились у них друг к другу. Однако выяснилось,
# что иногда один и тот же человек в разные дни выступал как в роли должника, так и в роли кредитора.
#
# Напишите программу, которая по заданным распискам вычислит, сколько всего должен каждый друг выплатить другим (или получить с других).
#
# Сначала вводится число N — количество друзей, затем вводится число K — количество долговых расписок,
# после этого следует K троек чисел: номер друга, взявшего в долг, номер друга, давшего деньги, и сумма.
# Гарантируется, что ни один друг не брал в долг сам у себя.
#
# Программа должна вывести «баланс друзей», то есть суммы, которые должны получить или отдать друзья.
# Положительное число означает, что друг должен получить деньги от других, отрицательное — должен отдать деньги.
#
# Пример 1:
#
# Кол-во друзей: 2
#
# Долговых расписок: 3
#
# 1-я расписка
#
# Кому: 1
#
# От кого: 2
#
# Сколько: 10
#
# 2-я расписка
#
# Кому: 1
#
# От кого: 2
#
# Сколько: 20
#
# 3-я расписка
#
# Кому: 1
#
# От кого: 2
#
# Сколько: 20
#
# Баланс друзей:
#
# 1: -50
#
# 2: 50
#
# Пример 2:
#
# Кол-во друзей: 3
#
# Долговых расписок: 1
#
# 1-я расписка
#
# Кому: 3
#
# От кого: 1
#
# Сколько: 100
#
# Баланс друзей:
#
# 1 : 100
#
# 2 : 0
#
# 3 : -100
#
# Что оценивается
#
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
#
#

# def start
def check(ask):
    while not ask.isdigit():
        ask = input("Ошибка! Некорректный ввод. Введите число: ")
    return int(ask)
# def end


men = check(input("Введите количество человек: "))

people = [0 for _ in range(men)]
cost = check(input("Введите количество расписок: "))

for i in range(cost):
    print(f"\n{i + 1}-я расписка.\n")
    to_who = check(input("Кому: ")) - 1
    from_who = check(input("От кого: ")) - 1
    money = check(input("Сколько: "))
    #Боль группового присваивания... эх
    # Check \ Done
    people[to_who] -= money
    people[from_who] += money

print("\nБаланс друзей:\n")

for i in range(men):
    print(i + 1, ":", people[i])
#ЗачОт