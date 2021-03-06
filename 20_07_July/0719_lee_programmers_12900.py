# 7월 19일

# 2 x n 타일링
# https://programmers.co.kr/learn/courses/30/lessons/12900
# DP - lv3

# 작은 문제에서부터 n까지 경우의 수를 구하면 된다.
# 막대기를 추가할 수 있는 경우는 2가지다.
# 오른쪽 끝에 세로 막대기가 추가하거나
# 가로 막대기 2개 쌓은 것을 추가하거나

# 세로 막대기 1개가 추가되는 경우는 d[n-1]에서 세로막대기 1개씩 추가하는 경우
# 가로 막대기 2개가 추가되는 경우는 d[n-2]에서 가로막대기 2개씩 추가하는 경우
# 이 2가지 경우가 합해져서 d[n]의 경우의 수가 나온다.
# 최초 d[0]과 d[1]을 1로 초기화한다. (d[0]은 가능한 경우가 아니지만, 가로 막대기 2개의 경우 최소 가능한 횟수로 가정한 것)
# d[2]는 d[1]의 결과에서 세로막대기를 추가하면 되니, 그 만큼 추가 경우의 수가 나올 수 있음.
# d[3]도 d[2]의 결과에서 세로막대기만 뒤에 추가하면 되는 것과, d[1]에서 가로막대기만 뒤에 추가하면 되는 경우를 가질 수 있다.
# 수열이 피보나치 수열과 흡사하게 생성되므로, 그런식으로 풀어도 되긴하다.

# 2 x (n-1) 세로 막대기가 추가되는 경우
# 2 x (n-2) 가로 막대기가 추가되는 경우

# 점화식 d[n] = d[n-1] + d[n-2]

# O(n)


def solution(n):
    d = [0] * (n + 1)
    
    d[0], d[1] = 1, 1

    for i in range(2, n + 1):
        d[i] = (d[i-1] + d[i-2]) % 1000000007

    return d[n]

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))