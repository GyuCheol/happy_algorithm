
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
