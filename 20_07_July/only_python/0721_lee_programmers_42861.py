# 7월 21일

# 섬 연결하기
# https://programmers.co.kr/learn/courses/30/lessons/42861
# Greedy - lv3

# 문제의 뉘앙스가 MST(최소 신장 트리) 알고리즘를 느껴지게 한다.
# Greedy 적인 방법으로, 현재 고를 수 있는 간선 중에서 
# 가장 작은 간선만을 선택한다.
# 이때 싸이클이 생기지 않는 간선을 선택하도록 해야한다.
# 참고 자료 : https://ghkvud2.tistory.com/97

# 1] 모든 간선을 heap 추가한다. (비용 순으로)
# 2] 모든 노드가 연결될 때까지 반복
# 3] heap에 있는 최솟값 pop
# 4] cycle이 형성되는지 확인 후 이상이 없다면 추가한다.
# 5] 2번으로 돌아가기
# ※ 싸이클의 형성을 체크하려면 Disjoint Set이라는 방법을 사용 (https://ghkvud2.tistory.com/98)

# disjoint_set
# 모든 노드마다 각각의 set을 만든다. (make_set)
# 노드가 연결될 때 마다 각 set을 합친다. (union)
# 어떤 노드가 어떤 집합에 속하는지 찾는다. (find)

# O(NlogN) - heap을 응용했기 때문.

import heapq

def solution(n, costs):
    answer = 0
    hq = []

    # 싸이클 검사를 위한 disjoint set 생성 (make_set)
    # 각 노드에 대한 set을 만든다. (처음에는 아무도 연결이 안되었으므로)
    disjoint_set = [{n} for n in range(n)]

    # 특정 노드가 어느 집합에 속하는지 (find)
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
            # 연결 되었으므로 2개의 set을 하나로 합친다. (union)
            start_set |= end_set
            disjoint_set.remove(end_set)
    
    return answer

# print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(solution(7, [[0, 1, 29], [0, 2, 10], [1, 4, 16], [1, 3, 15], [2, 5, 27], [3, 5, 25], [3, 6, 18], [4, 6, 12], [5, 6, 22]]))