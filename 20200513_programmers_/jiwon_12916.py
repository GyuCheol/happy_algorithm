def solution(s):
    answer = False
    p = s.count('p')+s.count('P')
    y = s.count('y')+s.count('Y')
    
    if (p == y):
        answer = True
    
    return answer

print(solution('pPoooyY'))
print(p,y)