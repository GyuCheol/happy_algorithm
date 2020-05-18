
'''
s = input()
# 1,10,3
# 5,10
# 10

number = list(map(lambda x: int(x), s.split(',')))

if len(number) == 3:
    print(list(range(number[0], number[1], number[2])))
elif len(number) == 2:
    print(list(range(number[0], number[1])))
else:
    print(list(range(number[0])))

print(list(range(*number)))
'''

l = []

def printing(i):
    print(i)

def printing2(i):
    print(i**2)

def append_something(i):
    l.append(i)

def for_each(func, iterable):

    for i in iterable:
        func(i)

number = [0, 1, 2, 3, 4]

# for_each(printing, number)
# for_each(printing2, number)
# for_each(append_something, number)

for_each(lambda x: print(x), number)
for_each(lambda x: print(x**2), number)
for_each(lambda x: l.append(x), number)

def func5(x: str, i: int) -> str:
    return x

ss = func5('asd', 3545)
