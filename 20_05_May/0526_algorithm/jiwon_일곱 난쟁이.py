# heights = list(map(int,input().split(' '))
# map은 일렬데이터 입력시
heights = []
for i in range(9):
    heights.append(int(input()))

total = sum(heights)


def solution():
    for i in range(len(heights)):
        for j in range(1,len(heights)):
            if total-(heights[i]+heights[j]) == 100:
                tmp1,tmp2 = heights[i], heights[j]
                heights.remove(tmp1)
                heights.remove(tmp2)
                
                print(i,j)
                return heights

solution()
heights.sort()

print(heights)

#tmp = heights[:]
#tmp1, tmp2
#tmp.remove(tmp1)
#tmp.remove(tmp2)
#sum(tmp) == 100:

# 전체합- (2개 합) 이 간편.
# 7개합하려면 for 3중문에 if k != i and k != j : a.append(k)