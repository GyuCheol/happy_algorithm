from functools import cmp_to_key

class Play(object):
    
    def __init__(self, id, genre, play, genre_dict):
        self.id = id
        self.genre = genre
        self.play = play
        self.genre_dict = genre_dict
    

def sorting(a: Play, b: Play):
    
    if a.genre == b.genre:
        if a.play == b.play:
            return a.id - b.id
        else:
            return b.play - a.play
    else:
        return b.genre_dict[b.genre] - a.genre_dict[a.genre]


def solution(genres, plays):
    genres_dict = {x: 0 for x in genres}
    genres_flag = {x: False for x in genres}
    play_list = []
    id = 0

    for genre, play in zip(genres, plays):
        genres_dict[genre] += play
        play_list.append(Play(id, genre, play, genres_dict))
        id += 1
    
    play_list.sort(key=cmp_to_key(sorting))

    answer = []
    key = ''
    rank = 0

    for play in play_list:
        if key != play.genre:
            key = play.genre
            rank = 1

        if rank <= 2:
            answer.append(play.id)

        rank += 1

    return answer


print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))
print(solution(['a', 'a', 'b', 'b', 'b'], [0, 1, 3, 3, 3]))
print(solution(['a', 'b', 'c', 'd', 'e'], [0, 1, 2, 3, 4]))
