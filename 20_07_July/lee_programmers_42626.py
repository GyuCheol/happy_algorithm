# 7월 16일

# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626
# Heap - lv2

# Heap 자료 구조를 이용하여 가장 최솟값을 반출, 반입 과정을 반복하면서 
# 풀이하는 문제
# Heap 구조는 우선 순위 큐와 살짝 비슷한 모습을 보인다.
# 우선 순위 큐 또한 
# heapq 라는 자료구조를 이용해도 되긴 하지만,
# 실제 heap 구조를 구현해보는 것이 또 경험이 아닐까.

# heap은 주로 배열을 이용해서 구축이 된다.
# 0번 index는 사용하지 하고 1번부터 사용한다.
# 자식 노드의 index는 아래와 같이 구함
# left : (부모 노드 id) * 2
# right : (부모 노드 id) * 2 + 1
# 부모 노드 id : (자신의 id) // 2

# 시간 복잡도 O(NlogN) 정확하게는 NlogN + (N-1)*(NlogN)

from heapq import heappop, heappush

def solution(scoville, K):
    h = []
    answer = 0

    for s in scoville:
        heappush(h, s)

    while h[0] < K and len(h) >= 2:
        answer += 1
        first, second = heappop(h), heappop(h)
        heappush(h, first + second * 2)
    
    return answer if h[0] >= K else -1


# 직접 heap을 구현한 것 (왜 인지 시간 초과뜸..)
# 알수 없는 느릿느릿 파이썬의 세계.
def solution2(scoville, K):
    answer = 0

    # 맨 첫 값은 쓰지 않음
    # 공간 초기화를 위해 scoville만큼의 공간 assign
    # 안그러면 append로 인한 비용 때문에 시간 초과 먹는다.
    h = [0 for _ in range(len(scoville) + 1)]
    size = 0

    def add(n):
        nonlocal size
        # 가장 마지막에 추가
        size += 1
        h[size] = n

        # 자신의 부모 노드와 비교해서 위치 조정
        # 최소 힙으로 구성한다. 작으면 부모 노드가 된다.
        id = size
        parent = id // 2

        while parent > 0 and h[parent] > n:
            h[id], h[parent] = h[parent], h[id]
            id, parent = parent, parent // 2
                    

    def pop():
        nonlocal size
        # 가장 맨 윗 노드 반환
        tmp, last = h[1], h[size]
        h[size] = 0
        size -= 1
        # 가장 마지막 노드를 root로 이동 시킨 뒤,
        # 자리를 조정해야한다.
        if size == 0:
            return tmp

        h[1] = last
        id = 1

        # 자식 노드와의 검사를 위해 id * 2를 해야함.
        while True:
            left = id * 2
            right = id * 2 + 1

            if right <= size:
                # case1 left, right 모두 자식 노드가 있는 경우
                # left, right 중에 작은 노드와 교환한다.
                if h[id] > h[left] and h[left] < h[right]:
                    h[id], h[left] = h[left], h[id]
                    id = left
                elif h[id] > h[right]:
                    h[id], h[right] = h[right], h[id]
                    id = right
                else:
                    break

            elif left <= size:
                # case2 left만 있는 경우
                # left보다 크다면 교환한다.
                if h[id] > h[left]:
                    h[id], h[left] = h[left], h[id]
                    id = left
                else:
                    break

            else:
                # case3 자식 노드가 없으므로 종료
                break

        return tmp

    for s in scoville:
        add(s)
    
    # 최소 힙의 root 값이 K보다 작고,
    # 섞을 수 있는 재료가 2개 있다면
    while h[1] < K and size >= 2:
        answer += 1
        first = pop()
        second = pop()

        add(first + second * 2)


    return answer if h[1] >= K else -1

print(solution([3, 2, 1, 12, 9, 10], 7))
print(solution([3, 4], 7))