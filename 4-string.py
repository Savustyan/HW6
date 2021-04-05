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


def string_math(Some_String):
    number = 0
    result = []
    for n in Some_String:
        if n == 'i':
            number += 1
        elif n == 'd':
            number -= 1
        elif n == 's':
            number = number ** 2
        elif n == 'o':
            result.append(number)
    return result


print(string_math('iiisdoso'))

