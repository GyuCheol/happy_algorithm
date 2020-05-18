set1 = {} # 공집합 일 때 immutable 추가 불가능
set2 = set() # mutable -> 요소 추가, 변경, 삭제 가능!



n = int(input())
numbers = list(map(int, input().split(' ')))

s = set(numbers)
sorted_numbers = sorted(s)

print(sorted_numbers)

# 키가 171, 171, 171, 173, 173, 173, 175, 175, 175 ~~
# 어떤 키만 있는지? (171, 173, 175)
# Dictionary
# '171cm' : 100
# '173cm' : 67
