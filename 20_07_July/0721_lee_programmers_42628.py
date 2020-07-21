# 7월 21일

# 이중 우선 순위 큐
# https://programmers.co.kr/learn/courses/30/lessons/42628
# Heap - lv3

# 2개의 heap을 만든다. (최소큐, 최대큐)
# 명령어에 따라 최소큐와 최대 큐에 해당 값을 제거
# 모든 것이 제거되었다면 [0, 0]을 반환
# 힙을 2개 쓴다면 매우 쉽게 해결되는 문제이다.
# 직관의 중요성

# O(NlogN) - heap을 사용함

import heapq

def solution(operations):
    max_hq = []
    min_hq = []
    cnt = 0
    removed_cnt =0

    for operation in operations:
        cmd, num = operation.split(' ')

        if cmd == 'I':
            heapq.heappush(max_hq, -int(num))
            heapq.heappush(min_hq, int(num))
            cnt += 1
        elif removed_cnt < cnt:
            removed_cnt += 1

            if num == '-1':
                # 최솟값 제거
                max_hq.remove(-heapq.heappop(min_hq))
            else:
                # 최댓값 제거
                min_hq.remove(-heapq.heappop(max_hq))


    return [-heapq.heappop(max_hq), heapq.heappop(min_hq)] if cnt != removed_cnt else [0, 0]


print(solution(['I 16','D 1']))
print(solution(	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(	["I 16"]))
print(solution(	["I 16", 'D 1', 'D 1']))
print(solution(	['I 4', 'I 3', 'I 2', 'I 1', 'D 1', 'D 1', 'D -1', 'D -1', 'I 5', 'I 6']))
