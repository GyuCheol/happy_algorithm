from collections import deque

def solution(n, s, a, b, fares):
    path = {id: [] for id in range(1, n + 1)}

    for start, to, cost in fares:
        path[start].append((to, cost))
        path[to].append((start, cost))
    
    cost_list = [0x7fffffff for _ in range(n + 1)]

    q = deque()
    cost_list[s] = 0
    q.append((s, 0))

    while q:
        node, cost = q.popleft()

        for next, c in path[node]:
            tmp = cost + c

            if tmp <= cost_list[next]:
                cost_list[next] = tmp
                q.append((next, tmp))
    
    min_value = 0x7fffffff
    min_node = 0

    for i in range(1, n + 1):
        cost_list2 = [0x7fffffff for _ in range(n + 1)]

        cost_list2[i] = 0
        q.append((i, 0))

        while q:
            node, cost = q.popleft()

            for next, c in path[node]:
                tmp = cost + c

                if tmp <= cost_list2[next]:
                    cost_list2[next] = tmp
                    q.append((next, tmp))
        
        if (cost_list2[a] + cost_list2[b] + cost_list[i]) < min_value:
            min_node = i
            min_value = cost_list2[a] + cost_list2[b] + cost_list[i]
    
    cost_list3 = [0x7fffffff for _ in range(n + 1)]
    q = deque()
    cost_list3[min_node] = 0
    q.append((min_node, 0))

    while q:
        node, cost = q.popleft()

        for next, c in path[node]:
            tmp = cost + c

            if tmp <= cost_list3[next]:
                cost_list3[next] = tmp
                q.append((next, tmp))


    return cost_list[min_node] + cost_list3[a] + cost_list3[b]

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
