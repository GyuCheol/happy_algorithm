# 7월 23일

# 줄서는 법
# https://programmers.co.kr/learn/courses/30/lessons/12936
# 연습문제 - lv3

# 팩토리얼 급으로 커지는 n의 크기로 정말 순열로 풀겠다고 하면
# 컴퓨터가 터질 것이다.
# k 값이 최대 2432902008176640000까지 올 수 있는데,,
# 다행히 64비트를 초과하지 않는다.
# 일단 k값을 토대로 ary의 몇번째 값이 몇번째에 오는지 유추해볼 수 있다. (사전 순이므로)

# 요소가 3개짜리라면, 가장 첫 요소가 가장 첫 자리에 있는 경우는 (k-1)!자리까지다 (즉 2가지)
# 그 다음 자리로는 당연히 (k-2)!자리까지가 순서상으로 올 수 있고
# 기준이 되는 k값을 감소해가며 총 n자리까지의 각 순서상 올 수 있는 값을 구하면 된다.

# O(N)

from math import factorial

def solution(n, k):
    ary = [x for x in range(1, n + 1)]
    answer = []

    k -= 1

    while n > 0:
        tmp = factorial(n-1)
        n -= 1

        answer.append(ary[k // tmp])

        ary.remove(ary[k // tmp])
        k -= (k // tmp) * tmp

    
    return answer

    
print(solution(3, 1))
print(solution(3, 2))
print(solution(3, 3))
print(solution(3, 4))
print(solution(3, 5))
print(solution(3, 6))

print(solution(10, 1))
