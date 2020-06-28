
# 타일 장식물
# https://programmers.co.kr/learn/courses/30/lessons/43104?language=python3
# 다이나믹 프로그래밍

# 피보나치 수열을 이용한 풀이가 가능한 문제이다.
# N까지의 타일을 나열한 후 만들어지는 사각형의 둘레를 구하는 문제
# 둘레 값은 d[N] * 2 + (d[N] + d[N-1]) * 2로 구할 수 있다.

# 5분만에 풀어서 소름 DP 학습의 효과

def solution(N):
    d = [0] + [0] * N

    d[1] = d[2] = 1

    for i in range(3, N + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[N] * 2 + (d[N] + d[N - 1]) * 2

print(solution(5))
print(solution(6))
