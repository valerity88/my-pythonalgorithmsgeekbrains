# Определить, какое число в массиве встречается чаще всего.
import random

array = [random.randint(0, 100) for _ in range(100)]
a = 0
n = 0

for i in array:
    k = 0
    for j in array:
        if j == i:
            k += 1
    if k > n:
        a = i
        n = k
print(array)
print(f'Число {a} в массиве встречается чаще всего - {n} раз')


