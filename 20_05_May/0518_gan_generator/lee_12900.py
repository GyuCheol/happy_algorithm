
# 단순 피보나치 수열
def solution(n):
    a, b = 1, 1
    
    for _ in range(n - 1):
        a, b = b, (a + b) % 1000000007

    return b

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))

