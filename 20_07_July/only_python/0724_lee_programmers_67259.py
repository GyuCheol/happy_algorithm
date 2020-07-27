# 7월 24일

# 경주로 건설
# https://programmers.co.kr/learn/courses/30/lessons/67259
# 2020 카카오 인턴쉽 - lv3

# BFS 문제
# 다만, 각 좌표마다 어떤 방향으로 왔는지 기록하며 움직여야 한다.
# 1, 0의 오른쪽에서 온 값, 왼쪽에서 온 값, 위쪽에서 온 값, 등
# 그래서 N*N*4의 공간을 할당해서 처리하고,
# 각 방향마다 최솟값이 가능한 경우 해당 최솟값으로 덮어씌우고 탐색을 진행한다.
# 다익스트라식 접근법과 유사하다.
# 이 문제에서 멘탈이 엄청 나갔음.

# O(N^2)? 겹치는 구간이 많으면 더 많이 탐색 할듯..

from collections import deque

DIRECTION = [[0, -1], [0, 1], [-1, 0], [1, 0]]
INF = 2 ** 31

def solution(board):
    q = deque()
    l = len(board)
    cost_map = [[[INF for k in range(4)] for j in range(l)] for i in range(l)]

    board[0][0] = -1

    # (x, y, 방향)
    # 0 1 2 3 상하좌우
    if board[0][1] == 0:
        q.append((1, 0, 3))
        cost_map[0][1][3] = 100
    
    if board[1][0] == 0:
        q.append((0, 1, 1))
        cost_map[1][0][1] = 100
    
    while q:
        x, y, prev_d = q.popleft()

        for d in range(4):
            cx = DIRECTION[d][0] + x
            cy = DIRECTION[d][1] + y

            if 0 <= cx < l and 0 <= cy < l and board[cy][cx] == 0:
                cur_cost = cost_map[y][x][prev_d] + (100 if d == prev_d else 600)
                if cost_map[cy][cx][d] >= cur_cost:
                    cost_map[cy][cx][d] = cur_cost
                    q.append((cx, cy, d))
    
    return min(cost_map[l-1][l-1])

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,1],[0,0,1],[1,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
