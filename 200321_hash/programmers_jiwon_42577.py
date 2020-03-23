
def solution(phone_book):
    answer = True
    len_pb = len(phone_book)

    for i in range(len_pb):
        for j in range(len_pb):
            if phone_book[j].startswith(phone_book[i]):
                answer = False
                return answer
    return answer

print(solution(['119', '123', '11945123']))
