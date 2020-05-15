def solution(arr):
    new_list = []
    new_list.append(arr[0])

    # 0, 1, 2, 3, 4, 5 X
    # 1, 1, 2, 2, 0, 3 O
    for i in range(1, len(arr)):

        if arr[i-1] != arr[i]: 
            new_list.append(arr[i])
    
    return new_list

print(solution([1,1,2,2,0,3]))

#for i in arr:하면 [1,1,2]나옴. 왤까
#[1,1],[1,2],[2,2],[2,0],[0,3]으로 돌아가지 않는다.