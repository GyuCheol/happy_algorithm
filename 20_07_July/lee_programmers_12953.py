# 7월 16일

# n개의 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12953
# lv 2 - 연습문제

# 각 n을 진행하며 최대공약수와 최소 공배수를 구해나가면 된다.
# reduce 함수를 요긴하게 쓸 좋은 문제였음.

# 시간 복잡도 O(NlogN) logN 공약수 구하기 * N개만큼

from functools import reduce

def solution(arr):

    def gcd(a, b):
        
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)

    return reduce(lambda a, b: a * b // gcd(a, b), arr)

print(solution([2, 6, 8, 14]))
