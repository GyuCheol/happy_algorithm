def solution(heights):

    heights = []
    answers = [0]*len(heights)
    value = 0

    for i in range(1,len(heights),1):
        for j in range(2,-1,1): #마지막항에서 첫번째항?
        
            if (heights[i] >= heights[j]):
                value = i
            else:
                value = 0
            answers.append(value)
        


    return answers

print(solution([6,9,5,7,4])