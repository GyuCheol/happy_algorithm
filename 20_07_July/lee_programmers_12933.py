# 7월 13일

# 정수 내림차순 배치
# https://programmers.co.kr/learn/courses/30/lessons/12933
# lv 1

# 숫자를 배열로 나누고, 정렬해서 다시 숫자로 만드는 과정.
# 난이도는 쉽지만, pythoic한 1줄 코딩 해보고자 도전

# 시간 복잡도 O(NlogN) (정렬 알고리즘이 포함되므로)

def solution(n):
    
    return int(''.join(sorted(str(n), reverse=True)))