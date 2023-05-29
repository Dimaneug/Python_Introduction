"""
Требуется найти в списке целых чисел самый близкий по 
величине элемент к заданному числу X. Пользователь вводит 
это число с клавиатуры, список можно считать заданным. 
Введенное число не обязательно содержится в списке.
"""

numbers = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
print(numbers)
x = int(input("Введите число: "))

min_difference = abs(x - numbers[0])
difference_value = numbers[0]

for number in numbers[1:]:
    if abs(x - number) < min_difference:
        min_difference = abs(x - number)
        difference_value = number
    
print(difference_value)
