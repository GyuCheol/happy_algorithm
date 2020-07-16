# 7월 16일

# JadenCase 문자열 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12951
# lv 2
# 시간 복잡도 O(n)

# 일반적인 로직 문제

def solution(s):
    tmp = []
    id = 0
    
    for ch in s:
        if ch == ' ':
            id = 0
            tmp.append(ch)
        else:
            tmp.append(ch.upper() if id == 0 else ch.lower())
            id += 1
        
    
    return ''.join(tmp)