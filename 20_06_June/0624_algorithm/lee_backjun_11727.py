
# 2 x n 타일링2
# https://www.acmicpc.net/problem/11727
# Dynamic Programming

# 이전 문제에서 2*2 타일이 추가됨
# 2*2의 타일로 d[n-2]의 경우의 수와 같으므로
# d[n] = d[n-1] + d[n-2] + d[n-2]가 될 수 있다.
# 단, 여기서 d[2]의 초기 값은 3이어야 함

n = int(input())
d = [0] * (n + 1)

d[1] = 1

if n >= 2:
    d[2] = 3

for i in range(3, n + 1):
    d[i] = (d[i-1] + d[i-2] + d[i-2]) % 10007

print(d[n])