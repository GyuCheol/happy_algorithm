from math import sqrt

# 미완

# 골브바흐의 파티션
# https://www.acmicpc.net/problem/17103

# 최대 N이 백만까지 입력되는 점을 이용
# 즉 50만까지의 소수를 구해서, 각 소수를 2가지씩 나열하는 경우의 수를 이용해서
# 모든 케이스를 미리 구해둔 후, 결과 출력


def is_prime(n):
    
    i = 2

    while (i * i) <= n:

        if n % i == 0:
            return False

        i += 1
    
    return True


prime_list = [1] * 500000
prime_list[0] = 0
prime_list[1] = 0

# 미리 50만까지의 소수를 모두 구한다.
# 에라토스체네스의 체 사용
for i in range(2, int(sqrt(500000))):
    
    if prime_list[i] == 1 and is_prime(i) == True:

        j = i * 2
        
        # 해당 소수의 배수는 모두 소수 목록에서 제외
        while j < 500000:
            prime_list[j] = 0

            j += i

# 백만 개의 경우의 수에 결과 누적
cases = [0] * 1000001

print(1)


n = int(input())

for _ in range(n):

    number = int(input())
    print(cases[number])

