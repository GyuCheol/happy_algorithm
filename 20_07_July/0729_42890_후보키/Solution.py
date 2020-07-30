
def solution(relation):

    # 각 컬럼이 희소성을 만족하는지 검사
    def is_unique(columns):
        s = set()

        for row in relation:
            tup = tuple(row[c] for c in columns)

            if tup in s:
                return False
            else:
                s.add(tup)

        return True

    # 현재 column이 최소성을 만족하는지 검사 ()
    def is_minimum(columns):
        
        for a in answer:
            if columns & a >= a:
                return False
        
        return True

    comb = 1
    l = len(relation[0])
    answer = []

    while comb < 2 ** l:
        # 10진(comb)값을 2진 배열로 변환한다.
        columns = [i for i in range(l) if comb & (1 << i) != 0]

        # 최소성, 유일성 모두 만족하는 경우
        if is_minimum(comb) and is_unique(columns):
            answer.append(comb)

        comb += 1

    return len(answer)


# exptected 2
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
