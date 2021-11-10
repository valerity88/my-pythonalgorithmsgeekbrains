import cProfile

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Тест {i} OK')

def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]
    return _fib_dict(n)

# test_fib(fib_dict)

#task_4_4.fib_dict(10)
#1000 loops, best of 5: 6.85 usec per loop

#task_4_4.fib_dict(15)
#1000 loops, best of 5: 8.57 usec per loop

#task_4_4.fib_dict(20)
#1000 loops, best of 5: 11.2 usec per loop

#task_4_4.fib_dict(100)
#1000 loops, best of 5: 57.7 usec per loop

#task_4_4.fib_dict(200)
#1000 loops, best of 5: 170 usec per loop

#task_4_4.fib_dict(500)
#1000 loops, best of 5: 361 usec per loop

#task_4_4.fib_dict(1000)
#RecursionError: maximum recursion depth exceeded

cProfile.run('fib_dict(500)')
# 19/1    0.000    0.000    0.000    0.000 task_4_4.py:12(_fib_dict) 10
# 39/1    0.000    0.000    0.000    0.000 task_4_4.py:12(_fib_dict) 20
# 199/1    0.000    0.000    0.000    0.000 task_4_4.py:12(_fib_dict) 100
# 999/1    0.001    0.000    0.001    0.001 task_4_4.py:12(_fib_dict) 500