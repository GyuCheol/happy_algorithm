
# F5 Debug
# Ctrl + F5 Run
# F9 Toggle Breakpoint
# F10 Step Over
# F11 Step Into

def solution(participant, completion):
    participant.sort() # O(N * log2N)
    completion.sort() # O(N * log2N)
    
    for par, com in zip(participant, completion): # O(N)
        if par != com:
            return par

    return participant[-1]




print(hash('a'))
print('a'.__hash__())

assert solution2(['a', 'b', 'c'], ['a', 'b']) == 'c'
assert solution2(['a', 'b', 'c', 'c', 'd'], ['a', 'b', 'c', 'd']) == 'c'
assert solution2(['a', 'b', 'c', 'c', 'c', 'd', 'd'], ['a', 'b', 'c', 'c', 'c', 'd']) == 'd'

# 소스를 숨기기 위한 것
# 특정 수치화 되지 않은 값을 숫자로 변환하기 위해서도 사용

# __ private
# print('askjdhaskdjh'.__hash__()) # 1333...

# d[1001]
# print('aa'.__hash__() % 1001)
# d = {}
# d['a'] = True

# print(d['a']) # O(1)


