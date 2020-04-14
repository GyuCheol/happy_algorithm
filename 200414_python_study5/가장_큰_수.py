import functools

def str_comp(x: str, y: str):

    x_len, y_len = len(x), len(y)

    for i in range(4):
        x_id = i % x_len
        y_id = i % y_len

        if x[x_id] == y[y_id]:
            continue
        elif x[x_id] > y[y_id]:
            return 1
        else:
            return -1


    return 0

def solution(numbers):
    str_list = list(map(str, numbers))
    str_list = sorted(str_list, key=functools.cmp_to_key(str_comp), reverse=True)

    return str(int(''.join(str_list)))

print(solution([121, 12]))