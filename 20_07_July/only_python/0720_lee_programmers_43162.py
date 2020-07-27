# 7월 20일

# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162
# DFS/BFS - lv3

# lv3부터는 조금 심화단계의 문제가 많이 나온다.
# 특히 자료구조와 탐색 알고리즘을 같이 사용하는 문제가 주로 lv3으로 채택되는 듯.
# 네트워크 문제는 BFS 또는 DFS와, 그 지점을 방문 했는지 정보를 가지고
# 해결 할 수 있다.

# 주어진 computers 인자는 그래프 구조를 2차원 배열로 온 것이라는 걸 참고
# computers[1][2] = 1이라면 1번과 2번은 연결된 것이다.
# BFS는 queue를 써야하니 그냥 DFS로 탐색해서 해결

# O(n^2)


def solution(n, computers):
    # 방문 정보 저장용
    check = [0] * n
    answer = 0

    def dfs(s):
        if s == n:
            return

        for i in range(n):
            if s != i and computers[s][i] == 1 and check[i] == 0:
                check[i] = 1
                dfs(i)

    for i in range(n):
        if check[i] == 0:
            answer += 1
            check[i] = 1
            dfs(i)

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
