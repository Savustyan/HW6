"""
2. Написать функцию, которая вернет True если число четное и False если не четное
"""
def even_or_not (num):
    if int(num) % 2 == 0:
        return True
    return False
print(even_or_not(input('Input any number: ')))