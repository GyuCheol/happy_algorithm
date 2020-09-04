# 개망..

def solution(n):
    dp = [0] * (n + 1)
    
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = (dp[i-1] * 2)

    return 36

print(solution(1)) # 1
print(solution(2)) # 2
print(solution(3)) # 5
print(solution(4)) # 14
print(solution(5)) # 
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(10))
print(solution(11))
print(solution(12))
print(solution(13))
print(solution(14))