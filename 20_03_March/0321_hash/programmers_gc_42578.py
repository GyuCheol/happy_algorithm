from collections import Counter
from functools import reduce

def solution(clothes):
    counter = Counter([t for n, t in clothes])
    
    return reduce(lambda x, y: x * (y + 1), counter.values(), 1) - 1

print(solution([["a", "e"], ["b", "e"], ["c", "e"], ["d", "t"]]))
print(solution([["a", "b"], ["b", "c"], ["c", "c"]]))
print(solution([["a1", "e"], ["a2", "e"], ["b1", "t"], ["b2", "t"], ["c1", "b"], ["c2", "b"]]))