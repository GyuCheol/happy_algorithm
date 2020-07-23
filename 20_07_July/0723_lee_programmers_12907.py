# 7월 23일

# 거스름돈
# https://programmers.co.kr/learn/courses/30/lessons/12907
# 연습 문제 - lv3

# DP식 문제의 냄새가 난다.
# 화페의 단위는 100종류 이하

# 고민을 1시간 정도 했는데,,, 답이 안나와 힌트를 얻었다.
# 힌트를 얻어도 발을 동동 굴리며 생각하다가 답이 나왔다.
# 이전 화페에서 얻은 결과를 다음 경우의 수를 어떻게 넘길까를 아래의 로직처럼 해결

# 각 money를 순회하며 이전 결과에서 얻어올 수 있는 경우의 수를 누적하며 n까지 나아가면 된다.
# 이전 결과 중에서 money를 더하여 갈 수 있는 곳을 이전 결과에서 올 수 있었으니 그 값으로 누적.
# 현재 money로 가능한 각 구간을 순회하며 +1

# O(M * N) 100,000 * 100



def solution(n, money):
    d = [0] * (n + 1)
    
    for m in money:

        for i in range(m, n + 1):
            if d[i - m] > 0:
                d[i] += d[i - m] % 1000000007

        for i in range(m, n + 1, m):
            d[i] = (d[i] + 1) % 1000000007

    return d[n]

# expected 4
print(solution(5, [1, 2, 5]))

# expected 1
print(solution(10, [1]))

print(solution(10, [1, 2, 4, 5, 8]))

