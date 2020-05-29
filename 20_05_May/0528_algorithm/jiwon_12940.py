# def solution(n, m):
#     answer = []
#     tmp1,tmp2 = n,m
#     if m%n == 0:
#         answer.append(tmp1)
#         answer.append(tmp2)
#     else:
#         while m:
#             n,m = m, n%m
#         answer.append(n)
#         answer.append(tmp1*tmp2/n^2)   
# return answer

print(solution(12,18))

# 최대공약수에 대한 수학적 접근법 필요.
# 계산량을 늘려서 전체 탐색했다

def solution(n,m):
    mi = 0
    for i in range(1,min(n,m)+1):
        if n%i == 0 and m%i == 0:
            mi = i

    mx = 0
    for j in range(max(n,m), (n*m)+1):
        if j%n== 0 and j%m == 0:
            mx = j
            break
    return [mi,mx]