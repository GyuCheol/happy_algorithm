

def quick_sort(ary, begin, end):

    if end - begin < 2:
        return

    pivot = ary[end]
    i = begin - 1
    j = begin

    while True:
        if ary[j] < pivot:
            i += 1

        j += 1

    


l = [5, 6, 1, 4, 3, 7, 8, 9, 2]

print(l)
quick_sort(l, 0, len(l) - 1)
print(l)
