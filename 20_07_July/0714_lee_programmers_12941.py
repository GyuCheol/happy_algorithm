# 7월 14일

# 최솟값 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12941
# lv 2

# 오름차순, 내림차순 zip에서 곱하고 더한 결과 so simple

# 시간 복잡도 O(NlogN)

def solution(A,B):

    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])