
# 쇠막대기
# stack 구조로 알고리즘 작성
# https://programmers.co.kr/learn/courses/30/lessons/42585

def solution(arrangement):
    answer = 0
    stack = []

    for i, ch in enumerate(arrangement):
        
        if ch == '(':
            # 막대기/레이저를 스택에 쌓음
            stack.append(i)
        else:
            top = stack.pop()

            if top == (i - 1):
                # 레이저인 경우 현재 스택에 쌓인 막대기만큼 쇳조각
                answer += len(stack)
            else:
                # 막대기가 끊어진 경우, 해당 막대기의 마지막 조각
                answer += 1

    return answer

# stack 자료구조 없이 풀이 (현재 쌓인 막대기 개수만 알면되므로)
def solution2(arrangement):
    answer = 0
    cnt = 0
    last_ch = ''

    for i, ch in enumerate(arrangement):
        
        
        if ch == '(':
            # 막대기/레이저를 스택에 쌓음
            cnt += 1
        else:
            
            cnt -= 1

            if last_ch == '(':
                # 레이저인 경우 현재 개수만큼 쇳조각 획득
                answer += cnt
            else:
                # 막대기가 끊어진 경우, 해당 막대기의 마지막 조각
                answer += 1

        last_ch = ch

    return answer

print(solution2('()(((()())(())()))(())'))