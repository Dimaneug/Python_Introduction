"""
Определить индексы элементов массива (списка), значения которых 
принадлежат заданному диапазону (т.е. не меньше заданного минимума 
и не больше заданного максимума)
"""


def find_indexes_from_range(nums: list, lower: int, upper: int):
    return [(i, val) for i, val in enumerate(nums) if lower <= val <= upper]


lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

print(find_indexes_from_range(lst1, 2, 10))
print(find_indexes_from_range(lst1, 2, 9))
print(find_indexes_from_range(lst1, 0, 6))
