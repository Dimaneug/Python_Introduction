"""
Напишите функцию 
print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент 
по номеру строки и столбца, т.е. функцию двух аргументов. Аргументы 
num_rows и num_columns указывают число строк и столбцов таблицы, 
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.
"""


def print_operation_table(operation, num_rows=6, num_columns=6):
    print(" " * 4, end="")
    for j in range(1, num_columns + 1):
        print(f"{j:4d}", end="")
    print("\n" + " " * 4 + "-" * 4 * num_columns)
    for i in range(1, num_rows + 1):
        print(f"{i:<2d}| ", end="")
        for j in range(1, num_columns + 1):
            print(f"{operation(i,j):4d}", end="")
        print()


print_operation_table(lambda x, y: x**y, 4, 4)
print()
print_operation_table(lambda x, y: x * y)
