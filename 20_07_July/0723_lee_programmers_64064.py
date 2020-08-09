# 7월 23일

# 불량 사용자
# https://programmers.co.kr/learn/courses/30/lessons/64064
# 2019 카카오 개발 인턴십 - lv3

# user_id와 banned_id를 full matching하면서
# 각각 banned_id에 해당하는 {}를 만들어 어떤 user들이 매칭되는지 추가해놓기
# dfs로 경우의 수를 탐색

# 문제를 제대로 읽자.... ㅠㅠ
# 문제를 대충 읽고 풀려니 다시 제대로 읽었을 때 문제의 내용이 엄청 변했다.
# lv3치곤 너무 쉬운데 했더니 다시 제대로 읽었더니 lv3인 이유를 알게된 것.

# yield 구문 연습

# O(N^2)?



def solution(user_id, banned_id):
    ban_dict = {ban:[] for ban in banned_id}

    for user in user_id:
        # match된 user_name ban_list에 추가
        for ban in ban_dict.keys():
            cnt = 0

            for u, b in zip(user, ban):
                if b == '*' or u == b:
                    cnt += 1
        
            # 매칭이 되는 것이니, ban id 반환
            if cnt == len(ban) == len(user):
                ban_dict[ban].append(user)

    registered = set()

    def get_hash(visited):

        r = 0

        for v in visited:
            r += hash(v)
        
        return r

    # 각각 경우의 수 찾기 (dfs)
    def dfs(id, visited):

        if id == len(banned_id):
            
            h = get_hash(visited)

            if h not in registered:
                registered.add(h)
                return 1

            return 0

        lst = ban_dict[banned_id[id]]

        if len(lst) == 0:
            return 0

        cnt = 0

        for user in lst:
            if user not in visited:
                visited.append(user)
                cnt += dfs(id + 1, visited)
                visited.remove(user)
            
        return cnt
    
    return dfs(0, [])

# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))

