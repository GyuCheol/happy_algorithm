# 7월 17일

# n진수 게임
# https://programmers.co.kr/learn/courses/30/lessons/17678
# 2018 카카오 블라인드 공채 3차 - lv2

# 진법 처리 + 문자열 처리 문제
# 게임이 진행되는 모든 경우를 문자열로 만든뒤
# 자신의 차례 문자열만 끄집어내기

# O(N)

chars = '0123456789ABCDEF'

def solution(n, t, m, p):
    saying = []

    i = 0
    l = 0

    # 진법 반환
    def get_n_digit(number):
        tmp = []

        while True:
            tmp.append(chars[number % n])

            number //= n

            if number == 0:
                break

        return ''.join(tmp[::-1])
        
    # t*m길이까지 l을 구한다.
    while l <= (t * m):
        n_digit = get_n_digit(i)
        saying.append(n_digit)
        i += 1
        l += len(n_digit)

    # 모든 경우가 있는 문자열 만듦
    cases = ''.join(saying)

    # p-1부터 시작해서 (문자열은 0이 시작)
    # 자기 차례인 m마다 말할 단어 구하고, t개까지 자르기
    return cases[p-1::m][:t]

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
