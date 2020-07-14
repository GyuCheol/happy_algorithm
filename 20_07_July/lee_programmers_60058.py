# 7월 14일

# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058
# 2020 카카오 블라인드 채용 - lv2

# 문제에 제시된 논리를 그대로 구현할 수 있냐 없냐가 관건인 문제다.
# 작년엔 제대로 이해도 못했음..
# 다시 풀어보자

# 그냥 문제에서 요구하는 대로만 잘 풀어도된다.
# 딱히 생각을 복잡하게 할 필요가 없었다...!
# 허무하지만 1년 사이 실력이 올랐다는걸 알려준 문제

# 시간 복잡도 O(NlogN)
# 딱히 시간 복잡도가 중요한 문제는 아니고,
# 시간 복잡도를 분석하기가 조금 힘들다.
# 일단 문자열 분리가 일어나니 logN의 비용을 예상할 수 있고.
# 분리 속에서 또 분리가 일어나니 NlogN을 예상해본다.


def solution(p):

    # 올바른 괄호 문자열인지 판단
    def is_correct_bracket(s):
        i = 0

        for ch in s:
            if ch == '(':
                i += 1
            else:
                i -= 1

            if i < 0:
                return False
        
        return i == 0

    # 균형잡힌 문자열인지 판단
    def is_balanced_bracket(s):
        return s.count('(') == s.count(')')

    def task(s):
        if s == '':
            return ''

        u = ''
        v = ''

        # u, v 분리하기
        for i in range(2, len(s) + 1, 2):
            u = s[:i]
            v = s[i:]

            if is_balanced_bracket(u) and is_balanced_bracket(v):
                break

            
        # u가 올바른 괄호라면 v만 task 실행
        if is_correct_bracket(u):
            return u + task(v)
        else:
            new = ''

            for ch in u[1:-1]:
                new += '(' if ch == ')' else ')'

            return '(' + task(v) +  ')' + new

        
    return task(p)

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
