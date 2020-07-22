# 7월 22일

# 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627
# heap - lv3

# 가장 우선 적인 순위는 실행 시간이 짧은 것이다.
# 실행 시간이 짧은 것부터 실행 시키는 것이 여기서 원하는 heap 구조의 개념이지만,
# 다른 실행 가능성이 있는 값도 봐야하므로 list를 정렬하여 처리했다. 
# ※ 현재 처리 중인 작업이 없다면 바로 실행 가능해야함.

# time이라는 시간 값을 증가시키며
# time에 따라 현재 실행 가능한 job이 있으면 실행하고 없다면 time을 1씩 증가시킨다.
# 그렇게 모든 job을 소비할 때까지 loop 진행
# python 따로 중첩 loop문에서 탈출할 방법이 없으므로 nested function 사용
# 좀 더 단순히 생각할 필요가 있겠다.
# 이런 류의 문제인 경우 문제 크기가 작다면, time 값을 하나하나 증가시켜서 해결할 아이디어.
# 매번 이런 류의 문제에 조금 더 logN, N등의 최적 시간 복잡도를 생각하다가 로직이 꼬인다.

# O(NlogN) 정렬된 상태에서 실행 가능한 job이 있는지 순회하기 때문에 평균적으로 NlogN을 순회할 것 같다.
# 다만 최악의 경우에는 N^2이 기대가 된다.


def solution(jobs):
    sorted_jobs = sorted(jobs, key=lambda x: (x[1], x[0]))

    time = 0
    total = 0

    def process_job():
        nonlocal time, total

        for job in sorted_jobs:
            job_start, job_process = job
            
            # 현재 시간에서 실행 가능한가?
            if time >= job_start:
                total += (time - job_start) + job_process
                time += job_process
                sorted_jobs.remove(job)
                return True

        return False


    while sorted_jobs:

        if process_job() == False:
            time += 1


    return total // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 3], [10, 3], [12, 6]]))