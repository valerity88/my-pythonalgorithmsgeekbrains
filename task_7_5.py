import random
size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

def quick_sort(array):

    if len(array) <= 1:
        return array
    pivot = random.choice(array)
    s_arr = []
    m_arr = []
    l_arr = []
    for item in array:
        if item < pivot:
            s_arr.append(item)
        elif item > pivot:
            l_arr.append(item)
        elif item == pivot:
            m_arr.append(item)
        else:
            raise Exception('Случилось непредвиденное')
    print(s_arr, m_arr, l_arr)
    return quick_sort(s_arr) + m_arr + quick_sort(l_arr)
array_new = quick_sort(array)
print(array_new)