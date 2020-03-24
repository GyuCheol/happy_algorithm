

def solution(n, f, t, tmp):

    if n == 1:
        print(f, '->', t)
        return

    solution(n - 1, f, tmp, t) # 자기 자신의 윗 원반을 tmp 이동
    print(f , '->', t) # 
    solution(n - 1, tmp, t, f)

solution(5, 'A', 'C', 'B')


# F(0) = 0
# F(1) = 1
# F(2) = F(1) + F(0) = 1
# F(3) = F(2) + F(1) = F(1) + F(0) + F(1) = 2
# F(4) = F(3) + F(2) = F(2) + F(1) + F(1) + F(0)


def solution2(n):
    if n == 0 or n == 1:
        return n

    return solution2(n-2) + solution2(n-1)

print(solution2(10))

# 17
# 1
# 7
# 17
# 71

# 011
# 0 -> 01 -> 011
# 1 -> 10 -> 101


# A -> 123
# B -> 999
# ZUI -> 123

# 2 ^ 512  
# NP문제 O() P문제 O(N^2)
# MD5 128bit 2^128
# SHA256

# hash_table [11]
# A -> 12000 -> 10번째에 저장 -> 
# B -> 13000 -> 10 -> 그 다음 노드에 저장
# 링크드 리스트
#+!+!+1+!

# hash_table [10]
# A -> 100 % 11

