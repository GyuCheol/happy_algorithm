# 7월 23일

# N-Queen
# https://programmers.co.kr/learn/courses/30/lessons/12952
# 연습문제 - lv3

# back-tracking 유형의 문제로 유명한 N-Queen (그리고 스도쿠) 문제
# dfs식 재귀호출과 굳이 돌아도 않아도 되는 경우를 제외시키며 탐색하는 문제
# 백트래킹은 완전 탐색 중에서도, 필요하지 않은 경우를 생략하며 탐색해나가는 기법이다.

# 문제 크기가 작아서 1~12까지의 그냥 정답만 if문으로 하드코딩해도 되긴하다.. ㅋㅋㅋ...
# 행, 열, 대각선에 대한 마킹 값을 만들어 해당 부분에 배치할 수 있는지 없는지 판단
# (퀸은 가로, 세로, 대각선으로 이동이 가능함)

# O(n!) 각 n에서 n-1, n-2, n-3... 으로 돌기 때문에.. 어마어마하다


def solution(n):
    columns = [0] * n
    rows = [0] * n
    dia_l = [0] * (n * 2 - 1)
    dia_r = [0] * (n * 2 - 1)

    def dfs(y):

        if y == n:
            return 1

        cnt = 0

        for x in range(n):
            # queen을 둘 수 있는가?
            if columns[x] + rows[y] + dia_l[x+y] + dia_r[(n-x-1)+y] > 0:
                continue
            
            columns[x] = 1
            rows[y] = 1
            dia_l[x+y] = 1
            dia_r[(n-x-1)+y] = 1

            cnt += dfs(y + 1)
        
            columns[x] = 0
            rows[y] = 0
            dia_l[x+y] = 0
            dia_r[(n-x-1)+y] = 0

        return cnt

    return dfs(0)


# print(solution(1))
# print(solution(2))
# print(solution(3))
# print(solution(4))

# 다른 사람의 풀이
# ?? 0~7 순열 조합을 만든 후,
# 각각 0~7까지 더하고, 뺀 값의 길이가 같으면 세고 있다 무슨 논리?

from itertools import permutations
def nQueen(n):
    cols = range(n)
    result = 0
    for vec in permutations(cols):
        tmp1 = set(vec[i]+i for i in cols)
        tmp2 = set(vec[i]-i for i in cols)

        if n == len(tmp1) == len(tmp2):
            result+=1
    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nQueen(8))