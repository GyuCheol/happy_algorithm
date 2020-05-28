def solution(n, m):
    answer = []
    tmp1,tmp2 = n,m
    if m%n == 0:
        answer.append(tmp1)
        answer.append(tmp2)
    else:
        while m:
            n,m = m, n%m
        answer.append(n)
        answer.append(tmp1*tmp2/n^2)   



    return answer

print(solution(12,18))