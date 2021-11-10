# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.

import random

def median(array, k):
    if len(array) == 1:
        return array[0]

    pivot = random.choice(array)

    left = [i for i in array if i < pivot]
    right = [i for i in array if i > pivot]
    pivots = [i for i in array if i == pivot]

    if k < len(left):
        return median(left, k)
    elif k < len(left) + len(pivots):
        return pivots[0]
    else:
        return median(right, k - len(left) - len(pivots))


lst = [random.randint(0, 20) for _ in range(10)]
print(f'Исходный список:\n{lst}')
print(f'Медианa:\n{median(lst, len(lst) / 2)}')

