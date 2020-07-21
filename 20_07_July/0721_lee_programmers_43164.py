# 7월 21일

# 여행 경로
# https://programmers.co.kr/learn/courses/30/lessons/43164
# DFS/BFS - lv3

# dictionary 이용해서 각 공항 이름을 key로 갈 수 있는 공항을 이름순 정렬.
# ICN출발하여 dfs로 모든 경우를 탐색하다가,
# 모든 경우를 탐색했다면 그것이 답이다. 바로 return (공항 이름순 정렬 했으므로 알파벳 우선이다)

# O(N^2)?? 제대로된 복잡도 분석을 하지 않음. 아마 N^2이지 않을까 예상 중임 (일반적인 dfs/bfs니깐.)

def solution(tickets):
    ticket_dict = dict()

    for departure, to in tickets:
        if departure not in ticket_dict:
            ticket_dict[departure] = [[to, 0]]
        else:
            ticket_dict[departure].append([to, 0])

    # 각 항공권 이름별 정렬
    for l in ticket_dict.values():
        l.sort()

    def dfs(departure, routine):
        routine.append(departure)

        # routine의 개수가 tickets+1와 같다면 모든 항공권을 다 쓴 것.
        # +1의 이유는 ICN에서 출발하니까.
        if len(routine) == len(tickets) + 1:
            return routine


        if departure not in ticket_dict:
            routine.pop()
            return None

        for ticket in ticket_dict[departure]:
            if ticket[1] == 0:
                ticket[1] = 1
                tmp = dfs(ticket[0], routine)

                if tmp != None:
                    return tmp

                ticket[1] = 0
        
        routine.pop()
        return None

    return dfs('ICN', [])


print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]))
print(solution([['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]))
