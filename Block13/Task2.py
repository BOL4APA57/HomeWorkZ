# Задача 2. Функция максимума

# Что нужно сделать
# Юра пишет различные полезные функции для Питона, чтобы остальным программистам стало проще работать. 
# Он захотел написать функцию, которая будет находить максимум из перечисленных чисел. 
# Функция для нахождения максимума из двух чисел у него уже есть. Юра задумался: может быть, её можно как-то использовать для нахождения максимума уже от трёх чисел?
# Помогите написать Юре функцию, которая находит максимум из трёх чисел. Для этого используйте только функцию нахождения максимума из двух чисел.

# Что оценивается
# результат вывода соответствует условию;
# Найден корректный максимум трех чисел;
# input содержит корректное приглашение для ввода;
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);

# def start
def maxi(a,b,c):
    max = (abs(a - b) + (a + b)) / 2
    max = (abs(max - c) + (max + c)) / 2
    return max

# def end

fir, sec, thr = int(input("Введите первое число:")), \
                int(input("Введите второе число:")), \
                int(input("Введите третье число:"))

print("Наибольшее число:", maxi(fir,sec, thr))