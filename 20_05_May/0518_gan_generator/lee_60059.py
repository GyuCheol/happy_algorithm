
# https://programmers.co.kr/learn/courses/30/lessons/60059

def rotate_to_right(key):
    l = len(key)
    cpy = [[0 for i in range(l)] for j in range(l)]

    for i in range(l):
        for j in range(l):
            cpy[j][l - i - 1] = key[i][j]

    return cpy

def check_map(key, lock, s_x, s_y):
    lock_len = len(lock)
    key_len = len(key)
    count = 0

    for y in range(key_len):
        for x in range(key_len):
            d_x = s_x + x
            d_y = s_y + y

            if 0 <= d_x < lock_len and 0 <= d_y < lock_len:
                if key[y][x] == 1 and lock[d_y][d_x] == 0:
                    count += 1
                elif key[y][x] == 1 and lock[d_y][d_x] == 1:
                    return -1
    
    return count

def check(key, lock, key_cnt):
    lock_len = len(lock)
    key_len = len(key)
    gap = -(key_len - 1)
    gap_max = lock_len + (key_len - 1)

    for s_x in range(gap, gap_max):

        for s_y in range(gap, gap_max):
            
            if check_map(key, lock, s_x, s_y) == key_cnt:
                return True

    return False

def getKeyCount(lock):
    cnt = 0
    l = len(lock)

    for y in range(l):
        for x in range(l):
            if lock[y][x] == 0:
                cnt += 1

    return cnt

def solution(key, lock):
    key_cnt = getKeyCount(lock)

    if check(key, lock, key_cnt):
        return True

    for i in range(3):
        key = rotate_to_right(key)

        if check(key, lock, key_cnt):
            return True
        
    return False

print(solution(
    [
        [0, 0, 0], 
        [1, 0, 0], 
        [0, 1, 1]],
    [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]))

print(solution(
    [
        [1, 1, 0], 
        [1, 0, 0], 
        [0, 0, 0]],
    [
        [1, 1, 1],
        [0, 0, 0],
        [1, 1, 1]]))

print(solution(
    [
        [1, 1, 1], 
        [1, 0, 0], 
        [0, 0, 0]],
    [
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0]]))

print(solution(
    [
        [0, 0, 1, 1], 
        [0, 0, 0, 1], 
        [0, 0, 0, 0],
        [0, 0, 0, 0]],
    [
        [1, 1, 0],
        [1, 1, 0],
        [1, 1, 0]]))
        
print(solution(
    [
        [0, 0, 1, 1], 
        [0, 0, 0, 1], 
        [0, 0, 0, 0],
        [0, 0, 0, 0]],
    [
        [1, 1, 0],
        [1, 0, 0],
        [1, 1, 1]]))

print(solution(
    [
        [1, 1, 1, 1], 
        [1, 1, 1, 1], 
        [1, 1, 1, 1],
        [1, 1, 1, 1]],
    [
        [1, 1, 0],
        [1, 0, 0],
        [1, 1, 1]]))


print(solution(
    [
        [1, 1, 1, 1], 
        [1, 1, 1, 1], 
        [1, 1, 1, 1],
        [1, 1, 1, 1]],
    [
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1]]))

print(solution(
    [
        [1, 1, 0], 
        [0, 1, 0],
        [1, 1, 0]],
    [
        [1, 1, 1],
        [0, 0, 0],
        [0, 1, 0]]))