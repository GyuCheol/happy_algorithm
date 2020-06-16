
# 숨바꼭질6
# https://www.acmicpc.net/problem/17087
# D는 거리의 차의 약수로 구할 수 있음.
# 모든 거리의 차의 최대 공약수 구하기


def gcd(a, b):
    
    while a % b != 0:
        a, b = b, a % b

    return b

n, s = tuple(map(int, input().split(' ')))
brothers = list(map(int, input().split(' ')))
distance_diff = [abs(s - x) for x in brothers]

# n개의 모든 요소의 최대 공약수는
# 최대 공약수 결과로 다음 최대 공약수를 구하는 인자로 쓰면 된다.
answer = distance_diff[0]

for diff in distance_diff[1:]:
    answer = gcd(answer, diff)

print(answer)

