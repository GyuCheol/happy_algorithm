def solution(n, build_frame):
    map = [[[0, 0] for j in range(n + 1)] for i in range(n+1)]

    # 전제 조건
    # 1. 기둥 밑에 기둥이 있거나, 보가 있어야 함
    # 2. 보 밑에 기둥이 있거나 양쪽에 다른 보가 있어야 함
    # 3. 삭제가 다른 기둥, 보 상태에 영향을 주어선 안됨.

    def check_column(x, y):
        
        # 바닥에는 바로 설치 가능
        if y == 0:
            return True

        # 밑에 기둥이 있거나, 보가 왼쪽이나 오른쪽에 있거나
        return map[y-1][x][0] == 1 or (x > 0 and map[y][x-1][1] == 1) or map[y][x][1] == 1


    def check_wrapping_cloth(x, y):

        if map[y-1][x][0] == 1 or map[y-1][x+1][0] == 1:
            # 좌우 중 한 쪽이라도 기둥이 있는 경우 가능
            return True
        elif (x > 0 and map[y][x-1][1] == 1) and map[y][x+1][1] == 1:
            # 좌우로 보가 붙어있어야함.
            return True
        
        return False

    # a 0은 기둥, 1은 보
    # b 0은 삭제, 1은 추가
    for x, y, a, b in build_frame:
        if a == 0:
            # 기둥
            if b == 0:
                if map[y][x][0] == 1:
                    # 기존 기둥이 존재해야함.
                    # 삭제 시, 윗 기둥 양 옆의 보가 조건을 만족하는가?
                    map[y][x][0] = 0
                    
                    conditions = []
                    # 윗기둥이 존재하며, 만족하는가
                    if map[y + 1][x][0] == 1:
                        conditions.append(check_column(x, y+1))
                    
                    # 왼쪽 보가 존재하며 만족하는가
                    if x > 0 and map[y+1][x-1][1] == 1:
                        conditions.append(check_wrapping_cloth(x-1, y+1))

                    # 우측 보가 존재하며 만족하는가.
                    if map[y+1][x][1] == 1:
                        conditions.append(check_wrapping_cloth(x, y+1))

                    if all(conditions) == False:
                        # 만족하지 않으면 되돌림.
                        map[y][x][0] = 1
                
            else:
                if check_column(x, y):
                    map[y][x][0] = 1

        else:
            # 보
            if b == 0:
                # 삭제
                if map[y][x][1] == 1:
                    # 제거하려는 보 존재

                    # 제거
                    map[y][x][1] = 0
                    
                    conditions = []

                    # 바로 위에 기둥 있는 경우
                    if map[y][x][0] == 1:
                        conditions.append(check_column(x, y))

                    # x+1 위에 기둥 있는 경우
                    if map[y][x+1][0] == 1:
                        conditions.append(check_column(x+1, y))

                    # x-1 보
                    if x > 0 and map[y][x-1][1] == 1:
                        conditions.append(check_wrapping_cloth(x-1, y))

                    # x+1 보
                    if x < (n-1) and map[y][x+1][1] == 1:
                        conditions.append(check_wrapping_cloth(x+1, y))

                    if all(conditions) == False:
                        # 삭제 불가능한 경우 되돌림
                        map[y][x][1] = 1

            else:
                # 추가
                if check_wrapping_cloth(x, y):
                    map[y][x][1] = 1

    result = []

    for x in range(n + 1):
        for y in range(n + 1):
            for k in range(2):
                if map[y][x][k] == 1:
                    result.append([x, y, k])

    return result

solution(5, [[0,0,0,1],[3,0,0,1],[0,1,1,1],[2,1,1,1],[1,1,1,1],[1,0,0,1],[1,1,1,0]])

# solution(5, [[0,1,1,1],[0,0,0,1],[1,0,0,1],[0,1,0,1],[2,1,0,1],[0,1,1,1]])
# solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
# solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])