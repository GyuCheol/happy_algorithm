from math import sqrt

# 팬디지털(Pandigital) 문제 
# 팬디지털 : 1~n까지 숫자 1개씩만 이용해서 만든 수
# n자리 모든 팬디지털 소수 개수와 가능한 경우 중 가장 큰 소수 출력
# permuation 순열 알고리즘을 이용한 모든 경우의 수 나열
# 시간 복잡도 O(n!)

n = int(input())
cnt = 0
max_number = 0

# 1~n까지의 list 생성
numbers = [x for x in range(1, n + 1)]

# numbers list 숫자들을 10진 숫자로 변환
def getNumber():
    number = 0

    for n in numbers:
        number *= 10
        number += n
    
    return number


def isPrime(number):

    num = int(sqrt(number))

    # 소주는 2부터 n의 제곱근까지만 약수 검사하면 됨 O(logN)
    for n in range(2, num + 1):

        if number % n == 0:
            return False

    return True


# 순열 알고리즘은 O(n!)
def perm(start):
    global cnt, max_number

    if len(numbers) == start:
        number = getNumber()

        if isPrime(number):
            cnt += 1
            max_number = max(max_number, number)

        return

    for n in range(start, len(numbers)):
        # swap
        numbers[start], numbers[n] = numbers[n], numbers[start]
        perm(start + 1)
        # 상태 원상 복귀
        numbers[start], numbers[n] = numbers[n], numbers[start]

perm(0)

print(cnt)
print(max_number)
    

    


