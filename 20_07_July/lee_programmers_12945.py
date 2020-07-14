# 7월 14일

# 피보나치
# https://programmers.co.kr/learn/courses/30/lessons/12945
# DP - lv2

# bottom-up 방식으로 풀이

# 시간 복잡도 O(logN)

def solution(n):
    d = [0] * (n+ 1)
    
    d[0], d[1] = 0, 1
    
    for i in range(2, n + 1):
        d[i] = (d[i-1] + d[i-2]) % 1234567
    
    return d[n]
