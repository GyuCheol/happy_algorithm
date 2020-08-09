
def solution(strs, t):
    str_dict = {s[0]: [] for s in strs}
    d = [0] * (len(t) + 1)

    for s in strs:
        str_dict[s[0]].append(s)

    for i in range(1, len(t) + 1):
        tmp = i - 1

        if t[tmp] in str_dict:
            for s in str_dict[t[tmp]]:
                if s == t[tmp:tmp + len(s)]:
                    
                    if d[i] == 0:
                        d[i] = d[tmp] + 1
                    else:
                        d[i] = min(d[i], d[tmp] + 1)

                    if d[tmp + len(s)] == 0:
                        d[tmp + len(s)] = d[tmp] + 1
                    else:    
                        d[tmp + len(s)] = min(d[tmp + len(s)], d[tmp] + 1)
        
        if d[i] == 0:
            return -1

    
    return d[len(t)]


solution(["a"], "bbbabaa")

solution(["ab", "na", "n", "a", "bn"], "nabnabn")

solution(["ba", "na", "n", "a"], "banana")


solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple")

solution(["ba", "an", "nan", "ban", "n"], "banana")

solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple" * 4)
