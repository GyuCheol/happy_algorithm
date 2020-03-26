

def solution(heights):
    answer = []
    queue = []

    for height, idx in zip(heights, range(len(heights))):
        receiver = 0

        for (h, id) in queue:
            if h > height:
                receiver = id
                break

        answer.append(receiver)

        if len(queue) > 0 and height >= queue[len(queue) - 1][0]:
            queue = [(height, idx + 1)]
        else:
            queue.insert(0, (height, idx + 1))


    return answer

print(solution([6,9,5,7,4]))
print(solution([3,9,9,3,5,7,2]))
print(solution([1,5,3,6,7,6,5]))
