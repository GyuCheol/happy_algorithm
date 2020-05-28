
# https://www.acmicpc.net/problem/2309

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
