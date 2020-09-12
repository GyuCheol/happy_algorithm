from itertools import combinations

def solution(orders, course):
    ordered_map = [dict() for _ in range(len(course))]
    max_values = [0 for _ in range(len(course))]
    answer = []

    for i in range(len(course)):
        for o in orders:
            o = ''.join(sorted(o))

            for p in combinations(o, course[i]):
                key = ''.join(p)
                if key in ordered_map[i]:
                    ordered_map[i][key] += 1
                else:
                    ordered_map[i][key] = 1
                
                max_values[i] = max(max_values[i], ordered_map[i][key])

        if max_values[i] >= 2:
            answer.extend([k for k, v in ordered_map[i].items() if v == max_values[i]])

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
