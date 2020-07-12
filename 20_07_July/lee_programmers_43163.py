# 7월 12일

# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163
# DFS/BFS - lv3

# BFS를 이용하면 된다.
# begin에서부터 queue에 가능한 다음 단어를 쌓고, (단어와 step)
# target에 도달할 때까지
# 도달하지 못하면 0을 리턴
# 사용 자료구조
# Queue : BFS 진행용
# Set : 단어 처리 (거쳐간 단어인지?)

# 시간 복잡도 O(N^2)

from collections import deque

def solution(begin, target, words):
    q = deque()
    s = set()

    q.append((begin, 1))
    
    if begin in s:
        del s[begin]

    # a에서 b로 이동가능한지?
    def can_move(a, b):
        cnt = 0

        for ch1, ch2 in zip(a, b):
            if ch1 != ch2:
                cnt += 1
        
        return cnt == 1
            

    # q에 요소가 있다면
    while q:
        word, step = q.popleft()

        # 1걸음만에 도달 가능한 words 찾기
        for w in words:

            if can_move(word, w):
                if w == target:
                    return step
                elif w not in s:
                    # 거쳐가지 않은 경우에만 queue에 추가
                    q.append((w, step + 1))
                    s.add(w)

    # q에 요소가 비었으므로 도달 못함 0 리턴
    return 0

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))
