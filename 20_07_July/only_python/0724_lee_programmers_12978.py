# 7월 24일

# 배달
# https://programmers.co.kr/learn/courses/30/lessons/12978
# Summer/Winter Coding (2018) - lv3

# 다익스트라 알고리즘을 이용한다고 한다...
# 2시간을 고민했지만 ㅠ.ㅜ 나의 한계였음. 다른 힌트를 참고함.
# 다익스트라 알고리즘은 각 정점에서 다른 정점까지의 도달 가능한 최소 거리를 모두 구하는 알고리즘이다.

# 거리를 구하고 싶은 첫 출발 정점을 큐에 노드를 넣는다.
# 큐에 있는 노드를 빼서 해당 노드가 도달 가능한 다른 정점과의 거리를 확인하고 큐에 넣는다.
# 이때 각 노드의 도달 가능한 거리를 지금까지 누적한 비용과 비교하여 최솟값으로 업데이트한다.
# 반복 반복

# 우선 순위 큐를 이용하므로 heapq가 필요하다.
# 각 정점에 도달하는 최소 도달 값을 계산할 수 있다.

# 1번을 큐에 넣는다
# 큐에 있는 값을 꺼낸다.
# 해당 값에서 연결 가능한 다른 모든 노드을 확인하고 거리를 최솟값으로 업데이트 한다.

# O(N^2)

import heapq

INF = 2 ** 31

def solution(N, road, K):
    village = [dict() for _ in range(N + 1)]
    hq = []
    visited = [INF for _ in range(N + 1)]

    for f, t, d in road:
        if t in village[f]:
            village[f][t] = min(village[f][t], d)
        else:
            village[f][t] = d

        if f in village[t]:
            village[t][f] = min(village[t][f], d)
        else:
            village[t][f] = d
        
    visited[1] = 0
    heapq.heappush(hq, (0, 1))

    while hq:
        cost, node = heapq.heappop(hq)

        for t, distance in village[node].items():
            if (cost + distance) <= visited[t]:
                heapq.heappush(hq, (cost + distance, t))

                visited[t] = min(visited[t], cost + distance)

    answer = 0

    for v in visited[1:]:
        if v <= K:
            answer += 1

    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	, 4))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 1))
print(solution(8, [[1, 2, 1], [1, 4, 4], [1, 7, 7], [2, 3, 1], [3, 6, 1], [4, 5, 1], [5, 6, 1], [7, 8, 1], [6, 8, 1]], 5))
print(solution(5, [[1, 2, 1], [1, 4, 1], [3, 4, 1], [1, 3, 5], [3, 5, 1]], 5))
