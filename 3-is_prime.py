"""
3. Напишите функция is_prime, которая принимает 1 аргумент (число) и возвращает True, если число простое, иначе False
Простое число - это число, которое делится без остатка только на себя и на 1
"""


def is_prime(number):
    if number > 1 and number % 2 != 0:
        d = 3
        while number % d != 0:
            d += 2
        if d == number:
            return True
    return False


print(is_prime(97))
