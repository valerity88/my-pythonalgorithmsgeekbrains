import cProfile
import functools

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Тест {i} OK')

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)



# "import task_4_7" "task_4_7.fib(10)"
# 1000 loops, best of 5: 247 nsec per loop

# "import task_4_7" "task_4_7.fib(100)"
# 1000 loops, best of 5: 237 nsec per loop

# "import task_4_7" "task_4_7.fib(200)"
# 1000 loops, best of 5: 257 nsec per loop

# "import task_4_7" "task_4_7.fib(500)"
#RecursionError: maximum recursion depth exceeded in comparison
cProfile.run('fib(200)')

# 11/1    0.000    0.000    0.000    0.000 task_4_7.py:10(fib) 10
# 101/1    0.000    0.000    0.000    0.000 task_4_7.py:10(fib) 100
# 201/1    0.001    0.000    0.001    0.001 task_4_7.py:10(fib) 200
