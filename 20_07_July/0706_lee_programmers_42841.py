
# 7월 6일

# 숫자 야구 
# https://programmers.co.kr/learn/courses/30/lessons/42841
# 완전 탐색 - lv2

# 무식하게 123~987까지 돌면서 답의 가능성이 있는지 모두 탐색하여 비교한다.
# 시간 복잡도 O(N)

def solution(baseball):
    answer = 0

    def check(i):
        nums = converting_three_numbers(i)
        # 110, 120, 100, 200등 0이 포함된 숫자 제외
        if 0 in nums:
            return False

        # 113, 221, 313 등 동일 숫자 2개 반복 제외
        if nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return False

        return True

    def converting_three_numbers(x):
        return (x // 100, (x // 10) % 10, x % 10)

    # 111~999 루프
    nums = [converting_three_numbers(x) for x in range(123, 988) if check(x)]
    converted_baseball = [(converting_three_numbers(numbers), s, b) for numbers, s, b in baseball]

    for i_numbers in nums:
        # baseball 배열에 맞는지 검사한다.
        cnt = 0

        for num_number, s, b in converted_baseball:
            strike = 0
            ball = 0

            for id, n in enumerate(i_numbers):
                if i_numbers[id] == num_number[id]:
                    strike += 1
                elif i_numbers[id] in num_number:
                    ball += 1

            if s == strike and b == ball:
                cnt += 1
        
        # i의 strike, ball이 모두 만족하면 답으로 가능하다.
        if cnt == len(baseball):
            answer += 1

    return answer

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))