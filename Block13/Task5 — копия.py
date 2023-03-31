# Задача 5. Недоделка 2
# Что нужно сделать
# Вы всё так же работаете в конторе по разработке игр и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами, вам нужно было написать код по следующим условиям:
# программа получает на вход два числа. В первом числе должно быть не меньше трёх цифр, во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку. Если всё нормально, то в каждом числе первая и последняя цифра меняются местами, а затем выводится их сумма.
# И тут вы натыкаетесь на программу, которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код, чтобы он не выглядел так ужасно. Да и вам самим становится, мягко говоря, не по себе от него.
# Разбейте приведённую ниже программу на функции. Повторений кода должно быть как можно меньше.
# Также сделайте, чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.
#
# first_n = int(input("Введите первое число: "))
# first_num_count = 0
# temp = first_n
# while temp > 0:
#     first_num_count += 1
#     temp = temp // 10
# if first_num_count < 3:
#  print("В первом числе меньше трёх цифр.")
# else:
#  last_digit = first_n % 10
#  first_digit = first_n // 10  (first_num_count - 1)
#  between_digits = first_n % 10 (first_num_count - 1) // 10
#  first_n = last_digit * 10 (first_num_count - 1) + between_digits * 10 + first_digit
# print('Изменённое первое число:', first_n)
# second_n = int(input("\nВведите второе число: "))
# second_num_count = 0
# temp = second_n
# while temp > 0:
#    second_num_count += 1
#    temp = temp // 10
# if second_num_count < 4:
#    print("Во втором числе меньше четырёх цифр.")
#  else:
#    last_digit = second_n % 10
#    first_digit = second_n // 10 (second_num_count - 1)
#    between_digits = second_n % 10 (second_num_count - 1) // 10
#    second_n = last_digit * 10 (second_num_count - 1) + between_digits * 10 + first_digit
#    print('Изменённое второе число:', second_n)
#    print('\nСумма чисел:', first_n + second_n)

# Что оценивается
# программа разбита на несколько функций;
# выполнены условия по организации основного тела программы.


# def start

def check(first, second):
    ask = 0
    while ask < 2:
        ask = 0
        if first < 100:
            print("В первом числе меньше трёх цифр.")
        else:
            ask += 1
        if second <  1000:
            print("Во втором числе меньше четырёх цифр.")
        else:
            ask += 1
        if ask < 2:
            first, second = int(input("Повторите ввод:\nВведите первое число: ")), int(input("\nВведите второе число: "))
    return (first, second)

def twist(num):
    num_count = len(str(num))
    last = num % 10
    first = num // (10 ** (num_count - 1))
    body = num % (10 ** (num_count - 1)) // 10
    return ((last * (10 ** (num_count - 1)) + body * 10 + first))

# def end

f_num, s_num = check(int(input("Введите первое число: ")), int(input("\nВведите второе число: ")))

print('Изменённое первое число:', twist(f_num), '\nИзменённое второе число:', twist(s_num), '\nСумма чисел:', twist(f_num) + twist(s_num))
