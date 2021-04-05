"""
1. Написать любую детерменированную функцию (Детерменированная функция = функция, которая возвращает одно и тоже вне
зависимости от парамеметров)
"""
def determin (Some_String):
    Some_String = Some_String.upper()
    return Some_String

print(determin(input('Input any string: ')))