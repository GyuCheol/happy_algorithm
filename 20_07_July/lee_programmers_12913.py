# 7월 15일

# 땅따먹기
# https://programmers.co.kr/learn/courses/30/lessons/12913
# lv2 연습문제 (DP?)

# DP적인 관점으로 문제를 봐야한다.
# 최대 N이 100,000 * 4라서 O(400,000)이 되어도 큰 문제는 없다.
# DP적인 관점으로 자기 열을 제외한 최댓값을 누적하며 내려오자. 

# 시간 복잡도 O(N)

def solution(land):
    d = [[0, 0, 0, 0] for _ in range(len(land))]

    d[0] = land[0]

    for y in range(1, len(land)):
        for x in range(4):
            tmp = []
            for k in range(4):
                if x != k:
                    tmp.append(d[y-1][k])

            d[y][x] = land[y][x] + max(tmp)

    return max(d[len(land) - 1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))