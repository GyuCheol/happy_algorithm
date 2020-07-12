# 7월 12일

# 크레인 인형 뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061
# 카카오 개발자 겨울 인턴십 - lv1

# stack 이용한 문제
# 이게 lv1? lv2~3은 되어 보인다.
# 로직은 쉽지만, 문제 지문도 길고 요구하는 로직도 단순하진 않다

# stack으로 각 line을 쌓고,
# 인형을 보관하는 곳도 stack으로 쌓아둔다.
# 크레인으로 가져갈 때 마다 stack 맨 윗 값과 비교하여 같으면 pop
# 아니면 append

# 시간 복잡도 O(N^2) board에 있는 걸 로딩하므로..

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