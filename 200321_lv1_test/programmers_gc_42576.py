from collections import Counter

def solution2(participant, completion):
    par_map = Counter([p for p in participant]) # O(N)
    comp_map = Counter([p for p in completion]) # O(N)
    
    for name, v in par_map.items(): # O(N)
        if name not in comp_map or v != comp_map[name]:
            return name

def solution(participant, completion):
    left_hash = sum([hash(x) for x in participant]) - sum([hash(x) for x in completion])

    for p in participant:
        if hash(p) == left_hash:
            return p


assert solution2(['a', 'b', 'c'], ['a', 'b']) == 'c'
assert solution2(['a', 'b', 'c', 'c', 'd'], ['a', 'b', 'c', 'd']) == 'c'
assert solution2(['a', 'b', 'c', 'c', 'c', 'd', 'd'], ['a', 'b', 'c', 'c', 'c', 'd']) == 'd'
