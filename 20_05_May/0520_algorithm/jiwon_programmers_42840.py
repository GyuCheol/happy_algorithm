a = [1,2,3,4,5]
b = [2,1,2,3,2,4,2,5]
c = [3,3,1,1,2,2,4,4,5,5]

def solution(answers):
    answers = []

    count = 0
    mark = [0,0,0]

    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            mark[0] += 1
        if answers[i] == b[i%8]:
            mark[1] += 1
        if answers[i] == c[i%10]:
            mark[2] += 1

    max_mark = max(mark)
    return [id + 1 for (mark, id) in zip(marks, range(3)) if mark == max_mark]



answer_1 = [1, 2, 3, 4, 5]
answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    answer = []
    marks = [0, 0, 0]

    # range(5) = 0, 1, 2, 3, 4, 5, 6, 7

    for i in range(len(answers)):
        
        if answers[i] == answer_1[i % 5]:
            marks[0] += 1
        
        if answers[i] == answer_2[i % 8]:
            marks[1] += 1

        if answers[i] == answer_3[i % 10]:
            marks[2] += 1

    max_mark = max(marks)

    return [id + 1 for (mark, id) in zip(marks, range(3)) if mark == max_mark]


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))