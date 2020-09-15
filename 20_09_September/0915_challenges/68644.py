from itertools import combinations

def solution(numbers):
    num_set = set()
    
    for com in combinations(numbers, 2):
        num_set.add(sum(com))
    
    
    return sorted(num_set)

print(solution([2, 1, 3, 4, 1]))

print(solution(	[5, 0, 2, 7]))