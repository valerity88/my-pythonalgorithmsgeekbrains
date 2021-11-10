# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0)
# и 2 нечетные (3 и 5).

num = input('Введите число: ')
j = 0
k = 0
num_even = []
num_odd = []
for i in range(len(num)):
    if int(num[i]) % 2 == 0:
        j += 1
        num_even.append(int(num[i]))
    else:
        k += 1
        num_odd.append(int(num[i]))
print(f'Количество четных чисел {j}, это числа {num_even}')
print(f'Количество нечетных чисел {k}, это числа {num_odd}')
