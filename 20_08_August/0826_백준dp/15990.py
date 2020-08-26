
n = int(input())
n_list = [int(input()) for _ in range(n)]

dp = [[0, 0, 0, 0] for _ in range(max(n_list) + 1)]

dp[1][1] = 1 # 1
dp[2][2] = 1 # 2
dp[3][1] = 1 # 2 + 1
dp[3][2] = 1 # 1 + 2
dp[3][3] = 1 # 3

for i in range(4, max(n_list) + 1):
    dp[i][1] = dp[i-1][2] + dp[i-1][3]
    dp[i][2] = dp[i-2][1] + dp[i-2][3]
    dp[i][3] = dp[i-3][1] + dp[i-3][2]

    dp[i][1] %= 1000000009
    dp[i][2] %= 1000000009
    dp[i][3] %= 1000000009

for i in n_list:
    print(sum(dp[i]) % 1000000009)