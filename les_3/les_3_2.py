# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.
import random

array = [random.randint(0,100) for _ in range(100)]
array_index = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        array_index.append(i)
print(f'Исходный массив: {array}')
print(f'Массив индексов четных элементов: {array_index}')