import heapq

# 크루스칼 알고리즘

def solution(n, costs):
    answer = 0
    hq = []

    # 싸이클 검사를 위한 disjoint set 생성
    disjoint_set = [set([n]) for n in range(n)]

    def find_set(node):
        for s in disjoint_set:
            if node in s:
                return s

    for start, end, cost in costs:
        heapq.heappush(hq, (cost, start, end))

    # 모든 노드가 연결되었다면 종료
    # disjoint_set이 1이 되었다는 뜻.
    while len(disjoint_set) > 1:
        cost, start, end = heapq.heappop(hq)

        # 싸이클이 형성되는가?
        # 새로 연결할 간선이 이미 같은 간선 그룹과 연결된 경우 싸이클이 형성된다.
        start_set = find_set(start)
        end_set = find_set(end)

        if start_set != end_set:
            answer += cost
            # 연결 되었으므로 2개의 set을 하나로 합친다.
            start_set |= end_set
            disjoint_set.remove(end_set)
    
    return answer