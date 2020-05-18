
def solution(citations):
    
    citations.sort(reverse=True)
    length = len(citations)
    
    for x in range(length, 0, -1):
        for id, value in enumerate(citations):
            if value >= x and x == (id + 1):
                return x
    
    return 0

print(solution([6, 6, 6])) # 3
print(solution([6])) # 1
print(solution([0])) # 0
print(solution([2, 2, 2, 2])) # 2
print(solution([2, 2, 2, 2])) # 3
