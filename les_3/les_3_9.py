# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
print(f'Матрица: {matrix}')
min_l = []
min_l.extend(matrix[0])

for line in matrix:
    print(line)
    i = 0
    for j in line:
        if j < min_l[i]:
            min_l[i] = j
        i += 1
k = min_l[0]
for z in range(1, len(min_l)):
    if k < min_l[z]:
        k = min_l[z]

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {k}')

