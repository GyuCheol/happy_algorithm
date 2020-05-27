
# Stack 응용 문제 : 쇠막대기
# stack 구조로 막대기 상태를 처리 (자료구조는 굳이 안써도)
# https://www.acmicpc.net/problem/10799

s = input()
answer = 0
stack = 0
prev = ''

for ch in s:

    if ch == '(':
        # 막대기 stack up
        stack += 1
        
    else:
        # 막대기 stack down
        stack -= 1

        if prev == '(': 
            # 레이저인 경우, 쌓인 막대기만큼 조각 획득
            answer += stack
        else:
            # 막대기의 끝인 경우는 단 1조각만 획득
            answer += 1
    
    prev = ch


print(answer)
