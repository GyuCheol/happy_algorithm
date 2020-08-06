
def solution(words):
    count = len(words)
    if count == 1:
        return 1

    words = list(sorted(words))

    prv = (count - 1) * [0]
    nxt = (count - 1) * [0]

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        comp_len = len(startswith_text(word1, word2))

        prv[i] = comp_len
        if len(word1) != comp_len:
            prv[i] += 1

        nxt[i] = comp_len
        if len(word2) != comp_len:
            nxt[i] += 1

    return sum([max(a, b) for a, b in zip(prv + [0], [0] + nxt)])

def startswith_text(word1, word2):
    min_length = min(len(word1), len(word2))
    for i in range(min_length):
        if word1[i] != word2[i]:
            return word1[:i]
    return word1[:min_length]