# 7월 20일

# 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189
# 그래프 - lv3

# BFS로 탐색해서 가장 끝에 있던 거리를 출력하면 끝.
# vertex가 2만개일 수 있어서, 배열로 처리하다간 좋지 않다.
# 각 node가 가진 경로를 링크드 리스트 방식으로 가지고 있는 것이 좋겠음
# 참고로 딱히 queue쓰지 않아도 된다.

# O(N^2)


def solution(n, edge):
    visited = [0] * (n + 1)
    path_list = [[] for _ in range(n + 1)]
    s = []

    s.append(1)
    visited[1] = 1

    for fr, to in edge:
        path_list[fr].append(to)
        path_list[to].append(fr)

    while s:
        tmp = []

        # 현재 list에 있는 모든 node 담음
        for node in s:
            for to in path_list[node]:
                if visited[to] == 0:
                    visited[to] = visited[node] + 1
                    tmp.append(to)
        s = tmp

    return visited.count(max(visited))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))