# 7월 5일

# 기능개발 - 스택/큐 (lv2)
# https://programmers.co.kr/learn/courses/30/lessons/42586

# 순차적으로 기능 개발이 완료되어야 한다 (큐)
# input을 완료되는 날짜로 변환한다 우선은.
# 그리고 큐로 인출해가며 answer를 만든다.

# 시간 복잡도 O(N)

from math import ceil

def solution(progresses, speeds):
    answer = []

    # ceil 올림 함수
    # 올림을 통해 1.5일을 2일로 취급해야함
    completed_dates = [ceil((100-p)/s) for p, s in zip(progresses, speeds)]

    id = 0
    cnt = 0

    for i, comp in enumerate(completed_dates):
        
        if comp <= completed_dates[id]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            id = i
    
    answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([0, 0, 0], [1, 1, 1]))
print(solution([95], [4]))
