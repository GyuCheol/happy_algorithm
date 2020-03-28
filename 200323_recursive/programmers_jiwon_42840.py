import random
def solution(answers):

    a1 = [1,2,3,4,5] * 2000
    b2 = [2,1,2,3,2,4,2,5]* 1250
    c3 = [3,3,1,1,2,2,4,4,5,5] * 1000

    p = [0]*3
    q = [random.randint(1,6) for r in range(10000)]

    for i,j in zip(a1,q):
        if i == j:
            p[1] += 1
    
    for i,j in zip(b2,q):
        if i == j:
            p[2] += 1

    for i,j in zip(c3,q):
        if i == j:
            p[3] += 1

    return p        


        

    




    answer = []
    return answer