# 7월 24일

# 경주로 건설
# https://programmers.co.kr/learn/courses/30/lessons/67259
# 2020 카카오 인턴쉽 - lv3

# BFS 문제 같다.
# 다만, 움직이는 방향과 비용을 누적하며 진행시켜야한다!
# 그리고 항상 최소비용을 우선으로 먼저 탐색하도록 해야한다.
# (안 그러면 비효율적인 경로가 생길 수 있다.)
# heap에다가 항상 최소 비용을 우선으로 우선 움직일 수 있도록 하는 것이 좋겠음.
# 만약 비용이 완전 같은 경우는, 같은 방향을 우선으로 먼저 탐색해야함

# O(N^3)? 겹치는 구간이 많으면 더 많이 탐색 할듯..

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
