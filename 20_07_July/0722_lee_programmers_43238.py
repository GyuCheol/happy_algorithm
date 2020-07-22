# 7월 22일

# 입국 심사
# https://programmers.co.kr/learn/courses/30/lessons/43238
# 이분 탐색 - lv3

# 심플한 queue 스러운 문제
# 다만 n 크기가 너무커서 queue로 한사람 한사람 처리하려고 하면? Time-out (10억이다..)
# 시간 복잡도가 NlogN 이하로 처리되어야할 문제. (크기가 총 100,000) logN, N, NlogN 등
# 바로 보이는 최소 값은 times가 가장 작은 심사관과 n명을 처리하는 경우이다.
# 이 경우에서 부터 조금 더 작은 경우가 처리되는지를 확인하면 될 것이다.

# 처리가 가능하다는 로직은 각 time 가지고 n을 나눈 값의 합이 n에 도달하면 된다.

# 다른 사람의 힌트를 살짝 참고했다.
# 특정 시간이 처리 가능한지 가능하지 않은지 검사하는 로직
# 그리고 처음으로 처리 가능한 시간
# 이것으로 범위를 점점 더 좁혀나가면 되는 문제이다.
# 반대로 정답에서 이것이 정답이 맞는가? 를 작성해야하는 유형도 생각하자.
# 이때 정답이 맞는가?를 최대한 효율적이게. 이분 탐색 같은.

# O(NlogN)

def solution(n, times):
    # 적어도 가장 빠른 심사관이 n명씩 처리하는게 일단은 가능하다.
    end = n * min(times) * 2
    start = 1
    answer = (start + end) // 2

    # 2개가 같으면 모두 탐색한 것이다.
    while True:
        tmp = n
        target = (start + end) // 2
        # 처리가 가능한지 검사한다.
        for time in times:
            tmp -= target // time
        
        # tmp가 음수가 되면 오버한 시간이므로
        # 탐색 범위 좁히기
        if tmp <= 0:
            # tmp가 0보다 작으면 일단은 가능한 경우이다.
            answer = min(answer, target)
            end = (start + end) // 2
        else:
            # tmp가 양수가 되면 start로 좁혀야함.
            # 이미 start가 좁힐 수 없는 상태라면 break
            if start == (start + end) // 2:
                break
                
            start = (start + end) // 2

    return answer

print(solution(6, [7, 10]))
#print(solution(5, [1, 5]))


