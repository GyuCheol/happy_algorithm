from collections import deque

def solution(n, edge):
    distance = [0 for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    q = deque()
    maximum_distance = 1

    for f, t in edge:
        graph[f].append(t)
        graph[t].append(f)

    distance[1] = 1
    q.append((1, 1))

    while q:
        node, d = q.popleft()

        for e in graph[node]:

            if distance[e] == 0:
                distance[e] = d + 1
                maximum_distance = max(maximum_distance, distance[e])
                q.append((e, distance[e]))

    return distance.count(maximum_distance)


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
