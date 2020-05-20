
def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        
        sec = 0

        for j in range(i + 1, len(prices)):
            sec += 1

            if prices[i] > prices[j]:
                break
        
        answer.append(sec)

    answer.append(0)

    return answer


print(solution([1, 2, 3, 4, 5]))
# 4 3 2 1 0

print(solution([3, 2, 1, 5, 4]))
# 1 1 2 1 0

print(solution([999, 998, 997, 996, 995]))
# 1 1 1 1 0



