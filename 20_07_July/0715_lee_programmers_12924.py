# 7월 15일

# 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924
# lv2 연습문제 (수학?)

# 연속으로 더한 값이 N에 도달할 수 있는지.
# 모든 연속된 결과를 구해야한다.

# 시간 복잡도 O(N)

def solution(n):
    # 기본적으로 자기 자신만으로 구할 수 있음.
    answer = 1
    
    # 홀수라면 방법이 2개를 더해서 할 수 있음
    if n % 2 == 1:
        answer += 1
    
    limit = n // 2
    
    total = 0
    i = 1
    de_i = 1

    while i <= limit:

        if total <= n:

            if total == n:
                answer += 1

            total += i
            i += 1
        else:
            total -= de_i
            de_i += 1
    
    
    return answer

# 다른 사람의 풀이를 보았는데, 약수 중에 홀수가 되는 것만 찾은 것도 있었다.
# 소인수 분해하면서 홀수의 개수가 답이 되겠다 싶었는데
# 내가 작성한 소인수 분해 로직에 문제가 있었나보다..
# 이것도 어쨋거나 똑같이 시간복잡도는 O(N)이다.
def solution2(n):
    return len([x for x in range(1, n + 1, 2) if x % n == 0])
        
# print(solution(15))
print(solution(20))