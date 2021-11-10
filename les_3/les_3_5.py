# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random

array = [random.randint(-100, 100) for _ in range(100)]
min_ind = 0
k = array[min_ind]
for i in range(len(array)):
    if k > 0 and array[i] < k:
        k = array[i]
    if k < 0 and k < array[i] < 0:
        k = array[i]
print(f'Массив: {array}')
print(f'Максимальный отрицательный элемент: {k}')

