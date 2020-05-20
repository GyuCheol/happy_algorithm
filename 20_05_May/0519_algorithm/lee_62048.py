
def solution(w,h):
    answer = w * h

    if w == h:
        answer -= w
    elif w % 2 == 0 and h % 2 == 0:
        answer -= min(h, w) * 2
    elif w % 2 == 1 and h % 2 == 1:
        answer -= min(h, w) * 2
        answer -= 1
    else:
        answer -= min(h, w) * 2

    return answer

# 80
print(solution(8, 12))
