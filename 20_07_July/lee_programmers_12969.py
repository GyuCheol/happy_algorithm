# 7월 13일

# 직사각형 별 찍기
# https://programmers.co.kr/learn/courses/30/lessons/12969
# lv 1

# python의 문자 연산자 응용

# 시간 복잡도 O(N^2)

a, b = map(int, input().strip().split(' '))

print(('*' * a + '\n') * b)