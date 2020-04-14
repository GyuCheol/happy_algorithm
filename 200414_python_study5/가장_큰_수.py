
def solution(numbers):
    str_list = list(map(str, numbers))
    str_list = sorted(str_list, key=lambda s: s * 3, reverse=True)

    return str(int(''.join(str_list)))

print(solution([121, 12]))