

def solution2(participant, completion):
    d = {}

    for p in participant: # O(N)
        if p in d:
            d[p] = d[p] + 1
        else:
            d[p] = 1
    
    for com in completion: # O(N)
        d[com] = d[com] - 1

    for name, v in d.items(): # O(N)
        if v == 1:
            return name

def solution(participant, completion):
    left_hash = sum([hash(x) for x in participant]) - sum([hash(x) for x in completion])

    for p in participant:
        if hash(p) == left_hash:
            return p

