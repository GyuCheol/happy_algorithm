# number = input()
# n = []
# for _ in range(number):
#     n.append(list(map(int,input().split())))
# #n = [(x,y) for x in range(number) for y in range(number)]
# n = sotred(n, key = lambda x:(x[0])

number = int(input())
case = []
for i in range(number):
    x= list(map(int,input().split(' ')))
    case.append(x)

new_case= sorted(case)
new_case = case.sort(key = lambda x : x[0])
print(new_case)
