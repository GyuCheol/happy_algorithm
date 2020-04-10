n = int(input())

d = {}

for i in range(n):
    name, action = tuple(input().split(' '))

    d[name] = action

    if action == 'leave':
        del d[name]
    
    # print(d)

names = sorted(d, reverse=True)

print('\n'.join(names))

    #{name:state for i in }