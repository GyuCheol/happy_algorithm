# 6월 16일

# GCD 합
# https://www.acmicpc.net/problem/9613
# 주어진 요소 모든 쌍의 최대 공약수 구한 합
# 유클리드 호제법을 이용하여 최대 공약수 시간 복잡도를 O(logN)으로 만들고, 2중 루프로 해결

n = int(input())

def gcd(a, b):

    while a % b != 0:
        a, b = b, a % b

    return b

for i in range(n):
    ary = list(map(int, input().split(' ')))[1:]
    l = len(ary)

    total = 0
    for x in range(l):
        for y in range(x + 1, l):
            total += gcd(ary[x], ary[y])

    print(total)



