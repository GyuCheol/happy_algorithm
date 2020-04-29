from collections import Counter

def solution(participant, completion):
    counter_p = Counter(participant)
    counter_c = Counter(completion)
    print(counter_p)
    for p in counter_p:
        if p not in counter_c or counter_p[p] != counter_c[p]:
            return p

def solution2(participant, completion):
    id = sum([hash(p) for p in participant]) - sum([hash(c) for c in completion])

    for p in participant:
        if id == hash(p):
            return p

solution(['A', 'B', 'B', 'C'], ['A', 'B', 'C'])

