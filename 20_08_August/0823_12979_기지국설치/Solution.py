def solution(n, stations, w):
    answer = 0
    start = 1
    width = 1 + (w * 2)

    for station in stations:
        begin, end = station - w, station + w
        
        if begin > start:
            answer += -(-(begin - start) // width)

        start = end + 1
    
    if start <= n:
        answer += -(-((n + 1) - start) // width)

    return answer


assert(3 == solution(11, [4, 11], 1))
assert(3 == solution(16, [9], 2))
assert(2 == solution(300, [151], 100))
assert(1 == solution(6, [5], 1))
assert(1 == solution(1, [], 1))
assert(2 == solution(10, [], 4))
assert(2 == solution(18, [], 4))
assert(3 == solution(19, [], 4))
assert(4 == solution(10, [], 1))
assert(0 == solution(10, [2, 4, 7, 9], 1))