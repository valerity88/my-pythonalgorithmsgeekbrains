# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы
import random

size = 10
arr = [random.randint(-100, 100) for i in range(size)]

print(f'Исходный массив: {arr}')
def bubble_sort(array):
    n = 1
    while n < len(array):
        for k in range(len(array) - n):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
        n += 1
    return array
new_arr = bubble_sort(arr)
print(f'Отсортированный массив: {new_arr}')