import sys

sys.setrecursionlimit(50000)

dp = [0] * 1000001

# 10만번의 stack call이 예상됨.. overflow
def go(n):
    if n == 1:
        return 0
    
    if dp[n] > 0:
        return dp[n]

    dp[n] = go(n-1) + 1
    
    if n % 2 == 0:
        tmp = go(n//2) + 1

        dp[n] = min(dp[n], tmp)
    
    if n % 3 == 0:
        tmp = go(n//3) + 1

        dp[n] = min(dp[n], tmp)
    
    return dp[n]

def bottom(n):
    for i in range(2, n + 1):
        dp[i] = dp[i-1]

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3])

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2])
    
    dp[i] += 1

    return dp[n]

n = int(input())


print(go(n))
