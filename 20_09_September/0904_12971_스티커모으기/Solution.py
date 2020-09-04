def solution(sticker):

    if len(sticker) == 1:
        return sticker[0]

    dp1 = [0] * len(sticker)
    dp2 = [0] * len(sticker)

    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])

    dp2[1] = sticker[1]

    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(dp1[-2], dp2[-1])

print(solution([10]))
print(solution([10, 15]))
print(solution([15, 10]))
print(solution([4, 2, 2, 3]))

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))