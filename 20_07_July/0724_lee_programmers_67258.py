# 7월 24일

# 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258
# 2020 카카오 인턴쉽 - lv3

# 정답이 되는 경우를 찾고,
# 찾으면 앞번호를 자르면서 최적의 길이를 찾고
# 자른 그 이후부터 다시 정답이 되는 경우를 찾고.. 반복.
# 생각보다 쉽게 풀었다. yeah~~
# 확실히 상위 랭킹오니, 실시간으로 랭킹이 왔다갔다한다.
# 221등 > 240등 > 다시 210등.
# 2자릿수가 코앞이다..
# lv3를 거의 다 완료할 때 쯔음에 될 것이라 예상.

# O(NlogN) 가능한 답을 찾으면 찾을수록 순회 문이 작아지는 로직이라 NlogN 아마도?


def solution(gems):
    s = {g for g in gems}
    t = dict()
    start = 0
    end_start = 0
    end = 0
    results = []

    while start < len(gems):

        for id in range(start, len(gems)):
            g = gems[id]

            if g not in t:
                t[g] = 1
            else:
                t[g] += 1

            # 모든 보석을 찾은 경우
            if len(t) == len(s):
                end = id
                start = id + 1
                break
        else:
            # break안 탄 경우 더 이상 답은 없음.
            break
        
        # 앞 번호를 없애가며 최적의 길이 만들기
        for i in range(end_start, end + 1):

            t[gems[i]] -= 1

            # 최적의 길이 도달하면, 해당 정보 저장
            if t[gems[i]] == 0:
                del t[gems[i]]
                results.append([i + 1, end + 1])
                end_start = i + 1
                break
    
    # results의 최소 길이, 앞 우선으로 리턴
    return sorted(results, key=lambda x: (x[1] - x[0], x[0]))[0]            


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

# expected [9:11]
print(solution(["A", "B", "A", "A", "C", "A", "A", "B", "A", "B", "C"]))
# expected [4:6]
print(solution(["A", "B", "B", "A", "B", "C", "A", "B", "A", "B", "C"]))
