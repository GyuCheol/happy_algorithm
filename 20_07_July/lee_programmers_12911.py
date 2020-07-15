# 7월 15일

# 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911
# lv2 연습문제 (수학?)

# 2진으로 개수 세는 것 (파이썬이므로 대충 bin함수와 count써도 되긴 된다..)
# 탐색하는 방법 (1씩 증가시키면서)

# 시간 복잡도 O(N) ?

def solution(n):
    
    tmp = n + 1
    bin_target = bin(n).count('1')

    while bin_target != bin(tmp).count('1'):
        tmp += 1

    return tmp

print(solution(78))