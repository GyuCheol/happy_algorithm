# 7월 7일

# 카펫 - 완전탐색 (lv2)
# https://programmers.co.kr/learn/courses/30/lessons/42842

# 겉은 갈색이고, 그 이외 범위는 모두 노란색
# input에 맞는 가로, 세로를 가지는 사각형 리턴하기
# brown + yellow 합으로 사각형의 너비를 구하고
# 사각형의 너비가 나올 수 있는 가로, 세로 경우를 완전 탐색하여
# 해당 가로, 세로가 brown, yellow와 맞는지 비교한다.
# brown = (height * 2) + (2 * (width - 2))
# yellow = (height * width) - brown
# ※ 세로나 가로는 최소 3이다.

# 처음에는 시간 복잡도 O(N^2)로 높이, 너비를 모두 2부터 가능한 경우까지 모두 순회했는데
# yellow가 2백만까지 될 수 있어서 그러면 안되는 논리였다... 2백만 * 2백만???

# yellow를 구하는 경우를 쉽게 생각해보자.
# 실제 가로, 세로의 -2를 곱한 것이 yellow의 너비가 되겠다.
# yellow = (width - 2) * (height - 2)
# 즉 yellow의 너비만 구하면 되고, yellow를 소인수 분해하면 쉽게 해결 될 것이다.
# yellow의 소인수 분해한 결과를 토대로 brown이 제대로 구해졌는지만 확인하면 끝.
# 소인수 분해는 O(logN)의 시간 복잡도만에 가능하다.

# 시간 복잡도 O(logN)

def solution(brown, yellow):

    i = 1

    while (i * i) <= yellow:

        if yellow % i == 0:
            h = i
            w = yellow // i

            b = ((h+2) * 2) + (w * 2)

            if b == brown:
                return [w + 2, h + 2]

        i += 1
    
    return []

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
