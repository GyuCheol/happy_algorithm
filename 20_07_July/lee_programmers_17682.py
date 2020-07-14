# 7월 14일

# 다트게임
# https://programmers.co.kr/learn/courses/30/lessons/17682
# 2018 카카오 블라인드 코딩테스트 - lv1

# 정규식으로 쉽게 parsing 할 수 있다.

# 시간 복잡도 O(1) 다트는 무조건 3개 상수항 시간복잡도

from re import findall


def solution(dartResult):
    score = [0] * len(dartResult)

    find = findall(r'(\d{1,2})([SDT])([#*]?)', dartResult)
    bonus = {'S': 1, 'D': 2, 'T': 3}
    id = 0

    for n, area, star in find:
        n = int(n)
        
        score[id] = n ** bonus[area]

        if star == '#':
            score[id] *= -1
        elif star == '*':
            score[id] *= 2

            if id > 0:
                score[id-1] *= 2

        id += 1        

    return sum(score)

# expected 37
print(solution('1S2D*3T'))
# expected 9
print(solution('1D2S#10S'))

