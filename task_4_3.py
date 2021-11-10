import cProfile
def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Тест {i} OK')
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

cProfile.run('fib(25)')

#cProfile.run('fib(10)')
#177/1    0.000    0.000    0.000    0.000 task_4_3.py:7(fib)

#cProfile.run('fib(15)')
# 1973/1    0.001    0.000    0.001    0.001 task_4_3.py:7(fib)

#cProfile.run('fib(20)')
# 21891/1    0.006    0.000    0.006    0.006 task_4_3.py:7(fib)

#cProfile.run('fib(25)')
#242785/1    0.094    0.000    0.094    0.094 task_4_3.py:7(fib)


#test_fib(fib)

#task_4_3.fib(10)
#1000 loops, best of 5: 30.7 usec per loop

#task_4_3.fib(15)
#1000 loops, best of 5: 299 usec per loop

#task_4_3.fib(20)
#1000 loops, best of 5: 3.44 msec per loop

#task_4_3.fib(20)
#1000 loops, best of 5: 3.44 msec per loop