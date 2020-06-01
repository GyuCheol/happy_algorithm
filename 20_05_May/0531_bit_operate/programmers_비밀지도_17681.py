
# 프로그래머스 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681

prop = 0b1000_1000
# 30년전 S/W RAM 4kb


def solution(n, arr1, arr2):
    result = []

    for a, b in zip(arr1, arr2):
        tmp = a | b
        s = ''
        
        for i in range(n - 1, -1, -1):
            if tmp & (1 << i) != 0:
                s += '#'
            else:
                s += ' '
        
        result.append(s)

    return result


def solution2(n, arr1, arr2):
    result = []

    for a, b in zip(arr1, arr2):
        tmp = bin(a | b)[2:]
        
        result.append(tmp.replace('1', '#').replace('0', ' '))

    return result


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution2(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

bit = 0b1001_0001_0001
#   & 0b0000_0000_1000
# n 번째 1 << (n - 1) 0과 다른지 비교
bit & (1 << 3) != 0

#   & 0b0000_0000_1000
#                     
# 0b0000_0000_0001 << 1
# 0b0000_0000_0010

# 0b0000_0000_0001 << 2
# 0b0000_0000_0100

# &, |, ~, ^, <<, >>

a = 0b1100 # 12
b = 0b0011 # 3
c = a | b  # 0b1111 -> 15

print(f'{a}, {b}')



