# 7월 16일

# 행렬의 곱셈
# https://programmers.co.kr/learn/courses/30/lessons/12949
# lv 2

# arr1의 내용을 돌면서 arr2 내용을 곱한 결과를 더해야 한다.
# 1줄 list comprehension으로 하려 했는데 가독성 문제가 넘 심하다.

# 시간 복잡도 O(N^3) ?

def solution(arr1, arr2):
    l = len(arr1)
    m = len(arr1[0])
    n = len(arr2[0])
    
    assert m == len(arr2)
    tmp = [[0 for j in range(n)] for i in range(l)]

    for i in range(l):
        for j in range(n):
            tmp[i][j] = sum([arr1[i][k] * arr2[k][j] for k in range(m)])

    return tmp
    # 1줄 코딩
    # return [[sum([arr1[i] [k] * arr2[k][j] for k in range(len(arr2))]) for j in range(len(arr2[0]))] for i in range(len(arr1))]

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))

print(solution([[1, 1], [1, 1]], [[1, 1], [1, 1]]))
print(solution([[1, 4]], [[1, 1], [1, 1]]))
print(solution([[1, 4, 5]], [[1, 1], [1, 1], [1, 1]]))