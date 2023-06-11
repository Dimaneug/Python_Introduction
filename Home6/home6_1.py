"""
Напишите программу, генерирующую элементы арифметической прогрессии
Программа принимает от пользователя три числа :

Первый элемент прогрессии, 
Разность (шаг),
Количество элементов
"""


# a - первый элемент
# d - шаг прогрессии
# n - кол-во элементов
def arithmetic_progression(a, d, n):
    return [a + (i - 1) * d for i in range(1, n + 1)]


a, d, n = [
    int(val)
    for val in input("Введите первый элемент, шаг и кол-во элементов: ").split()
]

print(arithmetic_progression(a, d, n))
