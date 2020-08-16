from collections import deque

def time_to_int(time):
    h, m = tuple(map(int, time.split(':')))

    return (h * 60) + m

def int_to_time(time):
    h, m = time // 60, time % 60

    return f'%02d:%02d' % (h, m)


def solution(n, t, m, timetable):
    crew_queue = deque(sorted([time_to_int(time) for time in timetable]))
    bus_capacity = n * m
    cur_bus = time_to_int('09:00')


    for i in range(n):
        cnt = 0

        while crew_queue[0] <= cur_bus:

            if (bus_capacity - cnt) == 1:
                return int_to_time(crew_queue[0] - 1)
            else:
                cnt += 1
                crew_queue.popleft()

                if cnt == m or len(crew_queue) == 0:
                    break
        
        bus_capacity -= m
        cur_bus += t

    cur_bus -= t

    return int_to_time(cur_bus)

print(solution(1, 1, 1, ["00:01"]))
print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))