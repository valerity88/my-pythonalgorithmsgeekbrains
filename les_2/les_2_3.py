# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
num = input('Введите число: ')
ind_new = len(num)- 1
new_num = ''
while ind_new >= 0:
    new_num += num[ind_new] 
    ind_new -= 1
print(f' Число в обратном порядке {new_num}')
    
