#Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв
letter_1 = input('Введите первую букву: ')
letter_2 = input('Введите вторую букву: ')
print(f'Место первой буквы в алфавите - {ord(letter_1) - 96}')
print(f'Место второй буквы в алфавите - {ord(letter_1) - 96}')
print(f'Между ними - {abs(ord(letter_2) - ord(letter_1))-1} букв')