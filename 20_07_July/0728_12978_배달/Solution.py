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