# 6월 21일

# 1로 만들기
# https://www.acmicpc.net/problem/1463
# Dynamic Programming

# 각 수를 만드는 최소의 경우의 수는 아래 점화식
# d[n] = min(d[n / 3], d[n / 2], d[n - 1]) + 1
# n/3에서 올 수 있거나, d/2에서 올 수 있거나, d - 1에서 올 수 있기 때문이다.
# 2에서 n까지 순회하며 체크하면 가장 빠른 최소 횟수로 온 것이기 때문에 가능한 논리

# bottom-up 방식으로 1에서부터 n까지 계산 결과를 통해 d[n]의 최소 회수를 구한다.

n = int(input())

d = [0] * (n + 1)

for i in range(2, n + 1):
    
    tmp = []

    if i % 3 == 0:
        tmp.append(d[i // 3])

    if i % 2 == 0:
        tmp.append(d[i // 2])
    
    tmp.append(d[i - 1])

    d[i] = min(tmp) + 1

print(d[n])
