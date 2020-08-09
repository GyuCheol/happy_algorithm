# https://programmers.co.kr/learn/courses/30/lessons/12987
# 숫자 게임 - lv3
# 정렬 응용

# 생각보다 넘 쉬웠던 문제
# 2개의 list를 내림차순 정렬해서, A요소는 어쩔 수 없으니,
# B요소로 더 커질 수 있는 짝만 찾아서 counting하면 된다. 
# o.o 우왕 점수 거져 먹었음.
# n 요소가 큰 문제는 자연스럽게 정렬 써야지 하는 습관이 생겼다.. ㅋㅋ..

def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    cnt = 0
    b = 0
    
    for a in A:
        if B[b] > a:
            cnt += 1
            b += 1
    
    return cnt