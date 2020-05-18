'''
분할정복 알고리듬 연습
(Divide and Conquer)
Merge Sort
'''

import random

def merge_sort(ary, p, q):

    if p == q:
        return

    m = (p + q) // 2

    merge_sort(ary, p, m)
    merge_sort(ary, m + 1, q)
    merge(ary, p, m + 1, q)

def merge(ary, i, j, e):
    tmp = []

    # ary i -> j -> tmp에 오름차순 집어넣기
    l = e - i + 1
    p = i
    q = j

    while len(tmp) != l:
        if q > e or (p < j and ary[p] < ary[q]):
            tmp.append(ary[p])
            p += 1
        else:
            tmp.append(ary[q])
            q += 1

    # tmp >> ary에 집어넣기
    for id, x in enumerate(range(i, e + 1)):
        ary[x] = tmp[id]


l = [1, 7, 1, 6, 5, 9, 3, 4, 2, 8, 4, 5]

print(l)
merge_sort(l, 0, len(l) - 1)
print('------Sorting------')
print(l)


