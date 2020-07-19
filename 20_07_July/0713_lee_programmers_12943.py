# 7월 13일

# 콜라츠 추측
# https://programmers.co.kr/learn/courses/30/lessons/12943
# lv 1

# O.o

# 시간 복잡도 O(logN)

def solution(num):
    answer = 0
    
    while num > 1:
        
        answer += 1

        if num % 2 == 0:
            num //= 2
        else:
            num *= 3
            num += 1
        
        if answer > 500:
            return -1
    
    return answer