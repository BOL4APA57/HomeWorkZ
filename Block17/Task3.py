# Задание 3. Файлы
# Что нужно сделать
# В IT-компании есть негласные правила именования текстовых документов:
#
# Название файла не может начинаться с одного из специальных символов: @, №, $, %, ^, &, *, ().
# Файл должен заканчиваться расширением .txt или .docx.
# Напишите программу, которая получает на вход полное название файла и проверяет, соответствует ли он этим правилам.
#
# Пример 1
#
# Название файла: @example.txt.
#
# Ошибка: название начинается недопустимым символом.
#
# Пример 2
#
# Название файла: example.ttx.
#
# Ошибка: неверное расширение файла. Ожидалось .txt или .docx.
#
# Пример 3
#
# Название файла: example.txt.
#
# Файл назван верно.
#
# Советы и рекомендации
# Метод endswith (как и startswith) можно использовать для проверки нескольких окончаний. Примеры такого использования.
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

restict = "@№$%^&*()"
name = input("Название файла: ")
if name[0] in restict:
    print("Ошибка: название начинается недопустимым символом.")
elif name[-4:] == ".txt" or name[-5:] == ".docx":
    print("Файл назван верно.")
else:
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")

#ЗачОт