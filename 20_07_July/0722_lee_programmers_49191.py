# 7월 22일

# 순위
# https://programmers.co.kr/learn/courses/30/lessons/49191
# 그래프 - lv3

# 예전 lv3 레벨 테스트 때 풀었던 문제
# 승리, 패배에 대해 그래프로 연결된 구조에서 연관이 있을 때마다 추가로 저장하여야 한다.
# 1번이 2를 이겼음, 1번이 3번에게 졌음 ---> 2번도 3번에게 진다는 뜻. 1번에게 지는 상대를 찾아 모조리 3번에게 졌다고 마킹해야함

# 1] 먼저 모든 결과를 graph에 저장
# 2] 2중 루프돌며, result 결과 토대로 다른 예상이 가능한 정보 처리
# 3] 각 graph row별 자신을 제외한 n-1만큼의 성적이 있는 경우 순위를 계산할 수 있다.

# O(N^3)

def solution(n, results):
    # 패를 기록할 그래프 배열 생성
    # graph[1][2] = 1이라는 뜻은, 1번은 2번한테 항상 이긴다는 의미
    # graph[3][2] = -1이라는 뜻은, 3번은 2번한테 졌다는 의미
    # 경계 처리 편의상 +1씩 더 생성함
    graph = [[0 for j in range(n+1)] for i in range(n+1)]
    
    # 모든 결과 등록
    for a, b in results:
        graph[a][b] = 1
        graph[b][a] = -1

    # 결과를 토대로 다른 값에 승, 패 여부 마킹
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            
            # a > b인 경우
            if graph[a][b] == 1:
                # b의 승리 결과를 반영
                for i in range(1, n + 1):
                    if graph[b][i] == 1:
                        graph[a][i] = 1
                        graph[i][a] = -1
            
            # a < b의 경우
            if graph[a][b] == -1:
                # a가 이긴 것들을 b도 이길 수 있음
                for i in range(1, n + 1):
                    if graph[a][i] == 1:
                        graph[b][i] = 1
                        graph[i][b] = -1


    # 승부가 결정 안난 값이 자기 자신인 레코드만 조회하면 된다. (0번째 배열은 항상 0이므로 -1)
    return sum([1 if row.count(0)-1 == 1 else 0 for row in graph])

# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
# print(solution(5, [[1, 2], [1, 3], [1, 4], [5, 1]]))
# print(solution(5, [[1, 2], [1, 3], [5, 1], [4, 5]]))
# print(solution(5, [[5, 1], [4, 5], [1, 2], [1, 3]]))
# print(solution(5, [[4, 5], [5, 1], [1, 3], [1, 2]]))
# print(solution(5, [[1, 2], [1, 3], [1, 4]]))
# print(solution(5, [[5, 1], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]))
print(solution(5, [[2, 3], [3, 4], [5, 1], [1, 2], [1, 3], [1, 4]]))
