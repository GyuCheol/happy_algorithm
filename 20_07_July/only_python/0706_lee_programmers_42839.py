# 7월 6일

# 소수찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839
# 완전 탐색 - lv2

# 1개, 2개, 3개.. n개 씩 카드를 뽑게하여 순열 알고리즘 이용
# set을 이용하여 중복되는 경우 검출
# 시간 복잡도 O(n!)


def solution(numbers):
    s = set()
    nums = []

    # n개 만큼의 카드를 고른 배열 생성
    def make_list(id, n):
        
        if len(nums) == n:
            # 생성이 끝난 배열은 permuate하여 모든 조합 생성
            permutate(0, len(nums))
            return

        for i in range(id, len(numbers)):
            nums.append(numbers[i])
            make_list(i + 1, n)
            nums.remove(numbers[i])

    # 소수 판별
    def is_prime(n):
        i = 2

        while (i*i) <= n:
            if n % i == 0:
                return False
            
            i += 1
        
        return True

    def permutate(src, len):
        
        if src == len:
            num = int(''.join(nums))

            if num > 1 and num not in s and is_prime(num):
                s.add(num)

            return
        
        for i in range(src, len):
            nums[i], nums[src] = nums[src], nums[i]
            permutate(src + 1, len)
            nums[i], nums[src] = nums[src], nums[i]


    for i in range(1, len(numbers) + 1):
        make_list(0, i)
    
    return len(s)

# print(solution('17'))
print(solution('123'))