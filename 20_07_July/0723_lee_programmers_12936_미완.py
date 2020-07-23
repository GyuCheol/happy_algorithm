# 7월 23일

# 줄서는 법
# https://programmers.co.kr/learn/courses/30/lessons/12936
# 연습문제 - lv3

# 팩토리얼 급으로 커지는 n의 크기로 정말 순열로 풀겠다고 하면
# 컴퓨터가 터질 것이다.
# k 값이 최대 2432902008176640000까지 올 수 있는데,,
# 다행히 64비트를 초과하지 않는다.
# 일단 k값을 토대로 ary의 몇번째 값이 몇번째에 오는지 유추해볼 수 있다. (사전 순이므로)

# 요소가 3개짜리라면, 가장 첫 요소가 먼저 오려면은 적어도 (k-1)!번째 까지는 되어야 한다.
# 그 다음 (k-1)번째부터 2번째 요소가 가장 첫자리에 위치할 것이다.
# 이를 이용해 (k-1)!나누고, (k-2)! 나누어.. 0이 될 때까지 반복하여 해당 번째 자리 값을 구하면 될 것이다.
# 확실히 lv3급 훼이크가 있는 문제지만, 코드는 짧다.

# O(N)

from math import factorial

def solution(n, k):
    ary = [x for x in range(1, n + 1)]
    answer = []


    while n > 0:
        tmp = factorial(n-1)
        n -= 1

        answer.append(ary[k // tmp])

        k //= tmp

        

    
    return answer

    

print(solution(3, 5))
