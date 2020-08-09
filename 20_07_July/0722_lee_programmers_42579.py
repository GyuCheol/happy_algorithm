# 7월 22일

# 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579
# hash - lv3

# 이전에 풀어본 문제인데,
# 최근 레벨 업된 파이썬 실력으로 다시 풀어본다.
# 1] 각 장르와 play에 맞게 dict를 만든다. (각 genre에 재생된 play list를 가지도록)
# 2] 각 장르와 해당 장르의 play 총 합계에 맞게 내림차순 정렬된 list를 만든다.
# 3] 내림차순 정렬된 list를 돌며 해당 play를 또 정렬한다.
# 4] 정렬된 list를 최대 2개까지 loop돌며 answer에 id를 추가한다.

# 그래서 정렬을 위한 튜플을 따로 만들어 해결하는게 제일 심플하긴 하다.
# 확실히 이전 답안에 비해 매우 심플해졌다.

# O(NlogN)

def solution(genres, plays):
    genres_dict = {x: [] for x in genres}
    answer = []

    for id, val in enumerate(zip(genres, plays)):
        genre, play = val[0], val[1]
        genres_dict[genre].append((play, id))

    # 각 장르마다 play 총 합계 저장
    cnt_list = [(sum([x[0] for x in v]), k) for k, v in genres_dict.items()]
    # 앨범 수록곡 총 재생횟수 내림차순 정렬
    cnt_list.sort(key=lambda x: -x[0])
    
    for cnt, genre in cnt_list:
        l = genres_dict[genre]
        # 재생횟수 내림차순, id 오름차순 정렬
        l.sort(key=lambda x: (-x[0], x[1]))
        
        # 최대 2개까지 answer에 추가
        for _, id in l[:min(len(l), 2)]:
            answer.append(id)

    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))
