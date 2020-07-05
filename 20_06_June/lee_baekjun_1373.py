# 6월 16일

# 2진수 > 8진수
# https://www.acmicpc.net/problem/1373
# 2진수 3자리가 8진수 1자리가 되므로, 문자열을 3개씩 짤라서 8진수 결과 값 이어 붙이는 문제

binary = input()

val = 0
ex = 0
answer = ''

# 3자리씩 누적
# 루프 역순회 (뒤에서부터 읽어야하므로)
for ch in binary[::-1]:
    
    val += int(ch) * (2 ** ex)
    ex += 1

    if ex == 3:
        answer += str(val)
        ex = 0
        val = 0


# 남은 값 있다면 추가
answer += str(val)

# 다시 뒤집음
answer = answer[::-1]

# 0이 아닌 첫번째 위치 찾기
index = 0
for id, ch in enumerate(answer):
    if ch != '0':
        index = id
        break

# 해당 위치부터 출력
print(answer[index:])

