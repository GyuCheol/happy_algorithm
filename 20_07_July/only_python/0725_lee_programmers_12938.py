# 7월 25일

# 최고의 집합
# https://programmers.co.kr/learn/courses/30/lessons/12938
# 연습문제 - lv3

# 

# O(NlogN)

def solution(n, s):
    tmp = [0 for x in range (1, n + 1)]

    if (1 * n) >= s:
        return [-1]
    
    # val만큼 값 추가해야함
    val = s

    # 잉여 값을 다 맞출 때 까지 순회
    while val > 0:
        
        # 길이보다 크면 골고루 나눠 줄 수 있음.
        if val >= len(tmp):
            div = val // n
            val -= div * n

            for i in range(n):
                tmp[i] += div
        else:
            # 작으면 끝에서 val길이까지만 1씩 나눠주기
            id = len(tmp) - 1
            while val > 0:
                tmp[id] += 1
                id -= 1
                val -= 1
            
    return tmp
                
        


print(solution(5, 30))
print(solution(10, 30))
print(solution(10, 100))
print(solution(2, 9))
print(solution(2, 8))
print(solution(3, 9))
# print(solution(10000, 500005000))
