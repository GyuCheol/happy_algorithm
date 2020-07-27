# 7월 19일

# 압축
# https://programmers.co.kr/learn/courses/30/lessons/17684
# 2018 카카오 블라인드 코딩테스트 3차 - lv2

# 단순히 dictionary를 이용해서
# 색인이 있는지 판단하고, 점점 그 길이를 늘려나가며 알고리즘을 만들면 된다.
# 문제 지문이 꽤 난해해서 여러 번 읽는데에 고생한 문제
# 단순히 각 index마다 단어를 늘이면서 포함되는지 포함 안되는지 하면 된다.
# 그 검색 자료구조를 dict(hash)를 쓰는 것이 중요

# 시간 복잡도 : O(N^2) 아마 모든 알파벳을 같도록 (ex: AAAAAAAAA) 하면 각 글자마다 길이만큼 루프를 돌 것이기에. 

def solution(msg):
    # 기본 1글자 알파벳 초기화
    map = {chr(65 + i): i + 1 for i in range(26)}
    answer = []
    
    id = 0
    l = 1
    word = ''

    while (id + l) <= len(msg):
        word = msg[id:id+l]

        if word in map:
            l += 1
        else:
            map[word] = len(map) + 1
            answer.append(map[word[:l-1]])
            id += (l-1)
            l = 1
    
    # 마지막 글자 처리
    answer.append(map[msg[id:id+l]])

    return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))
