from collections import deque

# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587
# Queue 처리 문제

def solution(priorities, location):
    answer = 0
    # location 매핑을 위해 각각 id로 묶어 만듦
    queue = deque(zip(range(len(priorities)), priorities))

    while True:
        
        # 첫번째 아이템
        front = queue.popleft()

        flag = False
        # 더 큰 요소 찾기
        for i in queue:
            if i[1] > front[1]:
                flag = True
                break
        
        # 더 큰 요소가 있는 경우 queue의 제일 뒤로
        if flag:
            queue.append(front)
        else:
            # answer번째로 출력
            answer += 1

            if front[0] == location:
                return answer

print(solution([2, 1, 3, 2], 0))