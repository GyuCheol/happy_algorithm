# 7월 4일

# n으로 표현
# https://programmers.co.kr/learn/courses/30/lessons/42895
# 다이나믹 프로그래밍 (lv3)

# @.@.@.@.@ 어렵다
# 아주 작은 문제에서 부터 사칙연산 모든 경우로 building 했더니 일단은 clear...
# @.@ 

# 점화식
# d[number] = min(d[number - 1] + d[1], d[number + i] + d[i], d[number - i] + d[i], d[number // i] + d[i], d[number * i] + d[i])
# i는 N, NN, NNN, NNNN, NNNNN의 경우
# 초기값은 d[1], d[N], d[NN], d[NNN], d[NNNN], d[NNNNN]이 정해질 수 있다. (나머진 이 작은 문제들로 도출해야 함)

def solution(N, number):
    # 최대 100000까지
    d = [9999] * 100000
    
    # d[1]은 2개로 도달 가능하다. N/N = 1
    # 단, N이 1인 경우 1번으로 가능하나, 아래 식에서 처리됨
    d[1] = 2

    # d[N] = 1, d[NN] = 2, d[NNN] = 3... 으로 채워준다.
    n_digits = []
    t = N
    for i in range(5):
        n_digits.append(t)
        d[t] = i + 1
        t *= 10
        t += N

    for i in range(1, len(d)):
        
        if d[i] == 0:
            d[i] = d[i-1] + d[1]

        for n in n_digits:
            if (i * n) < 100000:
                d[i * n] = min(d[i * n], d[i] + d[n])
            
            if (i + n) < 100000:
                d[i + n] = min(d[i + n], d[i] + d[n])

            if (i // n) > 1:
                d[i // n] = min(d[i // n], d[i] + d[n])

            if (n // i) > 1:
                d[n // i] = min(d[n // i], d[i] + d[n])
            
            if (i - n) > 1:
                d[i - n] = min(d[i - n], d[i] + d[n])

            if (n - i) > 1:
                d[n - i] = min(d[n - i], d[i] + d[n])
            

    if d[number] > 8:
        return -1

    return d[number]

print(solution(5, 56))