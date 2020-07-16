# 7월 16일

# n개의 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12953
# lv 2 - 연습문제

# 각 n을 진행하며 최대공약수와 최소 공배수를 구해나가면 된다.

# 시간 복잡도 O(NlogN) logN 공약수 구하기 * N개만큼


def solution(arr):

    def gcd(a, b):
        
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)
    
    tmp = arr[0]

    for n in arr[1:]:
        tmp = (tmp * n) // gcd(tmp, n)

    return tmp

print(solution([2, 6, 8, 14]))
