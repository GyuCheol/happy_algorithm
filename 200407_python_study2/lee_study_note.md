
# 4] 흐름 제어문 (Control Flow Statement)

## if문 : 다른 언어와 특이한점 없음. (keyword : elif, else)

## for문
for문은 Pascal, C 언어와는 조금 다름.
파이썬의 for문은 시퀀스의 아이템을 반복함.

## whilte문
    while_stmt ::=  "while" assignment_expression ":" suite
                    ["else" ":" suite]

else문의 경우, while 종료 이후 실행되는 마지막 줄.
가독성의 문제로 잘 쓰이진 않는다.

## range 함수
수열 시퀀스를 생성하는 함수로, 재밌는 점은 실제 물리적인 공간을 쓰지 않는다는 것. range(5)를 쓴다고해서 5개짜리 배열 공간이 생성되는 것이 아니다.

인자에 따라 다양한 수열 시퀀스를 생성한다.
range(5) 0, 1, 2, 3, 4

range(0, 10, 3) 0, 3, 6, 9
0 begin  10 until 3 step

enumerate() 함수를 이용하면, index와 함께 시퀀스를 순회시킬 수 있다.

    for i, c in enumerate(['A', 'B', 'C']):
        print(i, c)

실제 수열 시퀀스를 물리적인 배열 공간으로 만들고자 한다면, 
list() 함수를 이용하면 된다. (list함수 등 다양한 자료 구조에 대한 내용은 Data Structure 챕터에서 다룸)

이런 enumerate한 시퀀스는 sum() 등의 집계 함수를 통해 연산 결과를 만들 수 있다.

## break, continue문
break는 현재 flow 블록을 끊는(break out) 구문,
이 경우 loop의 else 블록이 실행되지 않는다.

continue는 현재 flow 블록의 다음 절차로 건너뛰는 구문.

## pass문
블록에서 아무것도 명령이 없거나 비었을 때 
최소 1줄의 문장이 필요하기에 쓰는 문.
또는 나중에 구현하기 위해 멤버 함수를 추상적 단계에서 생성하기 위해 사용.

## 함수 정의하기
**def** 키워드는 한 함수의 정의를 나타낸다.
반드시 이 키워드 뒤에는 함수의 이름과 parameters에 대한 것이 선언되어야 한다.
이 다음 줄부터는 indented된 문장이 요구됨.


