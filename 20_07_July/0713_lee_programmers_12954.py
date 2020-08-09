# 7월 13일

# x부터 시작 n개의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12954
# lv 1

# range 응용
# 함정으로 x가 0이 되면 range 함수 쓰기가 애매해짐.

# 시간 복잡도 O(n)

def solution(x, n):
    
    return [0 for x in range(n)] if x == 0 else list(range(x, x * (n + 1), x))