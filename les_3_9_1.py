# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
print(f'Матрица: {matrix}')
print(len(matrix))
print(len(matrix[1]))
for i in range(len(matrix)):
    for k in matrix[i]:

