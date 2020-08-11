from itertools import permutations

def solution(n, weak, dist):
    answer = 0x7fffffff

    def compare(end, id):

        if id < len(weak):
            return end >= weak[id]
        else:
            return (end - n) >= weak[id % len(weak)]


    for per in permutations(dist):

        for id in range(len(weak)):
            visited = [0] * len(weak)
            cnt = 0
            
            for i, p in enumerate(per):
                start = weak[id % len(weak)]
                end = start + p
                visited[id % len(weak)] = i + 1
                id += 1
                cnt += 1

                while compare(end, id) and id < (len(weak) * 2):
                    visited[id % len(weak)] = i + 1
                    cnt += 1
                    id += 1
                
                if cnt >= len(weak):
                    answer = min(answer, len(set(visited)))
                    break
            
    return answer if answer != 0x7fffffff else -1


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
solution(12, [1, 5, 6, 10], [1, 15])
solution(12, [1, 5, 6, 10], [1, 1, 1, 1, 1, 15])

solution(12, [1, 5, 6, 10], [1, 1, 1])
solution(12, [1, 5, 6, 10], [1, 1])

print(solution(12, [0, 11], [1]))
