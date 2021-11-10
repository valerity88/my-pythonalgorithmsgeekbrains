# Определить, является ли год, который ввел пользователь, високосным или не високосным.
input_year = int(input('Введите год: '))
if input_year % 4 != 0:
    print('Обычный год')
elif input_year % 100 == 0:
    if input_year % 400 == 0:
        print('Високосный год')
    else:
        print('Обычный год')
else:
    print('Високосный год')