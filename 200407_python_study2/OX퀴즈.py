n = int(input())
test = [input() for _ in range(n)]

for i in test:
    count = 0
    split = i.split('X')
    for O in split:
        
        len_n = len(O)
        if (len_n>0):
            count += (len_n*(len_n+1))//2
        
    print(count)


