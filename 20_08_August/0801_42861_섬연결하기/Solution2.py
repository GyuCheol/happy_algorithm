import heapq

# 최소 신장 트리 프림 알고리즘으로 작성

class Edge():

    def __init__(self, to, cost):
        self.to = to
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost

def solution(n, costs):
    hq = []
    edges = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    cost = 0

    for f, t, c in costs:
        edges[f].append(Edge(t, c))
        edges[t].append(Edge(f, c))
    
    visited[0] = 1

    # 기본 값으로 0번 정점의 모든 간선 추가하기
    for edge in edges[0]:
        heapq.heappush(hq, edge)
    
    for _ in range(n - 1):
        
        # 가장 최소 간선 꺼내기, 방문하지 않은 정점이 나올 때까지
        e = heapq.heappop(hq)

        while visited[e.to] == 1:
            e = heapq.heappop(hq)

        cost += e.cost
        visited[e.to] = 1

        for edge in edges[e.to]:
            if visited[edge.to] == 0:
                heapq.heappush(hq, edge)


    return cost

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))