# Задача 6. Монетка

# Что нужно сделать

# Практиканту дали задание найти старую металлическую монетку по заданным координатам.
# Металлоискатель сканирует местность вокруг пользователя, и при обнаружении/отсутствии металла прибор отображает на экране соответствующее сообщение.
# Даны два действительных числа x и y. Напишите функцию, которая проверяет, принадлежит ли точка с координатами (x, y)
# заштрихованному квадрату (включая его границу). Если точка принадлежит квадрату, выведите сообщение «Монетка где-то рядом»,
# в противном случае выведите сообщение «Монетки в области нет». На рисунке сетка проведена с шагом 1.

# Что оценивается
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# формат вывода соответствует условию («Монетка где-то рядом», «Монетки в области нет»);
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

#def start
def treasure(x, y):
    if abs(x) <= 1 and abs(y) <= 1:
        print("Монетка где-то рядом! ^_^")
    else:
        print("Монетки в области нет... :-/")
# def end
print("Введите координаты:")
treasure(float(input("Х: ")), float(input('Y: ')))