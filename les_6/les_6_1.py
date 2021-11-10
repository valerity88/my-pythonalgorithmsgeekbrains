# Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.

# 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] win32

# Задание 7 к уроку 3
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import sys
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

print('Переменные размер которых можно узнать: array, min1, min2')

while True:
    var = input('Введите переменную, чтобы узнать размер выделенной памяти, либо введите "end" для завершения: ')
    if var == 'array':
        print(f'Размер памяти выделенный под переменную {var} равен {sys.getsizeof(array)}')

    elif var == 'min1':
        print(f'Размер памяти выделенный под переменную {var} равен {sys.getsizeof(min1)}')

    elif var == 'min2':
        print(f'Размер памяти выделенный под переменную {var} равен {sys.getsizeof(min2)}')

    elif var == 'end':
        break
    else:
        print('Неверный ввод переменной' )

