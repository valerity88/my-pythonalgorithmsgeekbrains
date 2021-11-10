# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать
import random

array = [random.randint(0, 10) for _ in range(10)]
min = array[0]
min_index = 0
max = array[0]
max_index = 0
sum = 0
print(f'Массив: {array}')

for i in range(1, len(array)):

    if min > array[i]:
        min_index = i
        min = array[i]
    if max < array[i]:
        max_index = i
        max = array[i]

if max_index > min_index:
    for i in range(min_index + 1, max_index):
        sum += array[i]
else:
    for i in range(max_index + 1, min_index):
        sum += array[i]

print(f'Сумма элементов, находящихся между минимальным и максимальным элементами: {sum}')
