def solution(money):
    
    # 첫 집을 훔치는 경우
    dp = [0] * len(money)
    dp[:2] = money[0], max(money[0], money[1])

    # 첫 집은 안 훔치는 경우
    dp2 = [0] * len(money)
    dp2[:2] = 0, money[1]

    # 첫 집을 훔치는 경우
    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])


    return max(dp[len(money) - 2], dp2[len(money) - 1])

print(solution([10, 2, 2, 100, 2]))

# 3
print(solution([2, 1, 2]))

# 8
print(solution([1, 2, 3, 4, 5]))

# 7
print(solution([2, 1, 3, 5, 4]))

# 4
print(solution([1, 2, 3, 1]))

# 6
print(solution([1, 2, 3, 4]))

# 8
print(solution([1, 2, 3, 4, 5]))

# 8
print(solution([5, 3, 3, 2, 4]))

# 15
print(solution([5, 4, 7, 9, 8]))

# 14
print(solution([1, 9, 4, 2, 5]))
