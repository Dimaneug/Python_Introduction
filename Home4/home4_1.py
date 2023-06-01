"""Даны два неупорядоченных набора целых чисел 
(может быть, с повторениями). Выдать без повторений 
в порядке возрастания все те числа, которые 
встречаются в обоих наборах. Если таких чисел нет - 
выдать внятное диагностическое сообщение
Наборы (списки) чисел можно считать заданными и не 
вводить с клавиатуры"""


numbers1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
numbers2 = [3, 6, 9, 12, 15, 18]

nums1_set = set(numbers1)
nums2_set = set(numbers2)

result = sorted(nums1_set.intersection(nums2_set))
if result:
    print(" ".join(str(val) for val in result))
else:
    print("Повторяющихся чисел нет")

