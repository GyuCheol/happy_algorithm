
# 정수 삼각형
# https://programmers.co.kr/learn/courses/30/lessons/43105
# 다이나믹 프로그래밍

# n은 2차원 배열의 길이
# 2차원 배열로 memorization 필요해보임
# d[0][0]이 꼭대기에 있는 마지막 합이라고 생각한다면,
# 아래와 같이 점화식을 세워볼 수 있겠다.
# d[0][0] = max(d[n-i][j], d[n-i][j+1]) + triangle[i][j]

def solution(triangle):
    n = len(triangle)
    # 2차원 배열 생성 (삼각형 크기에 맞게)
    d = [[0 for j in range(i + 1)] for i in range(n)]

    # 맨 마지막 층은 tringle 맨 아랫층으로 초기화
    
    for i in range(0, n):
        d[n-1][i] = triangle[n-1][i]

    # bottom-up
    for i in range(1, n):
        
        # 현재 위치의 바로 밑에 있는 데이터의 max 값을 계산해야 하므로
        # n - i을 하면, 각 배열 요소의 크기가 나올 것이다. 4, 3, 2, 1
        # 0일 때 0, 1 비교
        # 1일 때 1, 2 비교 
        for j in range(0, n - i):
            
            d[n-i-1][j] = max(d[n-i][j], d[n-i][j + 1]) + triangle[n-i-1][j]
            

    return d[0][0]

# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
