# 7월 24일

# 야근 지수
# https://programmers.co.kr/learn/courses/30/lessons/12927
# 연습문제 - lv3

# 힙을 이용한 문제?
# 최댓값을 계속 줄이기
# n이 백만이하이므로, 백만 * log2000 적절함
# 다만, input이 더 많아지고, n 값이 1억, 10억까지 간다면 최적화 필요함!

# O(NlogN)

import heapq

def solution(n, works):
    hq = [-w for w in works]

    heapq.heapify(hq)
    
    while n > 0 and hq:
        max_work = heapq.heappop(hq)

        n -= 1

        if (max_work + 1) < 0:
            heapq.heappush(hq, max_work + 1)

    answer = 0

    for w in hq:
        answer += w * w

    return answer

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
print(solution(1, [1]))
print(solution(5000, [40000]))
print(solution(3, [3, 2]))

works = [50000] * 20000

print(solution(1000000, works))