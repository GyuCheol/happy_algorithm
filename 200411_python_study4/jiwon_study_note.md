## 6. Modules
이전에 사용한 함수,변수들을 파일에 넣고 스크립트와 인터프리터에서 사용하는 방법.

```python
def fib(n) --> fibo.py로 저장.
import fibo 로 호출
```
모듈의 이름은 전역 변수 __name__으로 제공된다.

## 6.1. More on Modules
이름변경 : from fibo import fib as fibonacci

## 6.1.1. Executing modules as scripts

## 6.1.2. The Module search path

import spam -> interpreter가 내장 모듈을 서치.
발견되지 않으면 sys.path로 주어지는 디렉토리에서 서치

## 6.1.3. "Compiled" Python files
__pycache__ 디렉터리에 각 모듈의 컴파일버전을 modul.version(파일 형식, 파이썬 버전).pyc라는 이름으로 캐싱.

## 6.2. Standard Modules
sys.ps1 , sys.pas2 : 기본과 보조 프롬프트로 사용되는 문자열 정의.

```python
sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```
sys.path : 인터프리터의 모듈 검색 경로를 결정하는 문자열들의 리스트. 
```python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

## 6.3. The dir() function
dir() : 모듈이 정의하는 이름 서치. 문자열들의 정렬된 리스트를 반환한다.

```python
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
```

인자가 없는 경우 현재 정의한 이름을 나열한다.
```python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```
## 6.4.Packages
<<점으로 구분된 모듈 이름>>을 사용하여 모듈 이름 공간을 구조화한다.
A.B : A라는 이름의 패키지에 있는 B라는 이름의 서브 모듈.

## 6.4.1. Importing * From a Package
from sound.effects import * : ?
패키지의 __init__.py 코드가 __all__ 이라는 이름의 목록을 제공하면, from sound.effects import * 는 __all__ 을 import하는 모듈 이름들의 목록으로 받아들인다.
__all__ = ["echo", "surround", "reverse"]
위 서브 모듈들을 import한다.

__name__ <- __ : private의 뜻.
__name__if 'main' : python이 내 스크립트를 실행
__name__if (모듈이름) : module로서 import됨

## 6.4.2. Intra-package References
from sound.effects import echo = from .. import echo


## 6.4.3. Packages in Multiple Directories
__path__. : 패키지의 __init__.py 를 실행하기 전 이 파일이 들어있는 디렉토리의 이름을 포함하는 리스트로 초기화된다.

__name__ symbol table
__init__.py  현재 package에서 초기화될때 실행해야 하는 스크립트인지?
