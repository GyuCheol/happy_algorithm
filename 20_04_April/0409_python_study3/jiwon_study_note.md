# 5] 자료 구조(Data Structure)

## 5.1. 리스트(List)

list.append(X): 리스트의 끝에 항목 추가
list.extend(iterable) : 리스트의 끝에 iterable의 항목 추가
list.insert(i,x): 주어진 위치에 항목 삽입
list.remove(x) : x와 값이 같은 첫번째 항목 삭제
list.pop([i]) = 주어진 위치의 항목 삭제 후 그 항목 반환
list.pop() : 마지막 항목 삭제 후 반환
list.clear() : 모든 항목 삭제 = del a[:] 
list.index(x[,start[,end]]): x와 값이 같은 첫번째 항목의 0부터 시작하는 인덱스 반환
list.count(x) : x 등장횟수
list.sort(key = None, reverse = False): 항목 제자리 정렬
list.reverse(): 요소 제자리에서 뒤집기
list.copy(): list 카피
Shallow copy vs deep copy : 리스트 메모리주소 복사(내용 복사x) vs copy.deepcopy 내용물 다 저장

## 5.1.1. 리스트를 스택으로 사용하기(LIFO)
```python
stack = [3,4,5]
stack.append(6)
print(stack)
stack.pop()
print(Stack)
```

## 5.1.2. 리스트를 큐로 사용하기(FIFO)
이 방법은 효율적이진 않다. collections.deque를 사용하기
```python
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
>>>queue.popleft()
'Eric'
>>>queue.popleft()
'John'
>>>queue
deque(['Michael','Terry','Graham'])
```

## 5.1.3. 리스트 컴프리헨션
연산 또는 조건을 만족하는 요소들로 구성된 리스트.
```python
squares = list(map(lambda x: x**2, range(10)))
```
```python
>>>[(x,y) for x in [1,2,3] for y in [3,1,2] if x! = y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
튜플이면 반드시 괄호로 둘러싼다.(x,y)
range(n) : 요소 하나씩 받음.
zip(range(n),range(m)): 요소 두개 받기 가능

listname.sort() : 사본 생성x 자신의 메모리가 정렬
sorted(listname) : 사본을 만들어서 해당 사본 메모리가 정렬

```python
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]

```
## 5.1.4. 중첩된 리스트 컴프리헨션
```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

##이 예시는 아래와 같다.

>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

```
## 5.2. del 문
```
>>>a = [1,2,3,4]
>>>del a[0]
>>>a
[2,3,4]
>>>del a
[]
```

## 5.3. 튜플과 시퀀스
튜플 : 불변값. 괄호로 둘러싸인다. 언패킹과 인덱싱으로 access
리스트: 가변값. 리스트에 대한 iteration으로 access

## 5.4. 집합
집합: 중복요소가 없는 순서 없는 컬렉션.
{'1','2','3'} 또는 set() : 빈 집합 만들때는 set() 사용
set1{'a','ab'} --> 공집합일 때 추가 불가능.
set2s = set() -->mutable
```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

집합 컴프리헨션 : 
>>>a = [x for x in 'abracadabra' if x not in 'abc']
>>>a
{'r','d'}

## 5.5. 딕셔너리

{key:value}

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> 'guido' in tel
True
```
dict() : key-value 쌍으로부터 직접 딕셔너리 생성
>>>dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

딕셔너리 컴프리헨션
```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

from collections import Counter

/ for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
```

## 5.6.루프 테크닉

item() : key와 value를 동시에 얻는다.
```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```
enumerate() : 위치 인덱스와 value를 동시에 얻는다.
```python
>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```
zip() : 둘 이상의 시퀀스를 부여한다.

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

resereved() : 정방향 지정 후 사용, 거꾸로 호출
sorted() : 순차적 정렬
루프 돌고 있는 리스트 변경이 필요할 경우 새로 만든다.

## 5.7. 조건 더 보기
while과 if의 조건에서는 비교 및 모든 연산자 사용가능.

in, not in : 값 있는지 검사
is, is not : 두 객체가 같은지 검사

## 5.8. 시퀀스와 다른 형들 비교
사전식 순서. 