# Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.

# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random
import cProfile

def max_negative_1(z):
    array = [random.randint(-z, z) for _ in range(z)]
    max_neg_ind = 0
    k = array[max_neg_ind]
    for i in range(len(array)):
        if k > 0 and array[i] < k:
            k = array[i]
            max_neg_ind = i
        if k < 0 and k < array[i] < 0:
            k = array[i]
            max_neg_ind = i
    return k, max_neg_ind, array


# "les_4_1.max_negative(100)"
# 1000 loops, best of 5: 188 usec per loop

# "les_4_1.max_negative(1000)"
# 1000 loops, best of 5: 2.07 msec per loop

# "les_4_1.max_negative(10000)"
# 1000 loops, best of 5: 23.5 msec per loop

def max_negative_2(z):
    array = [random.randint(-z, z) for _ in range(z)]
    array_new = []
    array_ind = []
    for index, i in enumerate(array):
        if i < 0:
            array_new.append(i)
            array_ind.append(index)
    return max(array_new), array_ind[array_new.index(max(array_new))], array

# "les_4_1.max_negative_2(100)"
# 1000 loops, best of 5: 168 usec per loop

# "les_4_1.max_negative_2(1000)"
# 1000 loops, best of 5: 1.85 msec per loop

# "les_4_1.max_negative_2(10000)"
# 1000 loops, best of 5: 24 msec per loop

def max_negative_3(z):
     array = [random.randint(-z, z) for _ in range(z)]
     num = float('-inf')
     index = -1
     for i, item in enumerate(array):
         if 0 > item > num:
             num = item
             index = i
     return num, index, array

# "les_4_1.max_negative_3(10)"
# 1000 loops, best of 5: 17.3 usec per loop

# "les_4_1.max_negative_3(1000)"
# 1000 loops, best of 5: 1.68 msec per loop

# "les_4_1.max_negative_3(10000)"
# 1000 loops, best of 5: 20 msec per loop

cProfile.run('max_negative_1(1000)')
cProfile.run('max_negative_2(1000)')
cProfile.run('max_negative_3(1000)')

# Скорость выполнения отличается незначительно,
# хотя в max_negative_2 создается два новых массива - для отрицательных чисел и их индексов,
# за счет чего увеличелось количество вызовов функции