# 7월 13일

# 문자열 마음대로 정렬
# https://programmers.co.kr/learn/courses/30/lessons/12915
# lv 1

# sort 함수의 비교 함수를 주입해서 풀면된다.
# 함정은 똑같은 경우에 사전 순으로 앞선 문자열이 앞에 온다는 것.
# tuple을 쓴 key를 반환해서 해결

# 시간 복잡도 O(NlogN) (정렬 알고리즘이므로)

def solution(strings, n):

    return sorted(strings, key=lambda s: (s[n], s))