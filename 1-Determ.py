"""
1. Написать любую детерменированную функцию (Детерменированная функция = функция, которая возвращает одно и тоже вне
зависимости от парамеметров)
"""
def determin (str):
    str = str.upper()
    return str

print(determin(input('Input any string: ')))