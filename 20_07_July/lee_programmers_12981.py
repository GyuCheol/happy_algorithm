# 7월 14일

# 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981
# Summer/Winter Coding (2018) lv 2

# set (hash) 구조를 이용하여
# 언급된 단어인지 검사

# 시간 복잡도 O(N)

def solution(n, words):
    spoken_word = set()
    last_word = words[0][0]

    for id, word in enumerate(words):

        if word in spoken_word or last_word[-1] != word[0]:
            return [id % n + 1, (id // n) + 1]

        spoken_word.add(word)
        last_word = word

    return [0, 0]


print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))