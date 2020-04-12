
n = int(input())

# 3 (range(n) -> 0, 1, 2)
# () # tuple
# [] # list
# {} # Set or Dict

points = [
    tuple(map(int, input().split(' '))) 
    for i in range(n)
]

# 사본 생성X
# 자기 자신의 메모리가 정렬
# points.sort()

# 사본을 만들어서 해당 사본 메모리가 정렬
sorted_list = sorted(points)

print(points)


# 3 5