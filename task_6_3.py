allocated = 0

for newsize in range(100):

    if allocated < newsize:
        new_allocated = (newsize >> 3) + (3 if newsize < 9 else 6)

        allocated = newsize + new_allocated
    print(newsize, allocated)
