# 7월 23일

# 멀리 뛰기
# https://programmers.co.kr/learn/courses/30/lessons/12914
# 연습문제 - lv3

# dp 문제로 보임
# lv3 치고는 심플하게 생긴 dp문제다.
# 각 칸마다 +1, +2로 갈 수 있으니 n까지 이동하며
# 현재 칸에서 -1, -2에서 왔다는 경우의 수를 누적하며 n까지 진행
# 거의 피보나치급 문제?

# O(N)


def solution(n):
    d = [0] * (n + 3)

    d[0] = 1
    
    for i in range(0, n + 1):
        d[i + 1] = (d[i + 1] + d[i]) % 1234567
        d[i + 2] = (d[i + 2] + d[i]) % 1234567

    return d[n]

print(solution(5))
print(solution(4))
print(solution(3))
