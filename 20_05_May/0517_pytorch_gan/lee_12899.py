# https://programmers.co.kr/learn/courses/30/lessons/12899

def reverse(l):

    for n in range(len(l) - 1, -1, -1):
        yield l[n]

def solution(n):
    answer = []

    while n > 0:
        tmp = n % 3
        n //= 3

        # 3진법이지만, 0을 자릿수로 쓰지 않음
        # 그러므로 3으로 나누어 떨어지는 구간에 4를 표시
        if tmp == 0:
            n -= 1
            answer.append('4')
        else:
            answer.append(str(tmp))

    return ''.join(reverse(answer))

print(solution(10))
