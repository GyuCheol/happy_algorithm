# 7월 21일

# 저울
# https://programmers.co.kr/learn/courses/30/lessons/42886
# Greedy - lv3

# 거의 40분간 규칙성을 찾아낸다고 고생했다..
# 일단 정렬을 하여 각 추 무게를 순서대로 놓을 수 있도록 한다.
# 첫 추부터 1을 초과한다면 바로 답은 1이다.
# 그 다음 추부터 놓을 때, 
# 그 추의 무게가 지금까지 쌓아온 추 무게보다 크다면 바로 이전 크기가 최대 값이 된다.
# 삽질을 엄청 했지만 만족스러운 시간 복잡도와 로직이 완성!!!!! YEAH!!!!!!!!

# O(NlogN)

def solution(weight):
    weight_list = sorted(weight)

    total = weight_list[0]

    if total > 1:
        return 1

    for w in weight_list[1:]:
        if total + 1 < w:
            return total + 1

        total += w


    return total + 1

# print(solution([1, 1, 2, 3, 6, 7, 30]))
# print(solution([1, 1, 1, 2, 3, 6, 7, 30]))
print(solution([10]))
print(solution([1, 1, 2, 3]))