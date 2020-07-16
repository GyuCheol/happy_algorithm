# 7월 16일

# 라면 공장
# https://programmers.co.kr/learn/courses/30/lessons/42629
# Heap - lv2

# python heapq를 최대 힙으로 이용하려면
# 튜플을 이용하여 음수 값으로 정렬될 수 있도록 하여야 원본 값이
# 내림차순으로 보관이 가능하다.

# 여기서 생각해야될 전제는 stock이 소진되기 전까지 성급하게 
# 공급을 받을 필요가 없다는 것.
# stock이 소진될 타이밍에 밀가루를 공급 받으면 되지만,
# 언제 받으나 k일까지의 일정에서는 똑같으니
# 현재 받을 수 있는 공급 중 가장 큰 값을 항상 취하면 된다.

# 시간 복잡도 O(NlogN) 최악 dates 길이만큼 logN 연산을 2번할 수 있다 (heap push, heah pop)

from heapq import heappop, heappush

def solution(stock, dates, supplies, k):
    answer = 0
    h = []
    idx = 0
    
    # stock이 k에 도달하면 충분한 밀가루를 확보한 것
    while stock < k:
        
        # 현재 stock에서 추가가능한 supply heap에 추가
        for i in range(idx, len(dates)):
            if dates[i] <= stock:
                heappush(h, (-supplies[i], supplies[i]))
                idx += 1
            else:
                break
            
        # 현재까지 공급 가능한 밀가루 중 가장 큰 밀가루량 추가
        stock += heappop(h)[1]
        answer += 1

    return answer

print(solution(4, [4, 10, 15], [20, 5, 10], 30))