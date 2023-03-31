# Задача 6. Анализ слова
# Что нужно сделать

# Напишите программу — анализатор слов, чтобы использовать её для тренировки нейросети и генерировать нужный текст.
# Пользователь вводит слово. Напишите программу, которая считает количество уникальных букв в слове.
# Уникальные буквы — это те, которые встречаются всего один раз.
 
# Пример 1:
# Введите слово: привет
# Количество уникальных букв: 6

# Пример 2:
# Введите слово: лава
# Количество уникальных букв: 2

# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

word, case = input("Введите слово:"), ""
word = word.upper()
for char in word:
    if char not in case:
        case +=char
print("Количество уникальных букв:", len(case))