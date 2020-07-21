# 7월 21일

# 단속카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884
# Greedy - lv3

# routes 경로 순으로 정렬 (pop하기 위해 역순)
# routes에 있는 모든 자동차를 해결할 때 까지 순회
# routes에 있는 것을 pop하며 경로가 겹친다면 계속 진행
# 등록된 다른 경로와의 연관이 없다면, 현재 위치에 하나 설치해야함.
# 설치하고, 등록된 모든 차 경로 제거
# routes의 모든 차를 없앨 때까지 반복

# O(NlogN) 정렬하고 N만큼 순회했으니.

def solution(routes):
    routes.sort(reverse=True)
    
    def is_included(route):

        for r in registed_routes:
            # route가 등록된 경로들 중 하나라도 겹치지 않는다면 
            # route의 시작점이 등록된 다른 경로의 끝점보다 크면 X
            if route[0] > r[1]:
                return False

        return True

    registed_routes = [routes.pop()]
    # 최소 1개는 필요
    answer = 1

    while routes:
        route = routes.pop()

        # 현재 등록된 모든 경로와 겹칠 수 있는가?
        if is_included(route) == False:
            # 카메라 설치 필요
            answer += 1
            # 설치 후 다른 경로 제거 (이미 커버했으므로)
            registed_routes.clear()
        
        registed_routes.append(route)
        
    return answer

# print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
print(solution([[-20, 15], [-14, -5], [-18, -13], [-18, -9], [-5, -3]]))