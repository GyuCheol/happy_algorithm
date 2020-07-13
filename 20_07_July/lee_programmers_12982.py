# 7월 13일

# 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982
# Summer/Winter Coding (2018) lv 1

# 정렬 후 얼마만큼 살 수 있는지 확인

# 시간 복잡도 O(NlogN)

def solution(d, budget):
    
    sorted_prices = sorted(d)
    tmp = 0

    for c, price in enumerate(sorted_prices):

        tmp += price

        if tmp > budget:
            return c
    
    # 모두 살 수 있다.
    return len(d)
        