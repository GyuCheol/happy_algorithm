from collections import deque

HORIZONTAL = 0
VERTICAL = 1
MODE_XY = ((1, 0), (0, 1))
DIRECTIONS = ((0, -1), (0, 1), (-1, 0), (1, 0))
ROTATIONS = (
    # 가로 (기준 변경, 체크 위치)
    (
        ((0, 0), (1, 1)),
        ((0, -1), (1, -1)),
        ((1, 0), (0, 1)),
        ((1, -1), (0, -1)) 
    ),
    # 세로
    (
        ((0, 0), (1, 1)),
        ((0, 1), (1, 0)),
        ((-1, 0), (-1, 1)),
        ((-1, 1), (-1, 0))
    )
)

class Step():

    def __init__(self, step, x, y, mode):
        self.step = step
        self.x = x
        self.y = y
        self.mode = mode

def solution(board):
    l = len(board)
    visited = [[[0, 0] for j in range(l)] for i in range(l)]
    q = deque()

    visited[0][0][HORIZONTAL] = 1
    q.append(Step(0, 0, 0, HORIZONTAL))

    # 모드에 해당하는 다른 블럭 체크
    def can_be_located(x, y, mode):
        
        nx, ny = x + MODE_XY[mode][0], y + MODE_XY[mode][1]

        return 0 <= nx < l and 0 <= ny < l and board[ny][nx] == 0

    def can_move(x, y, d, mode):
        nx, ny = x + d[0], y + d[1]

        if not(0 <= nx < l and 0 <= ny < l) or board[ny][nx] == 1 or can_be_located(nx, ny, mode) == False:
            return False
            
        return visited[ny][nx][mode] == 0


    def can_rotate(x, y, r, mode):
        nx, ny = x + r[0][0], y + r[0][1]
        bx, by = x + r[1][0], y + r[1][1]
        
        if all([0 <= pt < l for pt in (nx, ny, bx, by)]) and board[ny][nx] == 0 and board[by][bx] == 0 and can_be_located(nx, ny, mode):
            return visited[ny][nx][mode] == 0

        return False


    while q:
        f = q.popleft()

        # 디버깅
        # print(f.x, f.y, f.mode, f.step)

        if f.mode == HORIZONTAL and f.x == (l-2) and f.y == (l-1):
            return f.step
        elif f.mode == VERTICAL and f.x == (l-1) and f.y == (l-2):
            return f.step

        # 현재 모드에서 상하좌우 이동
        for d in DIRECTIONS:

            if can_move(f.x, f.y, d, f.mode):
                nx, ny = f.x + d[0], f.y + d[1]

                visited[ny][nx][f.mode] = 1
                q.append(Step(f.step + 1, nx, ny, f.mode))

        # 다른 모드로 변경하는 4가지 경우
        for r in ROTATIONS[f.mode]:

            if can_rotate(f.x, f.y, r, f.mode ^ 1):
                nx = f.x + r[0][0]
                ny = f.y + r[0][1]
                visited[ny][nx][f.mode ^ 1] = 1
                
                q.append(Step(f.step + 1, nx, ny, f.mode ^ 1))

    return -1


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
print(solution([[0, 0, 1], [0, 0, 1], [0, 0, 0]]))

tmp = [[0 for j in range(100)] for i in range(100)]
print(solution(tmp))

print(solution([
    [0, 0, 1, 1, 1], 
    [0, 0, 0, 0, 1], 
    [1, 1, 0, 0, 0], 
    [1, 1, 1, 0, 0], 
    [1, 1, 1, 1, 0]]))