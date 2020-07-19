# 7월 15일

# 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977
# Summer/Winter Coding (2018) lv2
# 탐색

# 3중 루프로 3개를 고르는 것을 완전 탐색해서 소수가 되는 것을 세자
# 50개가 최대이므로 시간 초과 문제는 없음.

# 시간 복잡도 O(N^3)

def solution(nums):
    answer = 0
    
    def is_prime(n):
        i = 2

        while (i*i) <= n:
            if n % i == 0:
                return False

            i += 1

        return True

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                
                if is_prime(nums[i] + nums[j] + nums[k]):
                    answer += 1
                    

    return answer

print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))