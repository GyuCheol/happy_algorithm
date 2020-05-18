import time

l = [x for x in range(100)]
s = {x for x in range(100)}

print(time.ctime())

for i in range(10000000):
    if 99 in l: # O(n)
        pass

print(time.ctime())

for i in range(10000000):
    if 99 in s: # O(1)
        pass

print(time.ctime())

