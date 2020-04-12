from collections import Counter

print(Counter(['A', 'B', 'A', 'C', 'A']))

d = {}

l = [x for x in 'ABABBBABACC']

for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

