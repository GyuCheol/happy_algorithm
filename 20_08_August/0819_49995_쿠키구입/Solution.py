
def solution(cookie):
    answer = 0

    for sid in range(len(cookie) - 1):

        left = cookie[sid]
        left_id = sid
        right = cookie[sid + 1]
        right_id = sid + 1

        while True:

            if left == right:
                answer = max(answer, left)
            
            if left_id > 0 and left <= right:
                left_id -= 1
                left += cookie[left_id]
            elif right_id < (len(cookie) - 1) and right <= left:
                right_id += 1
                right += cookie[right_id]
            else:
                break

    return answer

print(solution([1, 1, 2, 3]))
print(solution([1, 1, 4, 5]))
print(solution([1, 2, 4, 5]))
print(solution([1, 1, 1, 1, 1, 99, 1, 1, 98]))
