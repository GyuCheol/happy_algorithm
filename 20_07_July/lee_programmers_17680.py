# 7월 17일

# 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680
# 2018 카카오 블라인드 공채 1차 - lv2

# LRU 알고리즘 문제
# queue 구조로 쉽게 풀 수 있다.
# cacheSize만큼 찼다면 queue 젤 앞에 있는걸 빼주면서 진행.
# 시간 복잡도 효율을 위해 set 구조도 같이 사용하여야 한다.

# 다른 사람의 풀이를 보면 deque의 maxlen을 주는 것을 볼 수 있다.
# 또 set도 쓰지 않았는데 cache의 크기가 최대 30이라 큰 비용 차이가 없어서
# 그런거 같다. cache 크기가 10,000까지 갔더라면 set을 쓰는게 이득이었을 것임.

# O(N)

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

        # cache에 있는 경우
        if name in s:
            cost += 1
            # 이름을 deq의 끝에 올리기 위해 기존 이름 제거
            deq.remove(name)
        else:
            # cache에 없으므로 비용 큼
            cost += 5

            # cache가 가득차면 맨 앞 요소 제거
            if len(deq) == cacheSize:
                # set에서도 제거
                s.remove(deq.popleft())
            
            # 현재 값 set에 기록
            s.add(name)

        # LRU queue에 추가
        deq.append(name)

    return cost

print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(5, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))
print(solution(0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))