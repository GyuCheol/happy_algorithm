# 5] 자료구조 (Data Structure)

## List 멤버 함수
### append(x)
리스트의 마지막 위치에 x 요소를 추가함.
아래와 동일한 코드
```py
a[len(a):] = [x]
```

### extend(iterable)
열거가능한 list를 끝에 확장함.
```py
l = []
l.extend([1, 2, 3])
l.extend(range(3))
print(l)
[1, 2, 3, 0, 1, 2]
```

### insert(i, x)
i는 추가될 인덱스 위치, x는 추가될 요소.

해당 i 앞에 추가된다.
```py
l = [1, 2]
l.insert(0, 0)
print(l)
[0, 1, 2]
```

### remove(x)
해당 요소를 제거한다. 위치 i가 아니니, 참고.

제거된 후 뒤에 요소들이 shift됨.

### pop([i])
i가 없는 경우 맨 끝의 요소를,

i가 있는 경우 해당 위치의 요소를 반환하고 해당 위치를 remove시킴.

### clear()
내부의 모든 요소를 제거한다. 아래 코드와 같은 동작.
```py
l = [1, 2, 3]
del l[:]
```

### index(x[, start, [end]])
x 요소를 list 내에서 찾는다.

start, end가 있는 경우 해당 index 안에서 찾는다.

### count(x)
list 내부 x 요소 개수를 반환.

*list 자체 길이는 len(x) 함수를 이용해서 길이를 구할 수 있음.

### *sort(key=None, reverse=False)
내부 요소를 정렬한다. key가 없는 경우 자체 개체의 비교 함수로 정렬을 수행.

reverse의 기본 오름차순 정렬인데, True를 지정하면 내림차순 정렬이 된다고 보면 됨.

sorted 함수는 별도 key를 지정할 수 없지만 이것은 key 지정이 가능.

*만약, 내부 개체의 타입이 다른 경우, 정렬 수행이 되지 않는다. (['a', 1, 5, 'ZXC'])

### copy()
shallow copy를 실행하여 사본을 생성.

## List를 stack처럼 활용

append와 pop 함수를 이용하면 된다.

## List를 queue처럼 활용

append와 popleft 함수를 이용하면 된다.

## List Comprehensions
List Comprehensions은 간결하게 list를 생성하는 방법을 제공한다.

다음 코드를 참고
```py
squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
```

### 중첩된 List Comprehensions
아래 코드처럼, 기존 list를 참조하는 list comprehensions도 가능하다.

아래 예시는 배열의 행열을 반전한 예시 (transposed)
```py
l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
[[x[i] for x in l] for i in range(4)]
```

zip 함수를 이용한 방법. (언패킹을 이용하여 각 배열 요소를 인자로 넣음.)

```py
l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
list(zip(*l))
```

## del 키워드
pop() 메소드나 remove() 메소드 외에
del 키워드를 이용하여 요소를 제거할 수 있다.
del 키워드는 아예 변수 자체를 제거할 수도 있다.

```py
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

## tuples과 sequences 

튜플은 단순히 아래처럼도 정의 될 수 있음.
```py
t = 1, 2, 3, 4
t2 = t, (1, 2, 3, 4)
```

튜플은 immutable한 값이므로, read-only이다.

튜플로 assignment 연산자를 사용하면 튜플 아이템을 unpacking하여 할당하게 된다.
```py
t = 1, 2, 3
x, y, z = t
```

## Set
집합에 대한 자료구조도 지원한다.

집합은 중복이 없고, 정렬되지 않은(unordered) 자료구조이다.

수학 연산자를 지원한다 차집합(-) 교집합(&) 합집합(|) 여집합(^)

역시 list comprehension도 지원한다.

```py
s = {'apple', 'pear', 'orange'}
'apple' in s
s.delete('apple')
s.append('banana')
s2 = {x for x in 'abcddbbccdd' if x != a}
```

여기서 mutable한 Set을 만들고 싶다면 {}을 사용해서는 안됨.
set()을 이용하여 Set의 instance을 만들어야 add 메소드 사용이 가능하다.


## Dictionary
key:value의 table 형태인 Dictaionry도 지원한다.

튜플, 숫자, 문자열등은 key가 될 수 있다.

del 키워드를 이용하여 dict 내부 아이템을 제거할 수 있다.

append나 insert등의 함수가 없으므로 그냥 d['a'] = ~~~ 등으로 요소를 추가하여야 한다.

list 함수로 dict를 list화 시키면 key 값만으로 list를 만들게된다.

## 자료구조에 반복문 사용

dict의 경우 아래와 같이 반복문 사용이 가능하다.

튜플로서 순회가 가능.

```py
d = {'a': 1, 'b': 2}

for k, v in d.items():
    print(k, v)

```

zip 함수를 이용하여 시퀀스를 붙인 순회도 가능하다.
```py

for i, j in zip(range(5), range(5)):
    print(i, j)

```

sorted를 이용하여 정렬된 새 배열을 만든 순회도 가능.

enumerate 함수는 순회하면서 index를 tuple로 준다.

```py
for i, k in enumerate(['a', 'b', 'c']):
    print(i, k)
```

## 특이한 조건 연산자

in, not in은 시퀀스에 해당 요소가 존재하는지 검사한다.

is, not is는 해당 요소가 정말로 같은 요소인지 (같은 것을 참조하는지?) 검사한다.

is, not is 연산자는 mutable object에만 의미가 있다.

and, or 연산자는 이렇게도 응용될 수 있다. (or, and로 참이 나오면 해당 참 값을 반환?)

아래 코드의 a는 'A'가 된다.
```py
a = '' or 'A' or 'B'
```

:= 바다 코끼리 연산자 (연산자 우선 순위가 매우 낮다)

표현식 안에서의 대입 연산과 해당 값을 반환하여 쓸 수 있다고 보면 된다.

```py
if a := 5 == 5:
    print(a)

if (a := 5) == 5:
    print(a)

if a := 5:
    print(a)
```

## 시퀀스 끼리의 비교

아래는 모두 True를 리턴함.

시퀀스의 경우 각 요소별로 비교를 수행하여 문자열 비교 같은 결과가 나오고.

'ABC' < 'C' < 'Pascal' ... 처럼 여러 요소들을 연달아 대소비교하는 것은 모든 비교 조건이 만족하는지 확인.

```py
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```
