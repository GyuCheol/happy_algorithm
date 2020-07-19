# 7월 17일

# 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677
# 2018 카카오 블라인드 공채 1차 - lv2

# 문자열 처리, 분해 및 이산수학 처리(집합 연산)의 문제

# O(N)

from re import compile
from collections import Counter

# 영문자만
comp = compile('[^a-z]')

def solution(str1, str2):
    # 소문자 변환 및 특수문자 제거
    str1 = str1.lower()
    str2 = str2.lower()
    
    def get_divided_str(st):
        s = []

        for i in range(len(st) - 1):
            tmp = st[i:i+2]

            if len(comp.findall(tmp)) == 0:
                s.append(tmp)

        return s
    
    # 각 요소별 개수
    s1 = Counter(get_divided_str(str1))
    s2 = Counter(get_divided_str(str2))
    
    # 교집합 &의 개수 총합
    intersecion = sum([x for x in (s1 & s2).values()]) 

    # 합집합 |의 개수 총합
    union = sum([x for x in (s1 | s2).values()]) 

    return int(intersecion / union * 65536) if intersecion != union else 65536


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
