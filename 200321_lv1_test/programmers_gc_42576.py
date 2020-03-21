

def solution(participant, completion):
    d = {}

    for p in participant: # O(N)
        if d.__contains__(p):
            d[p] = d[p] + 1
        else:
            d[p] = 1
    
    for com in completion: # O(N)
        d[com] = d[com] - 1

    for name, v in d.items(): # O(N)
        if v == 1:
            return name
