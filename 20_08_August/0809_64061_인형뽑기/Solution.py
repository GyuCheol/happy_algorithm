def solution(board, moves):
    stack_list = [[] for x in range(len(board))]
    result = []
    answer = 0

    # 역으로 루프하며 추가 (stack 구조를 위해)
    for b in board[::-1]:
        for id, doll in enumerate(b):
            if doll > 0:
                stack_list[id].append(doll)
    
    for move in moves:
        
        # 아무 것도 없는 곳이면 continue
        if len(stack_list[move - 1]) == 0:
            continue

        doll = stack_list[move - 1].pop()
        
        if result and result[-1] == doll:
            answer += 2 # 인형은 짝으로 터진다
            result.pop()
        else:
            result.append(doll)
        
    
    return answer

# expected 4
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
