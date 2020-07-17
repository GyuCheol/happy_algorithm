# 7월 17일

# 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888
# 카카오 2019 블라인드 채용 - lv2

# python 숙련되고 나서 재풀이
# dict 이용한 풀이

# O(n)

def solution(record):
    result = []
    mapped_name = dict()

    for r in record:
        s = r.split(' ')

        if s[0][0] in {'C', 'E'}:
            # Change 또는 Enter는 이름 변경
            mapped_name[s[1]] = s[2]
        
        if s[0][0] != 'C':
            # command과 이름 저장
            result.append((s[0][0], s[1]))
    
    return [f'{mapped_name[name]}님이 { "들어왔습니다." if c == "E" else "나갔습니다." }' for c, name in result]

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))