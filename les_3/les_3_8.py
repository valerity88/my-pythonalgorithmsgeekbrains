#  Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
#  Программа должна вычислять сумму введенных элементов каждой строки
#  и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
matrix = []
for i in range(0, 4):
    matrix.append([])
    sum = 0
    for k in range(0, 4):
        num = float(input(f'Введите {k}-й элемент {i}-й строки: '))
        matrix[i].append(num)
        sum += num

    matrix[i].append(sum)

print('Матрица:')
for line in matrix:
    for item in line:
        print(f'{item:>6}', end = '')
    print()

