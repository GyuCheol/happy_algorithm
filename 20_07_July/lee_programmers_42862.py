# 7월 13일

# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862
# Greedy - lv1

# 체격 순으로 체육복을 빌려줄 수 있음.
# 딱히 어려운게 없을 줄 알았지만, 함정이 하나 있다.
# 여벌이 있지만, 도난까지 당한 친구들은 다른 친구한테 빌릴 수 있더라도
# 그냥 자신의 옷을 사용한다는 것.
# 그 경우만 처음에 초기화할 때 신경쓰면 된다.

# 시간 복잡도 O(N)

def solution(n, lost, reserve):
    # if문 경계 처리 편의성을 위해 앞뒤로 1개씩 추가하자..
    states = [1 for x in range(n + 2)]

    # 경계 부분은 체육복을 받을 수 없으므로 2 처리
    states[0] = 2
    states[n + 1] = 2

    # 도난 당한 친구들
    for l in lost:
        states[l] -= 1

    # 여벌이 있는 친구들
    for r in reserve:
        states[r] += 1

    lost_cnt = states.count(0)

    for i in range(1, n + 1):
        # 도난 당하지 않고, 여벌이 있는 친구
        if states[i] == 2:
            
            # 앞뒤로 빌릴 수 있는 경우를 본다.
            # 순차적으로 진행하므로 앞쪽(-1)부터 보는 것이 최적의 경우
            if states[i-1] == 0:
                lost_cnt -= 1
                states[i] = 1
                states[i-1] = 1
            elif states[i+1] == 0:
                lost_cnt -= 1
                states[i] = 1
                states[i+1] = 1

    
    return n - lost_cnt

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(3, [3], [1]))
print(solution(8, [6], [4, 5]))
