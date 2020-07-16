# 7월 16일

# 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257
# 2020 카카오 인턴십 - lv2

# +, -, *의 순서를 조정하기 위해 permuation을 사용 (N!) 이긴하나, 최대 3개라 상수항으로 치자
# 숫자와, 연산자를 분리시키고
# 인자로 온 연산자 순서에 맞게 연산
# split은 정규 표현식으로 한다.

# 연산자와, 피연산자를 따로 보관하여
# 우선순위 연산자부터 피연산자를 가져와 연산한다.
# 조금 의아하지만, 대충 이렇게라도 풀어야했던...

# 시간 복잡도 O(N) 엄밀히 따지면 O(6*6*N)

import re
from itertools import permutations

def solution(expression):
    answer = 0
    # 연산자, 숫자 분할
    params = re.split('([-+*])', expression)
    
    # 피연산자들을 미리 int화 시킨다.
    for id in range(len(params)):
        if params[id] not in {'+', '-', '*'}:
            params[id] = int(params[id])

    def calculate(priority):
        clone = params[:]

        for prior in priority:
            id = 0

            while id < len(clone):
                
                if clone[id] == prior:
                    if clone[id] == '*':
                        clone[id-1:id+2] = [clone[id-1] * clone[id+1]]
                    elif clone[id] == '+':
                        clone[id-1:id+2] = [clone[id-1] + clone[id+1]]
                    else:
                        clone[id-1:id+2] = [clone[id-1] - clone[id+1]]
                else:
                    id += 1
                        
        return abs(clone[0])

    for p in permutations({k for k in params if k in {'+', '-', '*'}}):
        answer = max(answer, calculate(p))

    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))