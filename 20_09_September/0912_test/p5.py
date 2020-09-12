from bisect import bisect_left, bisect_right

def parse_to_int(time):
    h = int(time[:2])
    m = int(time[3:5])
    s = int(time[7:9])

    return (h * 60 * 60) + (m * 60) + s

def solution(play_time, adv_time, logs):
    play_i = parse_to_int(play_time)
    adv_i = parse_to_int(adv_time)

    logs.sort()

    log_time_list = [range(parse_to_int(log[:8]), parse_to_int(log[9:])) for log in logs]
    max_value = 0
    answer = ''
    start_id = 0

    for i, elements in enumerate(log_time_list):
        start, end = elements.start, elements.stop
        adv_range = range(start, start + adv_i + 1)
        
        # 광고 재생이 불가능함.
        if adv_range.stop > play_i:
            break

        cnt = 0

        for j in range(start_id, len(logs)):
            el = log_time_list[j]

            if el.start in adv_range or el.stop in adv_range:
                cnt += 1
            elif el.start > adv_range.stop:
                break
        
        if log_time_list[start_id].start >
            start_id += 1


        if max_value < cnt:
            max_value = cnt
            answer = logs[i][:8]

    return answer

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
