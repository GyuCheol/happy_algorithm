# 7월 19일

# 추석 트래픽
# https://programmers.co.kr/learn/courses/30/lessons/17676
# 2018 카카오 블라인드 공채 1차 - lv3

# 문제를 풀기위한 아이디어와 직관이 중요한 문제.
# 시간을 연산하기 쉽게 수치화 시켜야하고
# 배열은 어차피 오름차순으로 오기 때문에 2분탐색해서 찾는 방법도 있긴하다.
# 2분 탐색했다면 NlogN 시간 복잡도 이지만, 굳이 그렇게 복잡하게 하지 않아도
# 시간 복잡도 안에 들어오므로 하나하나 최대 처리 가능한 요소를 찾아도 된다.
# 1] 처리 시작 시간과 처리가 마무리된 시간을 list에 넣는다. (각각의 그 2개 포인트만 탐색하면 되므로)
# 2] list를 오름차순 정렬한다
# 3] 각 시간당 1초 안으로 처리된 max count를 구한다.

# O(N^2) - 첫풀이
# O(NlogN) - 다른 사람 풀이 참고 필요

SECOND = 1000
MINUTES = SECOND * 60
HOURS = MINUTES * 60
INTERVAL = 0.001

def solution(lines):
    answer = 1
    time_list = []

    def convert_to_int(s):
        h, m, sec = s.split(':')

        return int(h) * HOURS + int(m) * MINUTES + int(float(sec) * SECOND)

    for id, line in enumerate(lines):
        # yyyy-MM-dd는 생략해도 된다. [11:]
        # 맨 마지막 s를 제외하기 위해 -1까지만 한다.
        start, time = line[11:-1].split(' ')

        # 시작 시분초를 int화 시킨다.
        # 1sec = 1000 (소수 셋째 자리까지 처리하기 위함)
        # time_list만 계산할 수 있도록 time_list에 따로 보관
        start = convert_to_int(start)
        time = int((float(time) - INTERVAL) * SECOND)

        # 시작~종료 시간 int화 해서 추가
        time_list.append((start - time, start))

    time_list.sort()
    l = len(time_list)

    for i in range(l):

        for end in time_list[i]:
            # 각 시간 값에서 1초동안 들어온 처리량 비고
            start = end - 999
            cnt = 0
            
            for s, e in time_list:
                
                # case1 s 또는 e가 start ~ end에 포함된다.
                # case2 start 또는 end가 s~e에 포함된다.
                if start <= s <= end or start <= e <= end:
                    cnt += 1
                elif s <= start <= e or s <= end <= e:
                    cnt += 1
            
            answer = max(cnt, answer)


    return answer

print(solution(['2016-09-15 03:00:00.001 0.5s', '2016-09-15 03:00:00.001 0.5s', '2016-09-15 03:00:00.001 0.5s']))
print(solution(['2016-09-15 01:00:04.001 2.0s', '2016-09-15 01:00:07.000 2s']))
print(solution(['2016-09-15 01:00:04.002 2.0s', '2016-09-15 01:00:07.000 2s']))
print(solution(['2016-09-15 23:59:59.999 0.001s']))