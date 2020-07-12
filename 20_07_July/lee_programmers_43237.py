# 7월 11일

# 예산
# https://programmers.co.kr/learn/courses/30/lessons/43237
# 이분탐색 - lv3

# 정렬된 상태에서 시작한다. (특정 위치 이상의 모든 요소를 기준액 이상으로 처리가능)
# 최적의 상한액을 이분 탐색하여 최적의 상한액을 찾아낸다.
# 초기 상한 범위를 0~M으로 지정하고, 합계에 따라 상한액 범위를 줄여가며(이분탐색) 풀이하기

# 시간 복잡도 O(NlogN)

def solution(budgets, M):
    
    l = len(budgets)
    sorted_budgets = sorted(budgets)

    # 첫 상한액 범위를 0~M으로 지정
    limit = M
    recent_limit = M
    start = 0

    # 결과 값 비교 및 최적 결과 저장
    diff = M
    answer = limit
    
    while True:
        # print(limit) 디버깅용 limit 값이 2분 탐색으로 출력되는지 봐야했다.

        pos = -1
        # limit보다 큰 위치 찾기
        for i in range(l):
            if sorted_budgets[i] >= limit:
                pos = i
                break
        
        # 정렬되었으므로 pos까지의 더한 결과, pos 이후 위치부터 limit 곱하면
        # 상한가 반영된 예산 총액 계산
        if pos == -1:
            # pos를 찾지 못한 경우 limit 범위를 조정하고 재실행
            recent_limit = limit
            limit = (limit + start) // 2
            continue
        
        s = sum(sorted_budgets[:pos]) + (limit * (l - pos))
        
        if s <= M:
            # s가 M에 맞게 들어온 경우,
            # 이전 결과보다 최적이라면, 저장
            if diff > (M - s):
                diff = M - s
                answer = limit
            
            # 더 큰 상한선으로 가능한지 범위 넓히기
            start = limit
            limit = (limit + recent_limit) // 2

        else:
            # 결과가 크므로, 범위 좁히기
            recent_limit = limit
            limit = (limit + start) // 2

        # limit, start가 똑같으면 모두 탐색한 것.
        if limit == start:
            break

    return answer

print(solution([1, 3, 5, 7], 9))
# print(solution([1, 3, 3, 3], 10))
# print(solution([120, 110, 140, 150], 481))
# print(solution([150, 150, 150, 150], 600))
# print(solution([150, 150, 150, 150], 604))
