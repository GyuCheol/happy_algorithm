# 7월 13일

# GCD, LCM (최대 공약수, 최소 공배수)
# https://programmers.co.kr/learn/courses/30/lessons/12940
# lv 1

# gcd, lcm 복습겸
# gcd는 유클리드 호제법
# lcm은 두 수를 곱한 것에 gcd를 나눈 값이다.

# 시간 복잡도 O(logN)

def solution(n, m):
    
    def gcd(a, b):
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)
    
    g = gcd(n, m)
    
    return [g, (n * m) / g]