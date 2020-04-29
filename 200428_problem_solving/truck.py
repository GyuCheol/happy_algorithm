from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_q = deque(truck_weights)
    trucks_on_bridge = []
    answer = 0

    while len(truck_q) > 0 or len(trucks_on_bridge) > 0:
        answer += 1

        # 다리 위 트럭의 위치를 1씩 변경
        for truck in trucks_on_bridge:
            truck[1] += 1

        # 다리 위를 지나지 않은 트럭만 남김. Filtering
        trucks_on_bridge = [x for x in trucks_on_bridge if x[1] <= bridge_length]

        # 대기 중인 트럭이 있는 경우에만
        if len(truck_q) > 0:
            t = truck_q.popleft()
            cur_weight = sum([x[0] for x in trucks_on_bridge])

            # Queue에서 꺼낸 트럭의 무게를 견딜 수 있다면
            if weight >= cur_weight + t:
                # 다리 위 트럭을 저장하는 자료구조에 추가 [트럭 무게, 트럭 위치]
                trucks_on_bridge.append([t, 1])
            else:
                # 트럭이 다리로 추가될 수 없으니까 다시 Queue 맨 앞에 추가
                truck_q.appendleft(t)

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
