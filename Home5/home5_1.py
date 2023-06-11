"""
Напишите рекурсивную функцию для возведения 
числа a в степень b. Разрешается использовать 
только операцию умножения. Циклы использовать нельзя
"""


def my_pow(a, b):
    if b == 1:
        return a
    if b == 0:
        return 1
    return a * my_pow(a, b - 1)


# print(my_pow(2, 0))
# print(my_pow(2, 1))
# print(my_pow(2, 3))
# print(my_pow(2, 4))
