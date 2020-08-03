
def solution(gems):
    s = {g for g in gems}
    t = {g: 0 for g in s}
    start = 0
    end = 0
    cnt = 0
    min_start = 0
    min_end = len(gems)
    
    while end < len(gems):

        if cnt < len(s):
            if t[gems[end]] == 0:
                cnt += 1

            t[gems[end]] += 1
            end += 1
        
        while cnt == len(s):
            
            if (end - start) < (min_end - min_start):
                min_end, min_start = end, start

            if t[gems[start]] == 1:
                cnt -= 1

            t[gems[start]] -= 1
            start += 1
        
    return [min_start + 1, min_end] 


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

# expected [9:11]
print(solution(["A", "B", "A", "A", "C", "A", "A", "B", "A", "B", "C"]))
# expected [4:6]
print(solution(["A", "B", "B", "A", "B", "C", "A", "B", "A", "B", "C"]))
