def solution(land, P, Q):
    # 2차원 > 1차원 변환
    flat = [x for sublist in land for x in sublist]
    left, right = min(flat), max(flat) + 1
    
    answer = 0x7fffffff

    def get_cost(n):
        add = 0
        remove = 0

        for x in flat:
            if x <= n:
                add += n - x
            else:
                remove += x - n

        return add, remove


    # 추가 블록이 크다 <<
    # 제거 블록이 크다 >> 로 로직 작성
    while True:

        mid = (left + right) // 2
        cost = get_cost(mid)

        if cost < answer:
            answer = cost
        
        

    return answer


# 5
print(solution([[1, 2], [2, 3]], 3, 2))

# 33
print(solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3))