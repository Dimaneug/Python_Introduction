"""На столе лежат n монеток. Некоторые из них лежат 
вверх решкой, а некоторые – гербом. Определите 
минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и 
той же стороной. Выведите минимальное количество 
монет, которые нужно перевернуть. Количество монет и 
их положение (0 или 1) пользователь вводит с клавиатуры."""

orel = 0
reshka = 0

for i in range(int(input("Введите кол-во монет: "))):
    if input("Положение монеты "+str(i)+": ") == '1':
        orel += 1
    else:
        reshka += 1

print(str(orel) if orel < reshka else str(reshka))
