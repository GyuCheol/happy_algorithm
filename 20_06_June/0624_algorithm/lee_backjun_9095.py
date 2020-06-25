
# 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095
# Dynamic Programming

# 점화식 : d[n] = d[n-1] + d[n-2] + d[n-3]
# d[n]을 만들 수 있는 방법은, d[n]을 만드는 방법은
# d[n-1]에서 +1을 더하는 방법, d[n-2]의 경우에서 +2를 하는 방법, d[n-3] 경우에서 +3을 하는 방법 등
# 이전 작은 문제에서 새로운 1, 2, 3을 더하면 되는 것이기에 이런 점화식이 성립한다.
# d[1], d[2], d[3]에서 시작하여 n까지 n-1, n-2, n-3 합산하며 진행하면 된다.

n = int(input())

d = [0] * (12)

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 11):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for i in range(n):
    print(d[int(input())])