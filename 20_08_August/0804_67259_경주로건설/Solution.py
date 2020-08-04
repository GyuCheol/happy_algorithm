from collections import deque

INF = 0x7fffffff
# 상하좌우 0123
DIRECTION = ((0, -1), (0, 1), (-1, 0), (1, 0))

def solution(board):
    q = deque()
    l = len(board)
    map_cost = [[[INF, INF, INF, INF] for j in range(l)] for i in range(l)]

    map_cost[0][0] = [0, 0, 0, 0]

    def push_node(x, y, dir, cost):

        if not(0 <= x < l and 0 <= y < l):
            return

        if board[y][x] == 0 and cost < map_cost[y][x][dir]:
            map_cost[y][x][dir] = cost
            q.append((x, y, dir, cost))

    push_node(1, 0, 3, 100)
    push_node(0, 1, 1, 100)

    while q:
        x, y, dir, cost = q.popleft()
        
        for d in range(4):
            nx, ny = DIRECTION[d]
            push_node(x + nx, y + ny, d, cost + (100 if d == dir else 600))

    return min(map_cost[l-1][l-1])


print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))
