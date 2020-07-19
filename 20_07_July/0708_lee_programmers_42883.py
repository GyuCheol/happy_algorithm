# 7월 8일

# 큰수만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883
# 그리디 - lv2

# greedy 적인 방법으로 최대한의 결과가 나올 수 있도록 탐색하여야 한다.
# 가능한 자릿수에 올 최댓값을 구해가며 list를 만들면 된다.
# 문제점은 C++이나 java로 짜면 통과할 로직이
# python 고유의 느릿함으로 시간 초과가 걸린다..
# python으로 최대한 빠르게 짤 수 있도록 최적화해야 한다

# 시간 복잡도 : 평균 O(NlogN) 최악 O(N^2)

def solution(number, k):
    l = len(number)
    # string 비교 성능 때문인가? 싶어서 int로 변환 (확실히 성능이 미약하게 상승함)
    numbers = list(map(int, number))
    answer = []
    id = 0
    
    # k의 위치가 number 길이를 넘어갈 때까지
    # k 위치가 넘어가면 나머지는 무조건 추가할 수 밖에 없으므로.
    while k < l:

        # python이 드럽게 느려서 자꾸 10번에서 timeout이 난다... 최적화 최적화..
        # 똑같은 로직을 java로 하면 통과한다..
        # 일반 loop보다 max + index가 훨씬 빠르다.. 왜?

        m = 0
        for i in range(id, k + 1):
            if m < numbers[i]:
                m = numbers[i]
                id = i + 1
        m = max(numbers[id:k + 1])
        id = numbers.index(m, id) + 1
        
        answer += number[id - 1]
        k += 1

    answer += number[k:]

    return ''.join(answer)

print(solution('1924', 2))
print(solution('999', 2))
print(solution('1231234', 3))
print(solution('4177252841', 4))

number = "1234567890"*100000
k = 999999

print('A')
solution(number, k)
print('A')

def solution(number, k):
    length = len(number)
    if length > k:
        m = 0
        for cnt in range(k):
            for idx in range(m, length-1):
                if number[idx] < number[idx+1]:
                    number = number[:idx] + number[idx+1: ]
                    length -= 1
                    if idx > 0:
                        m = idx-1
                    break
            else:
                number = number[:length-k+cnt]
                break
        return "".join([str(i) for i in number])
    else:
        return "0"