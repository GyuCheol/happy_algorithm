def solution(v):
    v.sort()

    # x1, y1, x2, y1, x1, y2, x2, y2
    # 이 중에서 없는 좌표 리턴하기

    if v[0][0] == v[1][0]:
        # x2, y1 필요
        return [v[2][0], v[]]
    elif:
        pass

    # 

    

    return answer

print(solution([[1, 4], [3, 4], [3, 10]]))
print(solution([[1, 1], [2, 2], [1, 2]]))