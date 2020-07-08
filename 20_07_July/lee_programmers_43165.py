
# 7월 8일

# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165
# DFS - lv2

# DFS(재귀호출)을 이용하여 모든 경우를 순회하면 된다.
# 시간 복잡도 O(2^n)

def solution(numbers, target):
    l = len(numbers)

    # 모든 숫자를 다 이용했다면, target과 검사하여 비교
    def dfs(cur, num):

        if cur == l:
            return 1 if num == target else 0
        
        return dfs(cur + 1, num + numbers[cur]) + dfs(cur + 1, num - numbers[cur])
        

    return dfs(1, numbers[0]) + dfs(1, -numbers[0])

print(solution([1, 1, 1, 1, 1], 3))