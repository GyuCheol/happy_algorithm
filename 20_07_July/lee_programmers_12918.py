# 7월 12일

# 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918
# lv 1

# 쉬운 문제인데, 정규식 써보려고.

# 시간 복잡도 O(N)

import re

comp = re.compile(r'[^\d]')

def solution(s):
    return len(s) in (4, 6) and len(comp.findall(s)) == 0

print(solution('asdasd'))
print(solution('1234'))
print(solution('123asd'))


