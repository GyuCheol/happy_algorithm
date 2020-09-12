from itertools import permutations
from collections import deque
from copy import deepcopy

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Info:

    def __init__(self):
        self.alive = False
        self.pt1 = (0, 0)
        self.pt2 = (0, 0)

TEMP = [[0, 0, 0, 0] for _ in range(4)]

def solution(board, r, c):
    info = [Info() for _ in range(7)]

    def get_xy(n, y, x):
        for y2 in range(4):
            for x2 in range(4):
                if y == y2 and x == x2:
                    continue
                
                if board[y2][x2] == n:
                    return y2, x2
                    
    
    def get_cost(pt1, pt2):

        tmp_visited = deepcopy(TEMP)
        q = deque()

        q.append((pt1[0], pt1[1], 0))

        while q:
            y, x, step = q.popleft()

            if y == pt2[0] and x == pt2[1]:
                return step

            # 상하좌우
            for d in DIRECTIONS:
                ny = y + d[0]
                nx = x + d[1]
                
                if 0 <= ny <= 3 and 0 <= nx <= 3 and tmp_visited[ny][nx] == 0:
                    tmp_visited[ny][nx] = 1
                    q.append((ny, nx, step + 1))
            
            # ctrl 상
            for i in range(1, 4):
                if (y - i) < 0:
                    break
                if (y - i) == 0 or (board[y-i][x] != 0 and tmp_visited[y-i][x] == 0):
                    tmp_visited[y-i][x] = 1
                    q.append((y-i, x, step + 1))
                    break

            # 하
            for i in range(1, 4):
                if (y + i) > 3:
                    break
                if (y + i) == 3 or (board[y+i][x] != 0 and tmp_visited[y+i][x] == 0):
                    tmp_visited[y+i][x] = 1
                    q.append((y+i, x, step + 1))
                    break

            # ctrl 좌
            for i in range(1, 4):
                if (x - i) < 0:
                    break
                if (x - i) == 0 or (board[y][x-i] != 0 and tmp_visited[y][x-i] == 0):
                    tmp_visited[y][x-i] = 1
                    q.append((y, x-i, step + 1))
                    break

            # 우
            for i in range(1, 4):
                if (x + i) > 3:
                    break
                if (x + i) == 3 or (board[y][x+i] != 0 and tmp_visited[y][x+i] == 0):
                    tmp_visited[y][x+i] = 1
                    q.append((y, x+i, step + 1))
                    break


    card_map = []
    for y in range(4):
        for x in range(4):
            n = board[y][x]

            if n != 0 and info[n].alive == False:
                info[n].alive = True
                info[n].pt1 = (y, x)
                info[n].pt2 = get_xy(n, y, x)
                card_map.append(n)

    def set_value(info, value):
        board[info.pt1[0]][info.pt1[1]] = value
        board[info.pt2[0]][info.pt2[1]] = value


    def search(it, i, pt, total_cost):

        if i == len(it):
            return total_cost
        else:
            n = it[i]
            cost = total_cost + get_cost(info[n].pt1, info[n].pt2)

            c1 = get_cost(pt, info[n].pt1) + cost
            
            set_value(info[n], 0)
            c1 = search(it, i + 1, info[n].pt2, c1)
            set_value(info[n], n)
            
            c2 = get_cost(pt, info[n].pt2) + cost

            set_value(info[n], 0)
            c2 = search(it, i + 1, info[n].pt1, c2)
            set_value(info[n], n)
            
            return min(c1, c2)

    answer = 0x7fffffff

    for it in permutations(card_map, len(card_map)):
        val = search(it, 0, (r, c), 0)
        # enter 비용
        val += len(it) * 2
        
        if val < answer:
            print(it)
            answer = val
    
    return answer

# print(solution([[1,0,0,0],[2,0,0,0],[2,0,0,0],[0,0,0,1]], 1, 0))
# print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
# print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))
print(solution([[1,2,2,1],[0,0,0,0],[5,5,6,6],[3,4,4,3]], 0, 0))

# print(solution([[0,0,0,0],[0,0,0,0],[0,0,0,1],[1,0,0,0]], 1, 1))

# print(solution([[2,0,1,0],[0,3,3,0],[0,0,0,0],[2,0,1,0]], 1, 1))

