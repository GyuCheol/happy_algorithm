# 7월 17일

# 예산 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985
# 2017 팁스타운 - lv2

# 시간 복잡도 O(logN) 2씩 계속 나누어 답에 근접하므로.

def solution(n,a,b):
    answer = 1
    a, b = min(a, b), max(a, b)
    a -= 1
    b -= 1

    # a가 항상 왼쪽, b가 오른쪽이면
    # a는 항상 짝수여야 b와 붙을 수 있다.
    while a + 1 != b or a % 2 != 0:
        answer += 1
        a //= 2
        b //= 2

    return answer

print(solution(8, 4, 7))
print(solution(8, 1, 2))
print(solution(8, 2, 3))