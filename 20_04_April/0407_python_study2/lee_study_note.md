
# 4] 흐름 제어문 (Control Flow Statement)

## if문 : 다른 언어와 특이한점 없음. (keyword : elif, else)

## for문
for문은 Pascal, C 언어와는 조금 다름.
파이썬의 for문은 시퀀스의 아이템을 반복함.

## while문
```
while_stmt ::=  "while" assignment_expression ":" suite
                ["else" ":" suite]
```
else문의 경우, while 종료 이후 실행되는 마지막 줄.
가독성의 문제로 잘 쓰이진 않는다.

## range 함수
수열 시퀀스를 생성하는 함수로, 재밌는 점은 실제 물리적인 공간을 쓰지 않는다는 것. range(5)를 쓴다고해서 5개짜리 배열 공간이 생성되는 것이 아니다.

인자에 따라 다양한 수열 시퀀스를 생성한다.
range(5) 0, 1, 2, 3, 4

range(0, 10, 3) 0, 3, 6, 9
0 begin  10 until 3 step

enumerate() 함수를 이용하면, index와 함께 시퀀스를 순회시킬 수 있다.

```python
for i, c in enumerate(['A', 'B', 'C']):
    print(i, c)
```

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

함수의 첫번째 문으로는 한 문자열이 선택적으로 될 수 있다. (함수 설명 주석)
Docsting : https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings

함수의 실행은 함수 내의 모든 지역 변수들을 위한 symbol table을 만든다.
(모든 함수 내 지역 변수는 table에 저장)
변수를 참조할 때는 먼저 현재 symbol table을 본 후,
전역 table을 본 뒤 마지막으로 내장된 table을 본다.

**globael** 키워드

**nonlocal** 키워드

함수를 정의한는 것도 함수 이름을 현재 symbol 테이블에 나타낸다.
return이 없는 함수를 procedure라고도 하지만
return이 없다고 해서 반환 값이 없는건 아님.
None이라는 것을 반환함.

## 함수 정의 더 살펴보기

### Argument 기본 값

### 중요 사항
함수의 기본 값은 한번만 계산되므로, 아래와 같은 코드는 예상되지 못한 결과를 받게됨.
```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```

이에 대한 대안으로 아래의 코드가 있다.

```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

## Keyword Arguments

함수는 keyword arguments를 사용하여 호출될 수 있다.
(kwarg=value 형식)

즉 optional의 paramter의 이름을 사용하여 지정할 수 있다.
아래와 같이 말이다.
```python
print(out='1')
```

**name 형식의 매개변수는 가변 길이를 갖는 parameter table을 가질 수 있다.
(*name의 경우는 **보다 먼저 정의해야함)

*name의 경우는 매개변수 key를 가지지 않는 가변적인 인자를 받는다.

## 특수 매개변수

### 위치 전용? 
/ 기호 앞의 모든 인자는 해당 인자 위치에 맞게 호출되어야 하는 것을 뜻하는듯.

### 키워드 전용?
\* 앞의 인자는 위치나 키워드 전용으로 쓸 수 있다는 것으로 보임.
\* 뒤의 인자는 keyword를 무조건 써야하는 것으로 보임.

## 사용 지침

매개 변수 이름을 사용자가 사용할 수 없도록 하기 위해서는 위치 전용을 사용. 매개 변수 이름이 의미 없고, 함수 호출 인자 순서를 강제하려고 할 때 유용.

이름이 의미가 있고, 함수 정의 이름을 명시적으로 지정하기 위해서는 키워드 전용을 사용함.

API의 경우는 위치 전용이 권장됨 (API변경 발생 방지)

# 임의의 인자 목록
*name을 이용하여 가변 길이 인자를 받을 수 있다.
가변 길이(*name)는 매개 변수 목록의 마지막에 정의함.

## 인자 목록 언패킹
인자들이 이미 리스트나 튜플에 있어 인자들을 요구하는 함수 호출을 위해 언패킹하는 경우가 있다.
그런 경우 쓰는 방법.
튜플의 경우 *, dict의 경우 **을 쓰면 된다. 

```python
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]

...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```

## 람다 표현식

lambda 키워드를 이용해서 작은 크기의 익명 함수를 만들 수 있다.

```python
lambda a, b: a+b
```

이것은 다음과 같다.

```py
def func(a, b):
    return a+b
```

람다식을 이용하므로 지루한 함수 정의 코드를 절약할 수 있게됨.

## Docs Strings

함수를 설명하는 설명 문자열에 대한 규약.
첫줄은 항상 짧아야 한다. 간결하게 함수의 목적을 서술.
함수의 이름만으로 이해가 된다면 예외이다.
두번째 줄은 비게하고, 세번째부터 다시 서술.

python의 parser가 이 설명을 읽어 해당 함수의 멤버 __doc__으로 docs strings을 가져올 수 있다.

## Annotation

Annotation은 선택적인 메타데이터 정보이다.
이것은 __annotations__멤버로 dict 형태의 자료구조로 담긴다.

함수의 ->, class을 정의하는 것도 일종의 함수가 무엇을 반환하는지 알려주는 메타데이터에 해당된다.

```py
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

# 코딩 스타일

- tab은 사용 금지, white space 4자로 들여쓰기 할 것. (대부분의 IDE가 지원한다.)
- 각 줄은 79자를 넘기지 않도록, 줄넘김 권장
- 큰 코드 블록 사이 빈 줄을 넣어 분리.
- 가능하다면 주석은 별도 줄로 분리
- docstring을 사용 (매 함수, 클래스)
- 괄호 안쪽은 공백을 쓰지말고, 연산자와 콤마 뒤에는 공백을 넣자.
- 클래스 함수에 일관성 있는 이름을 붙이기. 클래스는 UpperCamel, 함수 메서드는 lowercase_with_underscores
- 특별한 국가 인코딩 사용 금지, UTF-8이 기본
- 웬만하면 영어를 쓸 것.

