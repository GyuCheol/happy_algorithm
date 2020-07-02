
# 등굣길
# https://programmers.co.kr/learn/courses/30/lessons/42898
# 다이나믹 프로그래밍
# 1,1에서 n,n까지 가는 경로 개수 출력

# 점화식 : d[n][n] = d[n-1][n] + d[n][n-1]


def solution(m, n, puddles):
    # m*n 생성 (n,n을 위해 0,0~n,n까지 생성)
    d = [[0 for x in range(m + 1)] for y in range(n + 1)]
    
    for x, y in puddles:
        # -1은 갈 수 없음을 마크
        d[y][x] = -1

    d[1][1] = 1

    for y in range(1, n + 1):
        for x in range(1, m + 1):
            
            if d[y][x] == 0:
                tmp = []

                if d[y-1][x] > 0:
                    tmp.append(d[y-1][x])

                if d[y][x-1] > 0:
                    tmp.append(d[y][x-1])

                # python이므로 (a % m + b % m) % m을 할 필요는 없다.
                d[y][x] = sum(tmp) % 1000000007


    return d[n][m]

print(solution(4, 3, [[2, 2]]))
print(solution(4, 3, []))