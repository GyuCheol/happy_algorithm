# 십진수->2진수 를 자릿수 n 맞춰서 출력-> 문자열 바꿀때만 n자리 맞추면 됨
# 비트마스크로 결과물 비트값 구함. 이중for문? 놉!
# 1->'#', 0-> ' '로 변환
# https://programmers.co.kr/learn/courses/30/lessons/17681

# 비트연산문제 정석풀이
def solution(n, arr1, arr2):
    result = []
    for a, b in zip(arr1,arr2):
        tmp = a | b
        s = '' # 문자

    for i in range(n-1, -1, -1) 
    # 비트 첫번째 자리부터 왼쪽으로 카운트    
        if tmp & (1<<i)  = 1: # 왼쪽으로 1비트 이동
            s += '#'
        else:
            s += ' '
    result.append(s)

    return result

# python이라 가능한 꼼수풀이

def solution2(n,arr1, arr2):
    result = []
    for a, b in zip(arr1,arr2):
        tmp = bin(a | b)[2:] # 0b0001...에서0b 컷

        result.append(tmp.replace('1','#').replace('0',' '))

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))