# 7월 13일

# 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912
# lv 1

# loop를 쓰면 한 번에 해결이지만,
# 공식을 만들어서 해결하고 싶었음.
# 대소 비교로 작은 수, 큰수를 구한다.
# 큰수 만큼의 합계와 작은 수 -1까지의 합계를 빼면은 된다.
# 여기서 작은 수 -1까지 하는 이유는 3, 5까지의 합계 중 2까지의 합계가 제거되어야 하니
# 작은 수에서 1을 빼주는 것

# 다른 사람 풀이보니,,, 아래와 같은 한방 공식도 있다!
# (abs(a-b)+1) * (a+b) // 2 @.@

# 시간 복잡도 O(1) (상수항 해결)

def solution(a, b):
    mn, mx = min(a, b) - 1, max(a, b)
    
    return (mx * (mx + 1) // 2) - (mn * (mn + 1) // 2)

print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
print(solution(1, 10))
print(solution(0, 10))
print(solution(-5, 5))