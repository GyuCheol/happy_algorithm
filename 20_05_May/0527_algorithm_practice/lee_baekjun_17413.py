
# Stack 응용 문제 : 단어 뒤집기
# Stack 성질 : 순서대로 넣은 것을 스택으로 빼내면 순서가 뒤집어짐.
# https://www.acmicpc.net/problem/17413

s = input()

stack = []

inner_tag = False

# 태그 속 내용은 뒤집지 않음.
# 이외 내용의 단어는 모두 뒤집기

def print_reverse(stack):

    while len(stack) > 0:
        print(stack.pop(), end='')

for ch in s:
    
    if ch == '<': # 태그의 시작
        # 태그 이전 문자열을 출력해야함. (뒤집어서)
        print_reverse(stack)
        inner_tag = True
        print(ch, end='')
    elif ch == '>': # 태그의 끝
        inner_tag = False
        print(ch, end='')
    elif inner_tag == True: # 태그안의 단어는 모두 그대로 출력
        print(ch, end='')
    else:
        # 뒤집어야하는 text 구간
        if ch == ' ': # 공백이라면, 뒤집어서 출력
            print_reverse(stack)
            print(' ', end='')
        else:
            stack.append(ch)
        
# 남은 스택 모두 출력
print_reverse(stack)
        
    

