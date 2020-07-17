# 7월 17일

# 게임 맵 최단거리
# https://programmers.co.kr/learn/courses/30/lessons/1844
# 연습문제 (BFS) - lv 4

# 최단거리로 특정 좌표까지 가는 칸 출력
# (0,0)에서 (n,m)까지 가야함.
# 단순 BFS 문제 같은데 이게 왜 lv4? 조금 의아함.

# 시간 복잡도 O(n^2)

from collections import deque

def solution(maps):
    q = deque()
    target_y = len(maps) - 1
    target_x = len(maps[0]) - 1

    q.append((0, 0, 1))

    while len(q) > 0:
        x, y, step = q.popleft()

        # 도착한 경우
        if x == target_x and y == target_y:
            return step

        # 상하좌우 탐색
        for nx, ny in [[-1, 0], [1, 0], [0, -1], [0, +1]]:
            # 경계 안이라면
            cx = x + nx
            cy = y + ny
            if 0 <= cx <= target_x and 0 <= cy <= target_y and maps[cy][cx] == 1:
                # -1은 이미 밟은 길 mark
                maps[cy][cx] = -1
                q.append((cx, cy, step + 1))
        
    return -1

# exptected 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))

# expected -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

tmp = [[1 for x in range(100)] for y in range(100)]
print(solution(tmp))