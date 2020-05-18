# 1) Counter
# 2) sum hash(x)

from collections import Counter

# def solution(participant, completion):
#     p = sum(hash(x) for x in participant)
#     c = sum(hash(x) for x in completion)

#     missing = p-c
#     for i in participant:
#         if hash(i) == missing:
#             return i

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)

    for name,count in p.items():
        if name not in c or count != c[name]:
            return name














# def solution(participant, completion):
#     p = Counter(participant)
#     c = Counter(completion)


    

