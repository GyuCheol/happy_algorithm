# 7월 12일

# p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916

# 별거 아닌 쉬운 문제인데
# 다른 방법으로 구상해보고 싶었음. (count 안쓰고, python 답게)
# 근데 가독성이 별로다

# 시간 복잡도 O(N)

def solution(s):
    return sum([1 if c == 'p' else -1 if c == 'y' else 0 for c in s.lower()]) == 0


print(solution('pyyypy'))
print(solution('py'))
print(solution('pypypypy'))
print(solution('yp'))