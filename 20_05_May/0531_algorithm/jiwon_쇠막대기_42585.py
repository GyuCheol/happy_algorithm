# https://programmers.co.kr/learn/courses/30/lessons/42585
# 위치에 따라 막대 개수가 달라지는데 처리방법
def solution(arrangement):
    answer = 0
    stack = []

    for i, ch in enumerate(arrangement): 
        # 인덱스,문자 쌍으로 출력
        
        if ch == '(':
            stack.append(i)

        else: # ')'
            top = stack.pop()

            if top == (i-1):
                # 레이저
                answer += len(stack)
            else:
                # 막대기 끝
                answer += 1
    
    return answer

print(solution('()(((()())(())()))(())'))