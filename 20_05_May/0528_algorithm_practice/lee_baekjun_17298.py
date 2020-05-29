
# stack 응용 문제 : 오큰수
# https://www.acmicpc.net/problem/17298

# 시간복잡도 O(n)안에 해결해야함. 최대 N크기 1,000,000
# >> 으로 숫자를 확인해가며 스택에 있는 수를 소거해가며 오큰수 찾기


n = int(input())
numbers = list(map(int, input().split(' ')))
stack = []
result = [0] * n

for i, number in enumerate(numbers):

    # 스택에 아이템이 있는 경우
    # 현재 숫자가 오큰수가 되는지 검사 후 추가
    while stack:
        top = stack.pop()
        
        if number > numbers[top]:
            # 오큰수 찾은 경우
            # result에 기록 후 다음 stack 요소도 검사
            result[top] = number
        else:
            # 못 찾은 경우, stack의 다른 수를 볼 필요 없으므로 loop break
            stack.append(top)
            break
        

    # 오큰수를 찾기 위해 스택에 추가
    stack.append(i)

# stack에 남은 값들은 오큰수가 없으므로
# 모두 -1로 초기화
while stack:
    result[stack.pop()] = -1

# 오큰 수 모두 출력
for number in result:
    print(number, end=' ')
