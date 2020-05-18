

arr = [1, 2, 2, 3, 0, 2]

for i in arr:
    print(i, i + 1)

result = [arr[0]]

for i in range(1, len(arr)):
    
    if arr[i -1] != arr[i]:
        result.append(arr[i])

print(result)

# range 수열의 iterator를 만드는 함수

range(5) # 0, 1, 2, 3, 4 인자가 1개라면 start 0
# [0, 1, 2, 3, 4] -> 이걸 만드는게 아님!!

range(1, 5) # 2개라면, 첫번째 인자가 start 1, 2, 3, 4

range(1, 10, 2) # 3번째 인자는 interval이 되어서 1, 3, 5, 7, 9

print(list(range(5))) # [0, 1, 2, 3, 4] 이것이 배열을 만드는 것!
print(range(5))

# iterator? 

for i in range(100000): # start 0, 100000, 1씩 증가 숫자만 반복해주는 메모리 낭비 XX
    print(i)

for i in list(range(100000)): # 10만개의 숫자를 만듦
    print(i)

