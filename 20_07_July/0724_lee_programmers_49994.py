# 7월 24일

# 방문 길이
# https://programmers.co.kr/learn/courses/30/lessons/49994
# Summer Winner Coding (2018) - lv3

# 시작 위치를 그 중앙인 5, 5에서 시작해서 명령어에 따라
# 움직인 길을 표시하고, 표시된 길의 개수를 세는 것
# 여기서 함정은 각 좌표가 일반적인 좌표평면으로 보면 안된다.
# 점과 점 사이의 간선을 지나갔는지를 보는 문제이다.
# 점과 점 사이의 간선은 가로 선이 10 * 11개가 있고
# 세로 선이 11 * 10개가 있다.
# U, D으로 지나갈 땐 세로 선이며 L, R로 지나갈 땐 가로 선으로 지나간다.

# L, R, U, D에 따라 해당 값을 기록하여 처리
# 첨에 경계 조정을 잘못해서 에러가 났다.. 0~20...

# O(N)


def solution(dirs):
    x = 5
    y = 5
    horizontal_lines = [[0 for x in range(10)] for y in range(11)]
    vertical_lines = [[0 for x in range(11)] for y in range(10)]

    direction = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, -1),
        'D': (0, 1)
    }
    
    for d in dirs:
        nx = x + direction[d][0]
        ny = y + direction[d][1]

        if 0 <= nx <= 10 and 0 <= ny <= 10:
            if d == 'L':
                horizontal_lines[y][nx] = 1
            elif d == 'R':
                horizontal_lines[y][x] = 1
            elif d == 'U':
                vertical_lines[ny][x] = 1
            elif d == 'D':
                vertical_lines[y][x] = 1

            x, y = nx, ny

    return sum([h.count(1) for h in horizontal_lines]) + sum([v.count(1) for v in vertical_lines])

print(solution('UUUUUUUUUUUUUUUUUUUUU'))
print(solution('LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL'))
print(solution('RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR'))
print(solution('DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD'))
print(solution('ULURRDLLU'))
print(solution('LULLLLLLU'))
print(solution('UDUDUDUDUD'))