# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
sum1 = 0
sum2 = 0
num2 = ''
while True:
    num = input('Введите число или "end" для завершения: ')
    if num == 'end':
        break
    for i in range(len(num)):
        sum1 += int(num[i])
    if sum2 <= sum1:
        sum2 = sum1
        num2 = num
        sum1 = 0
    
print(f'Наибольшая сумма цифр у числа {num2} = {sum2}')







    
    
