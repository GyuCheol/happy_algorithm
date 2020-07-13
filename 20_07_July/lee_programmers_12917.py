# 7월 13일

# 문자열 내림차순
# https://programmers.co.kr/learn/courses/30/lessons/12917

# 쉬운 문제지만, comprehension 연습용

# 시간 복잡도 O(N)

def solution(s):
    return ''.join(sorted(s, key=lambda a: -ord(a)))



print(solution('abcd'))
print(solution('1245acasdbgd'))
print(solution('Zbcdefg'))
