# 7월 15일

# 하노이의 탑
# https://programmers.co.kr/learn/courses/30/lessons/12946
# lv3 연습문제 (재귀호출)

# 재귀호출의 기본이자 시작인 하노이탑 문제
# 여기서 하노이탑 호출 순서를 list로 반환해야하는 것을 추가했다.
# wrapped function을 이용해서 안전하게 처리가능하다.

# 시간 복잡도 O(2^N)

def solution(n):
    answer = []

    def move(i, s, d, t):
        if i == 1:
            answer.append([s, d])
            return
        
        move(i-1, s, t, d)
        answer.append([s, d])
        move(i-1, t, d, s)
        

    move(n, 1, 3, 2)

    return answer


print(solution(2))