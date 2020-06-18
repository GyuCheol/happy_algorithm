
# 괄호
# https://www.acmicpc.net/problem/9012
# stack의 특성으로 괄호 짝을 맞추어 짝이 맞는지 아닌지 처리

def is_corrected(s):

    stack = []

    for ch in s:
        
        if ch == '(':
            stack.append(ch)
        elif len(stack) == 0:
            # 여는 괄호 없이, 닫는 괄호 나온 경우
            return False
        else:
            # 여는 괄호 짝을 맞추어 스택에서 제거
            stack.pop()
    
    # 여는 괄호가 남아있지 않아야 정확함
    return len(stack) == 0



n = int(input())

for _ in range(n):
    s = input()

    if is_corrected(s):
        print('YES')
    else:
        print('NO')


