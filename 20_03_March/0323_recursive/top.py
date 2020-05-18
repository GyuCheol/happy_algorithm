

def solution(heights):
    # [7, 6, 6, 7, 3]
    answer = [0]

    # 모든 탑에 대한 루프
    for i in range(1, len(heights)):
        
        received = 0

        # i에서 왼쪽으로 가면서 나보다 큰 수신탑 찾기
        for j in range(i - 1, -1, -1):
            # 나보다 큰 탑을 찾은 경우
            if heights[j] > heights[i]:
                received = j + 1 # 탑 번호는 1부터 시작이니 +1
                break

        answer.append(received)

    return answer

print(solution([7, 6, 6, 7, 3]))


print(list(range(3))) # -> ? [0, 1, 2]
print(list(range(3, 5, 1))) # -> ? [3, 4]
print(list(range(3, 9, 2))) # -> ? [3, 5, 7]
print(list(range(3, 0, -1))) # -> ? [3, 2, 1]
print(list(range(0, -1, -1))) # -> ? []
print(list(range(-1, -1, -1))) # -> ? []


for(int j = i - 1; j >= 0; j--) {
}