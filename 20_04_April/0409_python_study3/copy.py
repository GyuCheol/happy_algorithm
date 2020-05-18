'''
Shallow(얕은) copy : 얕은 사본을 만듦
vs
Deep(깊은) copy : 똑같은 깊은 사본을 만듦
'''
import copy

from collections import deque

l = [
    [1, 2, 3], 
    [4, 5, 6]
]

l2 = l.copy()           # shallow copy
l3 = copy.deepcopy(l)   # deep copy

l[0][0] = 5

print(l[0][0])  # -> 5
print(l2[0][0]) # -> 5!!!!
print(l3[0][0]) # -> 1

q = deque()

q.append(1)
q.popleft()

number = input()
n = []
for i in range(number):
    n.append(list(map(int,input().split())))


# [ (x,y) for x,y in range(number)]   
# n = sorted(n, key = lambda x: (x[0]))

# (x,y)의 좌표 정렬
# x y
# x y
# x y

# (x,y),(x,y)
# x[0] ->(1,2),(1,2)
