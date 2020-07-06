from itertools import permutations


n = '17'

a = set()
for i in range(len(n)):
    print(list(permutations(list(n), i + 1)))
    v = set(map(int, map("".join, permutations(list(n), i + 1))))
    print(v)
    a |= v

# permutations 함수의 2번째 인자 값이 총 몇개만 뽑을지를 정할 수 있다.
# permutations([1, 2, 3], 1) 이러면 1개씩 뽑아서 순열 생성 -> 1, 2, 3
# permutations([1, 2, 3], 2) 이러면 2개씩 뽑아서 순열 생성 -> (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)

# python에 알고리즘 관련 라이브러리 확실히 매우 잘되어 있다는 것을 보여준다.

print(list(permutations([1, 2, 3], 2)))

print(a)
