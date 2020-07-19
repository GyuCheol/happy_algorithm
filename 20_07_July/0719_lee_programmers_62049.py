# 7월 19일

# 종이접기
# https://programmers.co.kr/learn/courses/30/lessons/62049
# Summer/Winnter Coding 2019 - lv3
# DP 문제의 느낌

# 접히고 펼쳐질 때마다 중앙에 [0]이 붙고
# 기존 배열의 0과 1을 반전한 값을 reverse해서 붙이면 된다.
# 풀기위해 종이 한장을 겁나 접고 피면서 규칙성을 알아냈다..

# O(2^n) 배열이 복제되고 뒤집는 행위 포함해서 대략?


def solution(n):
    d = [0]
    
    for i in range(n - 1):
        # 기존 d의 0과 1을 반전함
        # xor 1을 하면 0 1을 뒤집을 수 있음.
        tmp = [x ^ 1 for x in d[::-1]]
        d += [0]
        d += tmp

    return d

print(solution(1))
print(solution(2))
print(solution(3))

# [0]
# [0, 0, 1]
# [0, 0, 1, 0, 0, 1, 1]
# [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
print(solution(4))
print(solution(5))