# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
print('Введите три разных числа')
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))
if (a < b and a > c) or (a < c and a > b):
    print(f'Среднее = {a}')
elif (b > a and b < c) or (b < a and b >c):
    print(f'Среднее = {b}')
elif a == b or b == c or a ==c:
    print('Неверный ввод')
else:
    print(f'Среднее = {c}')