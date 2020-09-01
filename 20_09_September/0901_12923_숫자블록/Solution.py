
def solution(begin, end):

    def find_number(n):
        if n == 1:
            return 0

        sq = int(n ** 0.5)
        i = max(2, n // 10000000)

        while i <= sq:
            if n % i == 0 and (n // i) <= 10000000:
                return n // i

            i += 1

        return 1

    return [find_number(i) for i in range(begin, end + 1)]

# print(solution(90, 100))
# print(solution(1, 10))
# print(solution(1000000000-9999, 1000000000))
print(solution(1000000000-10, 1000000000))

