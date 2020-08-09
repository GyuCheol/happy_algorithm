# 7월 20일

# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059
# 2020 카카오 블라인드 채용 - lv3 (완전 탐색?)

# 열쇠를 회전시키며 자물쇠 배열에 만족하는지 확인하면 되는 문제
# 이전에도 풀어본 문제인데,
# 더 똑똑하게 풀기위해 2진 연산을 이용할까 해본다. (훨씬 속도가 빠르다)
# 풀이법은 열쇠를 회전하면서 자물쇠와 매칭을 하면 되는데
# 열쇠의 위치가 최소 (-{열쇠 가로 크기} - 1, -{열쇠 세로 크기} - 1) 부터 
# 최대 ({자물쇠 가로 크기} - 1, {자물쇠 세로 크기} - 1)까지의 모든 좌표를 매칭해서 맞는지 봐야한다.
# 시간 복잡도가 무려 n^4이긴하다..
# 2진 연산을 하게 되면 복잡도가 O(N^3)으로 확 감소하긴 하는데
# 머리가 너무 연산과정이 꼬여서 그냥 N^4로 풀자 ^.^

# 로직짜면서 공간적인 논리가 많이 필요했다..
# 2영역의 겹치는 부분,,, 어떻게 탐색해야 전체 탐색이 되는지..
# @.@ 여러 모로 머리 아팠던 문제 이거 때문에 오늘은 이 문제 다음은 lv3 중에서 쉬운 문제로..

# 예전에 작성한 답안에 비하면 정말 짧아졌음 우와!

# O(N^4)


def solution(key, lock):
    m = len(key)
    n = len(lock)
    empty_cnt = sum([lock[i].count(0) for i in range(n)])

    # 2차원 배열 90도 회전
    def rotate_to_right(k):
        return [[key[j-1][i] for j in range(m, 0, -1)] for i in range(m)]

    def check(loc_x, loc_y):
        mapping_cnt = 0
        
        for y in range(m):
            for x in range(m):
                cx = x + loc_x
                cy = y + loc_y

                # loc_x, loc_y 위치상 해당 영역이 lock 영역과 겹치는지
                # 겹친다면 2개의 합이 1이 되어야 한다.
                if cx in range(0, n) and cy in range(0, n) and key[y][x] == 1:
                    if lock[cy][cx] == 0:
                        mapping_cnt += 1
                    else:
                        return False
                    
        return empty_cnt == mapping_cnt

    # 총 4번 돌려서 검사
    for i in range(4):
        key = rotate_to_right(key)

        # m-1부터 n까지 
        for x in range(-(m-1), n):
            for y in range(-(m-1), n):
                if check(x, y):
                    return True
    
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
print(solution([[0, 0, 0], [1, 0, 0], [1, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
print(solution([[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
