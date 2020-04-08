n = int(input())
test = [input() for _ in range(n))

for i in range(n):
    count = 0
    for OX in case:
        new = case.split('X')
        count = len(new[OX])*(len(new[OX])+1)/2
        
    print(count)



