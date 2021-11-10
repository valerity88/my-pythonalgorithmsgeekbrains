# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from _collections import defaultdict, deque
companies = defaultdict()
profit_less_middle = deque()
profit_more_middle = deque()
n = int(input('Введите количество предприятий: '))
profit_sum = 0
for i in range(1, n + 1):
    name = input(f'Введите название {i}-го предприятия: ')
    profit = 0
    quater = 1
    while quater <= 4:
        profit_quater = float(input(f'Введите прибыль за {quater}-й квартал: '))
        profit += profit_quater
        quater += 1
    companies[name] = profit
    profit_sum += profit
profit_middle = profit_sum / n
print(f'Средняя прибыль за год для всех {n}-х предприятий равна {profit_middle}')
for i, item in companies.items():
    if item < profit_middle:
        profit_less_middle.append(i)
    if item > profit_middle:
        profit_more_middle.append(i)
print(f'Предприятия, чья прибыль выше среднего: \n {profit_more_middle}')
print(f'Предприятия, чья прибыль ниже среднего: \n {profit_less_middle}')
