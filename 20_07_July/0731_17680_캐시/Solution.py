from collections import deque

def solution(cacheSize, cities):
    deq = deque()
    cost = 0
    s = set()

    # 0이면 loop 계산할 필요가 없음.
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        name = city.lower()

        if name in s:
            cost += 1
            deq.remove(name)
        else:
            cost += 5
            if len(deq) == cacheSize:
                s.remove(deq.popleft())
            
            s.add(name)

        deq.append(name)
        

    return cost