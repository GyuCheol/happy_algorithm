# 7월 17일

# 파일명 정렬
# https://programmers.co.kr/learn/courses/30/lessons/17686
# 2018 카카오 블라인드 공채 3차 - lv2

# pythoic한 sorting이면 매우 간단하게 풀이가 된다.
# 정규식을 응용하여 문자열 분리도 쉽고

# O(NlogN) N개 요소에 N번의 정규식을 실행하므로 N^2인가?

from re import compile

# head, number, tail 파싱
# sotring 순서 head > number (tail은 정렬에 영향이 없다.)
# head == number의 경우 원래 순서가 유지되어야 한다.
# sorint algorithm이 unstable인 경우를 고려하여 index를 하나 더 넣어두는 것도 고려.
# python sorting은 stable 알고리즘이다. (오우!)
comp = compile(r'^([^\d]+?)(\d+)(.*)$')

def solution(files):
    
    def sorting_key(s):
        l = comp.findall(s.lower())

        return (l[0][0], int(l[0][1]))

    return sorted(files, key=sorting_key)

print(solution(['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']))
print(solution(['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']))