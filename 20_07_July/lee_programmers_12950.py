# 7월 13일

# 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950
# lv 1

# 2개 행렬을 더해서 반환하는 문제
# comprehension을 이용한 좋은 풀이인듯?
# 근데 가독성은... ?

# 시간 복잡도 O(N^2)

def solution(arr1, arr2):
    
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[i]))] for i in range(len(arr1))]