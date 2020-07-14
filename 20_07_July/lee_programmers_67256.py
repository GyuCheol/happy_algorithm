# 7월 14일

# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256
# 2020 카카오 인턴십 - lv1

# Greedy 유형? 아무튼 논리가 단순하지만,
# 일반적인 수학적 알고리즘 문제라기 보단
# 특정 논리를 만족하는 프로그램으로 보인다.

# 시간 복잡도 O(N)

# 0~9, *, #까지 좌표
location = {
    1: (0, 0),
    2: (1, 0),
    3: (2, 0),
    4: (0, 1),
    5: (1, 1),
    6: (2, 1),
    7: (0, 2),
    8: (1, 2),
    9: (2, 2),
    '*': (0, 3),
    0: (1, 3),
    '#': (2, 3)
}

def solution(numbers, hand):
    l_loc = location['*']
    r_loc = location['#']
    answer = []

    def get_distnace(loc1, loc2):
        return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

    for n in numbers:
        tmp = ''
        if n in {1, 4, 7}:
            # 무조건 왼손
            tmp = 'L'
        elif n in {3, 6, 9}:
            tmp = 'R'
        else:
            # 가까운 엄지손가락
            l_dist = get_distnace(l_loc, location[n])
            r_dist = get_distnace(r_loc, location[n])

            if l_dist == r_dist:
                # 손가락 거리가 같다면
                tmp = hand[0].upper()    
            else:
                tmp = 'L' if l_dist < r_dist else 'R'

        answer += tmp
        
        if tmp == 'L':
            l_loc = location[n]
        else:
            r_loc = location[n]

    return ''.join(answer)

# LRLLLRLLRRL
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
# LRLLRRLLLRR
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))