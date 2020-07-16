# 7월 16일

# 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973
# 2017 팁스타운 lv2
# stack? 

# 문자 하나하나 추가해가며 제거 가능하면 pop pop
# so simple

# 시간 복잡도 O(N)

def solution(s):
    stack = []

    for ch in s:

        if stack and ch == stack[len(stack) - 1]:
            stack.pop()
        else:
            stack.append(ch)

    return 0 if len(stack) > 0 else 1

print(solution('baabaa'))