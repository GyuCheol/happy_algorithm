from collections import deque

def solution(n, path, order):
    # 1 방문, 2 연결은 되었으나 오기 전에 다른 곳을 방문 했어야 함!
    visited = [0] * n
    # -1은 조건 없이 입장 가능, 이외 값은 해당 방을 거쳐야 입장 가능.
    required = [-1] * n
    graph = [[] for _ in range(n)]
    chained = [[] for _ in range(n)]
    
    for p in path:
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])

    for a, b in order:
        # b를 가려면, a를 먼저 방문해야 한다.
        required[b] = a

        # a를 방문하면 b 위치를 열기 위함.
        chained[a].append(b)

    q = deque()

    if required[0] != -1:
        return False
        
    visited[0] = 1
    q.append(0)

    while q:
        node = q.popleft()

        for to in graph[node]:
            if visited[to] == 0:
                # 조건이 있고, 해당 조건 방을 아직 입장 못한 경우 2로만 마킹
                if required[to] != -1 and visited[required[to]] == 0:
                    visited[to] = 2
                    continue
                
                visited[to] = 1
                q.append(to)

                # 현재 방이 선행 조건으로 연결된 다른 방을, 이미 도달했던 경우 q에 다시 추가하기
                for c in chained[to]:
                    if visited[c] == 2:
                        visited[c] = 1
                        q.append(c)

    return visited.count(1) == n

solution(2, [[0, 1]], [[1, 0]])

# solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]])
# solution(9, [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]], [[4, 1], [5, 2]])
# solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]])

