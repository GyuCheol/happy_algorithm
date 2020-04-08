n = input()
num_list =  list()
for i in n:
    num_list.append(int(i))
num_list = reversed(sotred(num_list))
res = ''
for i in num_list:
    res += str(i)
print(res)


new = sorted(n)
for i in range(-1,0,-1):
    print('n', end = '')
