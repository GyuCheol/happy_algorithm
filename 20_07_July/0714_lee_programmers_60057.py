# 7월 14일

# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057
# 2020 카카오 블라인드 채용 - lv2

# 가능한 문자열 압축을 모두 시도해서, 가장 짧은 길이가 되는 문자열 찾기
# 살짝 로직이 복잡하면서도 단순하다.
# 각 길이를 분할한 단어를 list에 넣고
# 연속된 단어가 나오면 pop 한 후 cnt를 포함시켜서 반복한다.
# 이후 완성된 list를 join하여 길이 비교

# 시간 복잡도 O(N^2)


def solution(s):
    answer = len(s)

    l = len(s) // 2

    for i in range(l, 0, -1):
        tmp = []
        last_splitted = ''
        cnt = 0
        id = 0

        # 나눈 문자열 집어 넣기
        while id < len(s):
            t = s[id:id+i]
            
            if t == last_splitted:
                cnt += 1
                tmp.pop()
                tmp.append(f'{cnt + 1}{t}')
            else:
                cnt = 0
                tmp.append(t)

            last_splitted = t
            id += i

        tmp = ''.join(tmp)

        if len(tmp) < answer:
            answer = len(tmp)


    return answer

print(solution('aabbaccc'))
print(solution('a'))