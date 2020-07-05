# 6월 1일

# 소수 구하기
# https://www.acmicpc.net/problem/1929
# 에라토스체네스의 체를 이용한 소거법으로 풀이
# 시간 복잡도 : O(N * logN)

def is_prime(number):

    n = 2

    # 루트 number까지 확인
    # 소인수 분해시, 루트 number를 넘어가는 인자가 나오지 않음을 이용
    while (n*n) <= number:
        if number % n == 0:
            return False

        n += 1
    
    return True

min, max = tuple(map(int, input().split(' ')))

ary = [1] * (max + 1)
ary[0] = ary[1] = 0

prime_numbers = []

for i in range(max + 1):

    if ary[i] == 1 and is_prime(i):
        # i부터 max까지 모든 배수 소거
        for j in range(i, max + 1, i):
            ary[j] = 0
        
        # 소수 추가 (min 값보다 큰 값만)
        if i >= min:
            prime_numbers.append(str(i))

print('\n'.join(prime_numbers))

