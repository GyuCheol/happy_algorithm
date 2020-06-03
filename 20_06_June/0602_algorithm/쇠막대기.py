

def solution(arrangement):
    answer = 0
    stack = []

    for i, ch in enumerate(arrangement):
        
        if ch == '(':
            stack.append(i)
        else:
            # 닫는 괄호와의 짝이 되는 열린 괄호
            top = stack.pop()

            if top == (i - 1):
                # 레이저
                answer += len(stack)
            else:
                # 막대기 끝
                answer += 1

    return answer

print(solution('()(((()())(())()))(())'))
