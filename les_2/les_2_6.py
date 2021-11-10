# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.
import random

x = random.randint(0, 100)
for i in range(10):
    y = int(input('Введите целое число в диапозоне от 0 до 100: '))
    if y < x:
        print('Загаданное число немного больше.')
    elif y > x:
        print('Загаданное число немного меньше.')
    if x == y:
        print('Вы угадали!')
        break

print(f'Загаданное число = {x}')

