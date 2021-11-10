# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

array = [random.randint(0, 10) for _ in range(10)]
min1 = array[0]
min1_ind = 0
min2 = array[1]
min2_ind = 1

print(f'Массив: {array}')

for i in range(2, len(array)):
    if min1 > array[i]:
        min2_ind = min1_ind
        min2 = min1
        min1 = array[i]
        min1_ind = i
    elif min2 > array[i]:
        min2 = array[i]
        min2_ind = i


print(f'Два наименьших элемента: {min1, min2} с индексами {min1_ind, min2_ind}')