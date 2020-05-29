
# 일곱난쟁이
# https://www.acmicpc.net/problem/2309

# 2중 루프를 이용한, 2개의 요소를 고르는 경우의 수를 모두 나열하여 풀이

height_list = [int(input()) for n in range(9)]

def run():
    for i in range(9):
        for j in range(i + 1, 9):
            tmp = height_list[:] # O(n)

            tmp1, tmp2 = height_list[i], height_list[j]

            tmp.remove(tmp1)
            tmp.remove(tmp2)

            if sum(tmp) == 100:
                # 찾음!
                tmp.sort()

                for height in tmp:
                    print(height)
                    
                return

run()
