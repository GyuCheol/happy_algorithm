# 7월 12일

# 소수찾기 - lv1
# https://programmers.co.kr/learn/courses/30/lessons/12921

# 에라토스테네스의 체 이용

# 시간 복잡도 O(NlogN)

def solution(n):
    numbers = [True for x in range(0, n + 1)]
    
    numbers[:2] = False, False
    i = 2
    
    # 소수 판별
    def is_prime(number):
        
        i = 2

        while (i*i) <= number:
            
            if number % i == 0:
                return False

            i += 1
        
        return True
    
    # n 제곱근까지 확인
    while (i*i) <= n:
        
        if is_prime(i):
            for j in range(i * 2, n + 1, i):
                numbers[j] = False
        
        i += 1
            
    
    return numbers.count(True)

# 다른 사람이 푼 pythonic 풀이
# 다만 자료구조 복사와 개체 연산이 발생해서 성능이 차이가 20~30% 차이남.
def solution2(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

print(solution(10))

from time import time

t = time()
print(solution(1000000))
print(time() - t)

t = time()
print(solution2(1000000))
print(time() - t)
