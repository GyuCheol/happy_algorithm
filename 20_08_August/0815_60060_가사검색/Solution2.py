# 정렬, 이진 탐색 풀이법
from bisect import bisect_left, bisect_right

def find_words(words, query):
    
    q1 = query.replace('?', 'a')
    q2 = query.replace('?', 'z')

    # q1랑 비교해서 가장 작은 것 왼쪽
    left_index = bisect_left(words, q1)
    # q2랑 비교해서 가장 큰 것
    right_index = bisect_right(words, q2)

    return right_index - left_index


def solution(words, queries):
    sorted_word = [[] for _ in range(10001)]
    reversed_sorted_word = [[] for _ in range(10001)]

    for word in words:
        sorted_word[len(word)].append(word)
        reversed_sorted_word[len(word)].append(word[::-1])
    
    for i in range(1, 10001):
        sorted_word[i].sort()
        reversed_sorted_word[i].sort()

    answer = []

    for query in queries:
        cnt = 0

        if query[0] == '?':
            # 접두사가 '?'라면 뒤집은 것으로 검색
            cnt = find_words(reversed_sorted_word[len(query)], query[::-1])
        else:
            cnt = find_words(sorted_word[len(query)], query)

        answer.append(cnt)

    return answer



solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
