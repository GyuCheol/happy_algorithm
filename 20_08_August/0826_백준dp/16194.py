n = int(input())
price = [0] + list(map(int, input().split(' ')))

dp = price[:]

for i in range(2, n + 1):
    for j in range(1, i):
        dp[i] = min(dp[i], dp[i-j] + price[j])


print(dp[n])
