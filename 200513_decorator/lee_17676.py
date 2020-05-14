# https://programmers.co.kr/learn/courses/30/lessons/17676

import re

from typing import List

def solution(lines: List[str]) -> int:
    answer = 0

    # 정규식으로 시분초, 로그 문자열 파싱
    r = re.compile(r'2016-09-15 (\d{2}):(\d{2}):(\d{2}\.\d{3}) (\d{1}\.?\d*)s')
    time_info = []
    time_list = []

    for log in lines:
        groups = r.match(log).groups()

        # 정규식으로 파싱한 문자열 숫자로 컨버팅
        # 부동 소수점 연산의 정확도 문제로 모두 정수화
        hour = int(groups[0]) * 3600000
        minute = int(groups[1]) * 60000
        second = int(float(groups[2]) * 1000)
        log_sec = int(float(groups[3]) * 1000)

        # start, end를 초단위 수치화
        end = hour + minute + second
        start = end - (log_sec - 1) # 0.001초를 포함하므로

        time_info.append((start, end, log))
        time_list.append(start)
        time_list.append(end)
    
    answer = 0
    
    for start in time_list:
        count = 0
        end = start + 999

        for info in time_info:
            if (start <= info[0] <= end or start <= info[1] <= end or 
                (info[0] <= start and end <= info[1])):
               count += 1

        answer = max(answer, count)
    
    return answer

print(solution([
'2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s']))

print(solution([
'2016-09-15 01:00:04.002 2.0s',
'2016-09-15 01:00:07.000 2s']))


print(solution([
'2016-09-15 01:00:04.001 2.0s',
'2016-09-15 01:00:07.000 2s'
]))
