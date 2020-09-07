def solution(N, stages):
    # 실패한 유저 수
    fail = [0] * (N + 1)
    answer = []
    
    for stage in stages:
        if stage <= N:
            fail[stage] += 1
    
    user_cnt = len(stages)

    for i in range(1, len(fail)):
        if user_cnt > 0:
            answer.append((-(fail[i] / user_cnt), i))
            user_cnt -= fail[i]
        else:
            answer.append((0, i))
    
    
    return [n[1] for n in sorted(answer)]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4 , 4, 4, 4]))
