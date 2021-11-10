# На улице встретились N друзей.
# Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
n = int(input('Введите количество друзей: '))
array = []
k = 0
for i in range(0, n):
    array.append([])
    for j in range(n):
        if j <= i:
            array[i].append(0)
        elif j > i:
            array[i].append(1)
            k += 1

print(f'Граф: {array}')
print(f'Количество рукопожатий: {k}')