
seq = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for x, y, z in seq:
    print(x, y, z)
else:
    print('hoooo')

i = 0

while i < 3:
    i += 1
    print(i)
else:
    print('me')

for i, c in enumerate(['A', 'B', 'C']):
    print(i, c)

# 0, A
# 1, B
# 2, C

a = 2

def func():
    global a

    a = 1
    print(a)

func()

print(a)

def f(pos, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass

f()


