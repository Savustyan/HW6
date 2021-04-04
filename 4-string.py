"""
4. Напишите функцию, которая принимает 1 аргумент (строка) и выполняет следующие действия на каждую из букв строки:
i - инкремент (+1)
d - дикремент (-1)
s - возведение в квадрат
o - добавить число в результативный список
остальные буквы игнорируются
Исходное число = 0
Результативный список = []
Вернуть результативный список
parse("iiisdoso")  ==>  [8, 64] <- это как пример
"""


def string_math(string):
    number = 0
    result = []
    n = 0
    while n < len(string):
        if string[n] == 'i':
            number += 1
            n += 1
        elif string[n] == 'd':
            number -= 1
            n += 1
        elif string[n] == 's':
            number = number ** 2
            n += 1
        elif string[n] == 'o':
            result.append(number)
            n += 1
        else:
            n += 1
    return result


print(string_math('iiisdoso'))

