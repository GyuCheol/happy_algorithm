
# https://www.acmicpc.net/problem/2309

height_list = []

for i in range(9):
    height_list.append(int(input()))

total_height = sum(height_list)

# flag, 함수로 return

def solution():

    for i in range(9):
        for j in range(i + 1, 9):
            if total_height - (height_list[i] + height_list[j]) == 100:
                tmp1, tmp2 = height_list[i], height_list[j]
                height_list.remove(tmp1)
                height_list.remove(tmp2)
                return

solution()

height_list.sort()

for height in height_list:
    print(height)

# O(N^2) -> N * (N-1) / 2 -> O(N^2)

# 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 -> 36