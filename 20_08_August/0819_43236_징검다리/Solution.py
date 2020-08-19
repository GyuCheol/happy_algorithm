
def solution(distance, rocks, n):
    rocks.sort()
    distance_list = [rocks[0]]
    distance_list.extend([rocks[i] - rocks[i-1] for i in range(1, len(rocks))])
    distance_list.append(distance - rocks[-1])

    left = 0
    right = distance + 1
    answer = 0
    
    def can_get_dist(mid):
        cnt = n
        tmp = distance_list[:]

        for i in range(len(tmp)):

            if tmp[i] < mid:
                if cnt == 0:
                    return False

                cnt -= 1
                tmp[i + 1] += tmp[i]


        return True

    while True:
        mid = (left + right) // 2

        if left == mid or right == mid:
            break

        if can_get_dist(mid):
            left = mid
            answer = max(answer, mid)
        else:
            right = mid

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
