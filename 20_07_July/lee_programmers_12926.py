# 7월 13일

# 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926

# @.@ 설명 생략

# 시간 복잡도 O(N)

def solution(s, n):
    answer = []

    for ch in s:
        # 알파벳인 경우
        if 'a' <= ch <= 'z':
            tmp = (ord(ch) - 97) + n
            answer.append(chr(97 + (tmp % 26)))
        elif 'A' <= ch <= 'Z':
            tmp = (ord(ch) - 65) + n
            answer.append(chr(65 + (tmp % 26)))
        else:
            answer.append(ch)

    return ''.join(answer)


print(solution('z', 1))
