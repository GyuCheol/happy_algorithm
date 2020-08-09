
def solution(strs, t):
    str_set = {s for s in strs}
    d = [0] * (len(t) + 1)
    
    def search(i):
        tmp = i - 1

        for j in range(5):
            if (i + j) <= len(t) and t[tmp:i + j] in str_set:
                if d[i + j] == 0:
                    d[i + j] = d[tmp] + 1
                else:
                    d[i + j] = min(d[i + j], d[tmp] + 1)

    # 초기값
    search(1)

    for i in range(2, len(t) + 1):

        # 이전 단계가 0이면 현재 단계에서 검색 불가.
        if d[i - 1] != 0:
            search(i)
    
    return d[len(t)] if d[len(t)] != 0 else -1



solution(["a", "c"], "ca")
solution(["ab", "ba"], "aba")
solution(["a", "ba"], "ababa")

solution(["app", "le"], "apple")
solution(["app", "ap", "p", "l", "e", "ple", "pp", "pple"], "apple")
solution(["ab", "na", "n", "a", "bn"], "nabnabn")
solution(["ba", "na", "n", "a"], "banana")
solution(["ba", "an", "nan", "ban", "n"], "banana")
solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple" * 4)
