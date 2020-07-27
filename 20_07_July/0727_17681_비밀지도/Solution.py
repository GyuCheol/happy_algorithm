
def solution(n, arr1, arr2):
    result = []

    for a, b in zip(arr1, arr2):
        tmp = a | b
        s = []
        
        for i in range(n):
            s.append('#' if tmp % 2 == 1 else ' ')
            tmp //= 2
        
        result.append(''.join(s[::-1]))

    return result


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
