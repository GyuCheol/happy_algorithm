# 7월 10일

# 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885
# Greedy - lv2

# 가장 효율이 좋도록 구명보트에 사람을 태워야한다.
# 총 100kg limit에 50kg를 태웠다면 50kg에 가장 가깝도록 사람을 태워야 한다.
# 최대 2명만 탈 수가 있다!!! << 아니었다면 DP? 완전 탐색 문제 였을 수도?
# 로직은 정렬을 한다.
# 가장 왼쪽 값(최솟값)을 선택한다.
# 가장 마지막 값을 선택한다.
# 가능한가? 불가능하면 보트 +1

# 시간 복잡도 O(NlogN) (정렬과 deque 사용)

from collections import deque

def solution(people, limit):
    answer = 0
    
    sorted_people = deque(sorted(people))

    while sorted_people:
        # 구명 보트를 하나 띄움
        answer += 1
        smallest = sorted_people.popleft()

        # 남은 people이 있다면
        if sorted_people:
            biggest = sorted_people.pop()

            if (smallest + biggest) > limit:
                # limit보다 크다면, biggest는 혼자 떠나야함
                # 다시 짝을 구해야 하므로 smallest 다시 추가
                sorted_people.appendleft(smallest)
                
        
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([10, 20, 60, 80], 100))