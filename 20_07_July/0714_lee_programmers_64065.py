# 7월 14일

# 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065
# 2019 카카오 개발자 인턴십 lv2

# 문자열을 잘 쪼개는 기술 (split)
# 정렬하는 기술
# 그것만 알면 쉽게 해결 가능하다.
# 조금 귀찮아서 꼼수 같은 수단을 사용했다.

# 시간 복잡도 O(N^2)

def solution(s):
    # 가장 첫, 마지막 {, }을 생략하고 },으로 split
    sets = s[1:-1].split('},')
    # 문자열 길이별 정렬
    sets.sort(key=lambda a: len(a))
    s = set()
    answer = []

    for t in sets:
        # 내부 {, } 모두 제거하고 , 로 split
        elements = t.replace('{', '').replace('}', '').split(',')

        for e in elements:
            if e not in s:
                answer.append(int(e))
                s.add(e)
        
    return answer

from collections import Counter
from re import findall

# Counter로 요소 개수대로 sorting한 로직. 심플하다.
def solution2(s):

    return list(map(lambda i: int(i[0]), sorted(Counter(findall('\d+', s)).items(), key=lambda i: i[1], reverse=True)))
    

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution2("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
