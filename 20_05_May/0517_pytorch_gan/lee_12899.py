

def solution(n):
    answer = ''

    while n > 0:
        tmp = n % 3
        n //= 3

        if tmp == 0:
            n -= 1
            answer += '4'
        else:
            answer += str(tmp)

    return answer[::-1]

print(solution(10))
