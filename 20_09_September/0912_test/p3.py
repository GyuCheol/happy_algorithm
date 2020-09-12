from bisect import bisect_left

class Info:

    def __init__(self, lang, job, rank, food, score):
        self.lang = lang
        self.job = job
        self.rank = rank
        self.food = food
        self.score = score

        self._list = (lang, job, rank, food)
    
    def get_cases(self):
        
        b = 0

        while b < (2**4):
            tmp = []

            for i in range(4):
                if (b & (1 << i)) != 0:
                    tmp.append(self._list[i])
                else:
                    tmp.append('-')
                    
            yield ''.join(tmp)

            b += 1


def solution(info, query):
    answer = []
    cases_map = dict()

    def parse(info):
        id = 0
        lang = info[id]

        # language
        if lang == 'c':
            id += 4
        elif lang == 'j':
            id += 5
        else:
            # python
            id += 7
        
        job = info[id]

        if job == 'f':
            id += 9
        else:
            # backend
            id += 8
        
        rank = info[id]
        id += 7

        food = info[id]

        if food == 'c':
            id += 8
        else:
            # pizza
            id += 6

        return lang, job, rank, food, int(info[id:])

    def query_parse(query):
        id = 0
        key = [query[0]]

        if key[0] == 'c':
            id += 8
        elif key[0] == 'j':
            id += 9
        elif key[0] == 'p':
            id += 11
        else:
            id += 6
        
        key.append(query[id])

        if query[id] == 'b':
            id += 12
        elif query[id] == 'f':
            id += 13
        else:
            id += 6

        key.append(query[id])

        if query[id] == 'j' or query[id] == 's':
            id += 11
        else:
            id += 6

        key.append(query[id])

        if query[id] == 'p':
            id += 6
        elif query[id] == 'c':
            id += 8
        else:
            id += 2

        return ''.join(key), query[id:]

    for inf in info:
        candidate = Info(*parse(inf))

        for case in candidate.get_cases():
            if case in cases_map:
                cases_map[case].append(candidate.score)
            else:
                cases_map[case] = [candidate.score]

    # sorting
    for v in cases_map.values():
        v.sort()
    
    for q in query:
        key, score = query_parse(q)

        if score == '-':
            if key in cases_map:
                answer.append(len(cases_map[key]))
            else:
                answer.append(0)
        else:
            score_int = int(score)

            if key in cases_map:
                id = bisect_left(cases_map[key], score_int)
                answer.append(len(cases_map[key]) - id)
                
            else:
                answer.append(0)

        

    return answer



print(solution(
    ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
    ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

