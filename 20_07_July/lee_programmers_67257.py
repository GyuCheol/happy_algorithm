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

# 시간 복잡도 O(N)

import re
from itertools import permutations

def solution(expression):
    answer = 0
    # 연산자, 숫자 분할
    params = re.split('([-+*])', expression)
    
    def calculate(priority):
        operators = []
        numbers = []

        for param in params:
            if param in {'+', '-', '*'}:
                operators.append(param)
            else:
                numbers.append(int(param))
        
        for prior in priority:

            id = 0

            while id < len(operators):
                op = operators[id]

                if op == prior:
                    operand = numbers[id:id+2]
                    operators.remove(op)

                    if op == '*':
                        numbers[id:id+2] = [operand[0] * operand[1]]
                    elif op == '+':
                        numbers[id:id+2] = [operand[0] + operand[1]]
                    else:
                        numbers[id:id+2] = [operand[0] - operand[1]]
                else:
                    id += 1
                        

        
        return abs(numbers[0])


    for p in permutations({k for k in params if k in {'+', '-', '*'}}):
        answer = max(answer, calculate(p))

    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))