# 6월 16일

# 8진수 > 2진수
# https://www.acmicpc.net/problem/1212
# 진법 변환 단순한 수학 문제. 1자리를 2로 3번 나누어서 결과를 처리
# 귀찮아서 걍 bin 함수처리

octal = input()
l = []

for ch in octal:
    # 앞에 0b 짜르기 위함
    binary = bin(int(ch))[2:]

    # 3자리 맞게 출력하기 위해 0 padding 추가 (1 -> 001)
    l.append('0' * (3 - len(binary)))
    l.append(binary)

# 결과값 합치기
answer = ''.join(l)

# 숫자는 반드시 0이 아닌 수로 시작해야함 2진수므로 index로 문자 '1' 찾기
index = -1

for id, ch in enumerate(answer):

    if ch == '1':
        index = id
        break


# 못찾으면 값이 0임
if index == -1:
    print(0)
else:
    print(answer[index:])

