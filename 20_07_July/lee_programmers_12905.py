# 7월 14일

# 가장 큰 정사각형
# https://programmers.co.kr/learn/courses/30/lessons/12905
# DP - lv 2

# 3*3의 정사각형이 되려면 일단 2*2 값이 있어야한다.
# 그러므로 작은 사각형에서 부터 누적시키며 큰 사각형을 만든다는 로직으로
# 풀어나가면 된다. 사각형의 조건으로 위, 왼쪽, 왼쪽 위가 채워졌는지를 확인하면 된다.
# 다만, 위, 왼쪽, 왼쪽 위 중에서 가장 작은 값이 현재 만들 수 있는 사각형의 변 길이가 된다
# 가장 작은 값에 맞춰 변의 길이가 최소 만족하기 때문

# -1이 -1을 검사할 수 있는 문제가 있어 기존 board 크기보다 1씩 큰 배열을 만들어 해결하면 된다. (또는 경계검사)

# 예전에 풀어봤던 문젠데 많이 헷갈렸다..
# 왼쪽, 위쪽은 감이 왔는데 왼쪽위까지는 잘 생각을 못했네

# 점화식 d[n][n] = min(d[n][n-1], d[n-1][n], d[n-1][n-1]) + 1
# 시간 복잡도 O(n^2)

def solution(board):
    h = len(board)
    w = len(board[0])

    # 경계 체크를 용이하게 하기 위해 +1씩
    tmp = [[0 for x in range(w + 1)] for y in range(h + 1)]
    answer = 0

    for y in range(h):
        for x in range(w):
            tmp[y + 1][x + 1] = board[y][x]

    for y in range(1, h + 1):
        for x in range(1, w + 1):
            
            # 채워져 있고, 왼쪽, 위, 왼쪽위 모두 같은 값인 경우
            # 현재 값을 정사각형이 가능한 변의 길이로 지정
            if tmp[y][x] > 0:

                if tmp[y-1][x] > 0 and tmp[y][x-1] > 0 and tmp[y-1][x-1] > 0:
                    tmp[y][x] = min(tmp[y-1][x], tmp[y][x-1], tmp[y-1][x-1]) + 1

                # 최댓값 누적
                answer = max(tmp[y][x], answer)
    
    # 정사각형 너비로 반환하기 위해 제곱
    return answer ** 2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
print(solution([[1, 1], [1, 1]]))
print(solution([[1, 1], [1, 0]]))

