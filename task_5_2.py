from collections import deque

a = deque()
b = deque('abcdef')
c = deque([1, 2, 3, 4, 5])
print(a, b, c, sep = '\n')

b = deque('abcdef', maxlen = 3)
c = deque([1, 2, 3, 4, 5], maxlen = 4)
c.clear()
print(b, c, sep = '\n')

print('*' * 50)
d = deque([i for i in range(5)])
d.append(5)
d.appendleft(6)
print(d)
d.extend([7, 8, 9])
d.extendleft([10, 11, 12])
print(d)

print('*' * 50)
d = deque([i for i in range(5)], maxlen = 7)
d.append(5)
d.appendleft(6)
print(d)
d.extend([7, 8, 9])
d.extendleft([10, 11, 12])
print(d)

print('*' * 50)
f = deque([i for i in range(5)], maxlen = 7)
x = f.pop()
y = f.popleft()
print(f, x, y, sep = '\n')

print('*' * 50)
g = deque([i for i in range(5)], maxlen = 7)
print(g.count(2))
print(g.index(3))
g.insert(2, 6)
print(g)

g.reverse()
print(g)

g.rotate(3)
print(g)

g.rotate(-3)
print(g)

import random

array = [random.randint(-100, 100) for _ in range(10)]
print(array)

# arr_below = []
# arr_lager = []

deq = deque()

for item in array:
    if item > 0:
        deq.append(item)
    elif item < 0:
        deq.appendleft(item)
print(deq)

# вместо кода
# import random
#
# array = [random.randint(-100, 100) for _ in range(100)]
# print(array)
#
# arr_below = []
# arr_lager = []
#
# for item in array:
#     if item > 0:
#         arr_lager.append(item)
#     elif item < 0:
#         arr_below.append(item)
#
# print(arr_below)
# print(arr_lager)
# arr_below1 = [item for item in array if item < 0]
# arr_lager1 = [item for item in array if item > 0]
#
# print(arr_below1)
# print(arr_lager1)

print('*' * 50)
with open('log.txt', 'r', encoding = 'utf-8') as f:
    last_ten = deque(f, 10)

print(last_ten)

