# 역시 풀어봤던거 ㅇ.ㅇ

def solution(begin, end):

    def find_number(n):

        if n == 1:
            return 0

        i = max(2, n // 10000000)
        sq = n ** 0.5

        while i <= sq:
            
            if n % i == 0:
                tmp = n // i
                if tmp <= 10000000:
                    return tmp

            i += 1

        return 1

    return [find_number(n) for n in range(begin, end + 1)]



# print(solution(1, 10))
print(solution(1000000000 - 10, 1000000000))