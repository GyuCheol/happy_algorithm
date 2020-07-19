# 7월 18일

# 프렌즈4블록
# https://programmers.co.kr/learn/courses/30/lessons/17679
# 2018 카카오 블라인드 공채 1차 - lv2

# 2중 루프 돌며 현재 위치에서 (현재 위치 +1, +1)까지 전부 다 같으면 마킹을 하고,
# 마킹이 다 끝나면 소거하며 블럭을 제거해나간다.
# 변화가 없다면 바로 종료
# 로직은 간단하다.
# 문자열로 두는 것보단, 2차원 배열 상태가 좋다.

# O(N^2)

def solution(m, n, board):
    answer = 0

    # 2차원 배열로 변환
    map = [[ch for ch in row] for row in board]
    s = []
    
    while True:
        
        # 탐색하며 제거할 블록 s에 추가하기
        for y in range(m - 1):
            for x in range(n - 1):
                # 현재 위치에서 4블록 모두 같다면 s에 추가
                if map[y][x] != '' and map[y][x] == map[y + 1][x] == map[y][x + 1] == map[y + 1][x + 1]:
                    s.append((y, x))

        # 찾은 4블록이 없다면 종료
        if len(s) == 0:
            break
        else:
            # 4블록 제거
            while s:
                y, x = s.pop()
                map[y][x] = ''
                map[y + 1][x] = ''
                map[y][x + 1] = ''
                map[y + 1][x + 1] = ''
            
            # 빈값 끌어올리기
            for y in range(m - 1, 0, -1):
                for x in range(n):
                    # 빈 값이라면 상위에 있는 값 아무거나로 채워야함.
                    if map[y][x] == '':
                        for k in range(y-1, -1, -1):
                            if map[k][x] != '':
                                map[y][x], map[k][x] = map[k][x], map[y][x]
                                break
    
    # ''의 개수가 지워진 블록 개수다.
    for r in map:
        answer += r.count('')

    return answer

print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))