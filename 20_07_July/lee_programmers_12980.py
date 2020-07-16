# 7월 16일

# 점프와 순간이동
# https://programmers.co.kr/learn/courses/30/lessons/12980
# Summer/Winter Coding (2018) lv 2

# n을 0으로 만들면 된다.
# 2로 나뉘어지면 나누고 안되면 -1
# 이것을 반복하면 답이 나올것이다? so simple!

# 다른 사람 풀이를 보면 2진으로 변환해서 1을 개수를 센다 오우.
# 결국 2를 계속 나누어서 확인하는 과정도 이와 비슷하다는 것을 깨닫.

# 시간 복잡도 O(logN)

def solution(n):
    ans = 0
    
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1

    return ans

print(solution(5))
print(solution(6))
print(solution(5000))