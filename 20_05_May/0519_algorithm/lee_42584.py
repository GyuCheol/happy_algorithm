 

def solution(prices):
    answer = [0 for x in range(len(prices))]
    id_list = []

    for i, price in enumerate(prices):
        
        # id에 있는 리스트의 가격에 따라 값 추가,
        # 하락한 가격 제거
        for id in id_list[:]:
            answer[id] += 1
            
            if prices[id] > price:
                id_list.remove(id)

        id_list.append(i)


    return answer


print(solution([1, 2, 3, 2, 3]))
print(solution([1, 2, 3, 4, 5]))
print(solution([5, 5, 5, 5, 5]))
print(solution([3, 5, 2, 5, 1]))

