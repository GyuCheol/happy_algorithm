
# 오등큰수
# https://www.acmicpc.net/problem/17299
# 이전 문제, 오큰수에서 각 숫자의 반복 횟수를 이용하여 풀이 (hash)

from collections import Counter

n = int(input())
numbers = list(map(int, input().split(' ')))

# 각 숫자별 등장 횟수 dict
count = Counter(numbers)

stack = []
result = [0] * n

for i, number in enumerate(numbers):

    while stack:
        top = stack.pop()
        
        if count[number] > count[numbers[top]]:
            result[top] = number
        else:
            stack.append(top)
            break

    stack.append(i)

# 남은 값 -1
while stack:
    top = stack.pop()

    result[top] = -1

for n in result:
    print(n, end=' ')
