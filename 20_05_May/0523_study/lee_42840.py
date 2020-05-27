student_answer = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
]
    
def solution(answers):
    answer = []
    marks = [0, 0, 0]

    for i, answer in enumerate(answers):

        for id, a in enumerate(student_answer):
            length = len(student_answer[id])

            if answer == student_answer[id][i % length]:
                marks[id] += 1

    max_mark = max(marks)

    return [id for mark, id in zip(marks, [1, 2, 3]) if mark == max_mark]


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))