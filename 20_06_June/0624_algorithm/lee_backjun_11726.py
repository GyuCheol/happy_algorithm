
# 2 x n 타일링
# https://www.acmicpc.net/problem/11726
# Dynamic Programming

# 세로가 2이고 가로가 n으로 입력될 때 (n >= 1)
# 배치 가능한 2x1 타일의 개수 출력하기 (10,007로 나눈 나머지)
# n에 따라 경우의 수가 어떻게 나오는지 나열해보기
# n = 1, d[n] = 1
# n = 2, d[n] = 2
# n = 3, d[n] = 3
# n = 4, d[n] = 5
# ... 피보나치 수열과 비슷한 점화식 정의
# d[n] = d[n - 1] + d[n - 2]
# 이전 결과를 이용한 bottom-up 풀이
# 단, d[1]은 1, d[2]는 2

n = int(input())
d = [0] * (n + 1)

d[1] = 1

if n >= 2:
    d[2] = 2

for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2]) % 10007

print(d[n])