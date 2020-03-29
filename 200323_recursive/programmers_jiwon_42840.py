
def solution(answers):

    a1 = [1,2,3,4,5] * 2000
    b2 = [2,1,2,3,2,4,2,5]* 1250
    c3 = [3,3,1,1,2,2,4,4,5,5] * 1000

    p = [0]*3

    for i,j in zip(a1,answers):
        if i == j:
            p[1] += 1
    
    for i,j in zip(b2,answers):
        if i == j:
            p[2] += 1

    for i,j in zip(c3,answers):
        if i == j:
            p[3] += 1

    return p 


