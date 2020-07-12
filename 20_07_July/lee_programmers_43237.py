# 7월 12일

# 예산
# https://programmers.co.kr/learn/courses/30/lessons/43237
# 이분탐색 - lv3

# 정렬된 상태에서 시작한다. (특정 위치 이상의 모든 요소를 기준액 이상으로 처리가능)
# 최적의 상한액을 이분 탐색하여 최적의 상한액을 찾아낸다.
# 초기 상한 범위를 0~M으로 지정하고, 합계에 따라 상한액 범위를 줄여가며(이분탐색) 풀이하기

# 시간 복잡도 O(NlogN)

def solution(budgets, M):
    sorted_budgets = sorted(budgets)

    # 첫 상한액 범위를 0~가장 큰 값 + 1로 지정 (내림 발생 때문에 +1)
    end = sorted_budgets[-1] + 1
    begin = 0

    # 결과 값 비교 및 최적 결과 저장
    diff = M
    answer = 0
    
    while True:

        # 현재 범위에서 2분 탐색 값
        tmp = (end + begin) // 2

        # tmp 값이 2분 탐색으로 출력되는지 디버깅용.
        # print(tmp)

        # 합계 구하기
        s = sum([x if x < tmp else tmp for x in sorted_budgets])
        
        if s <= M:
            # s가 M에 맞게 들어온 경우,
            # 이전 결과보다 최적이라면, 저장
            if diff > (M - s):
                diff = M - s
                answer = tmp
            
            # 같으면 모두 탐색한 것
            if begin == tmp:
                break

            # 더 큰 상한선으로 가능한지 범위 넓히기
            begin = tmp

        else:
            # 결과가 크므로, 범위 좁히기
            end = tmp


    return answer

print(solution([1, 3, 5, 7], 9)) # 2
print(solution([1, 3, 3, 3], 10)) # 3
print(solution([120, 110, 140, 150], 485)) # 127
print(solution([120, 110, 140, 150], 481)) # 125
print(solution([150, 150, 150, 150], 600)) # 150
print(solution([150, 150, 150, 150], 604)) # 150
