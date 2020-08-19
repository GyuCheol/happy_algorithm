
def solution(stones, k):
    
    m = 0
    left = 0
    right = max(stones) + 1

    def can_cover(mid):
        cnt = k

        for i in range(len(stones)):

            if stones[i] < mid:
                cnt -= 1

                if cnt <= 0:
                    return False

            else:
                cnt = k
        
        return True

    while True:
        mid = (left + right) // 2

        # 모든 값을 다 탐색한 경우 종료 (경계 겹침)
        if left == mid or right == mid:
            break
                
        if can_cover(mid):
            # 가능하면 더 큰 값 시도
            left = mid
            m = max(m, mid)
        else:
            # 불가능 하면 범위 <<
            right = mid
        
    return m

# 답이 5가 되어야함.
print(solution([6, 5, 4, 3, 1, 6, 6, 6, 6, 6], 4))

# 답 6
print(solution([6, 6, 6, 6, 6, 6, 6, 6, 6, 6], 1))
print(solution([6, 6, 6, 6, 6, 6, 6, 6, 6, 12], 1))

# 답 12
print(solution([6, 6, 6, 6, 12, 6, 6, 6, 6, 12], 5))

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 10))
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 1))
print(solution([1, 1, 1, 1], 2))
print(solution([1, 1, 1], 2))
print(solution([1, 1, 1], 2))
print(solution([1, 1, 1, 1], 4))
print(solution([1, 1, 1, 1, 1, 1], 4))

tmp = [x for x in range(200000, 1, -1)]

# print(solution(tmp, 50000))

tmp2 = [x for x in range(1, 200000)]
# print(solution(tmp2, 50000))
