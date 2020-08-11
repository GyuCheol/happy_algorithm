def solution(s):
    answer = 0

    # tmp의 왼쪽, 오른쪽 대칭 검사
    def check(s, start, end):

        l = (end - start) // 2

        for i in range(l):

            if s[start + i] != s[end - 1 - i]:
                return False

        return True

    for i in range(len(s)):

        # 적어도 answer보다 큰 경우만 찾아야한다.
        for j in range(answer + 1, len(s) - i + 1):
            if check(s, i, i + j):
                answer = j
    
    return answer

print(solution("zxcvaaaa"))
print(solution('abcdcba'))

print(solution("abacde"))

print(solution("aaaa"))
