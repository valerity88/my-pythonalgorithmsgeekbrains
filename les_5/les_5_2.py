# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict
from collections import deque

hex_string = '0123456789ABCDEF'
hex_table = defaultdict(int)
c = 0
for key in hex_string:
    hex_table[key] += c
    c += 1

def number(string):
    number = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        number += hex_table[num[i]] * 16 ** i
    return number


def hex(x):
    num = deque()
    while x > 0:
        d = x % 16
        for i in hex_table:
            if hex_table[i] == d:
                num.append(i)
        x //= 16
    num.reverse()
    return list(num)

a = number(input('Введите первое число в шестнадцатиричном формате:\n ').upper())
b = number(input('Введите второе число в шестнадцатиричном формате:\n ').upper())

print(f'Сумма чисел равна {hex(a + b)}')
print(f'Произведение чисел равно {hex(a * b)}')