import random
size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)
def selection_sort(array):

    for i in range(len(array)):
        ind_min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[ind_min]:
                ind_min = j
        array[ind_min], array[i] = array[i], array[ind_min]
        print(array)

selection_sort(array)
print(array)
