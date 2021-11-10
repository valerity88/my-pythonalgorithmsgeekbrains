# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

array = [random.randint(0, 100) for _ in range(100)]
min = array[0]
min_index = 0
max = array[0]
max_index = 0
print(f'Исходный массив: {array}')

for i in range(1, len(array)):

    if min > array[i]:
        min_index = i
        min = array[i]
    if max < array[i]:
        max_index = i
        max = array[i]

array[max_index] = min
array[min_index] = max
print(f'Измененный массив: {array}')

print(min_index, min)
print(max_index, max)