# 6] 모듈 (Module)

파이썬에서는 각각의 스크립트가 담긴 하나의 파일을 Module(.py)이라고 다룬다.

여기서 현재 런타임의 모듈 이름을 얻고자 할 때는 \_\_name__을 이용하여 현재 모듈로 로드된 것인지 main으로 로드된 것인지 확인할 수 있다. (메인의 경우 \_\_main__을 리턴함)

현재 경로의 다른 파이썬 파일을 불러오고 싶은 경우, import '파일명'을 적어주면 된다. 이때 확장자 .py는 생략한다.

아래 예시
```py
'''module.py'''

def sum(a, b):
    return a + b

```

```py
import module

print(module.sum(5, 5))
```

모듈은 함수 정의만 불러오는 것이 아닌, load되는 타이밍에 실행가능한 문장 또한 실행한다.

각 모듈들은 자신의 private symbol 테이블을 가지고 있어 각 모듈간 전역 변수 영역은 충돌되지 않는다.

만약 전역 변수를 참조하고 싶다면, ```modulename.itemname```을 사용하여 호출하면 된다.

만약 아래와 같이 사용했다면 module이라는 모듈 이름을 local symbol 테이블에 만들지 않는다.

```py
from module import sum

sum(5, 5)
```

아래와 같은 예시도 마찬가지이다. (다만 권장하지는 않는다고 함)

```py
from module import *

sum(5, 5)
```

as를 이용하여 별칭을 부여할 수도 있다.

```py
import module as m

m.sum(5, 5)
```

요렇게도 가능.

```py
from module import sum as omg

omg(5, 5)
```

*각 모듈은 세션마다 단 한번만 load되므로 재실행하거나 ```importlib.reload()```을 사용하여야 한다.

## 모듈 검색 경로
먼저 built-in 모듈을 먼저 찾는다.

그 이후 현재 경로에서 찾고, 만약 찾지 못했다면 sys.path의 경로들에서 해당 모듈을 찾는다.

초기화 이후, sys.path는 수정될 수 있다. (기타 경로들을 변경 가능)

## 컴파일된 파이썬 파일

모듈 로딩의 속도 향상을 위해 __pycache__ 디렉터리에 각 모듈의 컴파일된 버전을 ```module.version.pyc```라고 캐싱한다.

만약 CPython 3.3에서 spam.py 이 캐싱된다면 이렇게 된다.
```__pycache__/spam.cpython-33.pyc```

## Standard Module

### sys 모듈

```py
import sys

sys.ps1 = 'C> '
sys.ps2 = '.l.'

```

### dir() 함수

모듈이 정의하는 이름들을 찾는 데 사용된다.

문자열들의 정렬된 리스트를 돌려준다.

## Package (패키지)

패키지는 파이썬의 모듈들을 구조화하는 방법이다.

해당 패키지 폴더 명에 \_\_init__.py 파일이 있다면,

해당 패키지를 로드할 때 init.py의 스크립트가 실행이 된다. (또는 정의된 함수를 symbol 테이블에 로드)

폴더 안에 폴더를 넣어 패키지 내부의 서브 패키지를 포함시킬 수 있고, 

해당 서브 패키지 끼리는 아래와 같이 참조한다. (상대 경로 정의 ., .. 등)

```py
from . import echo
from .. import formats
from ..filters import equalizer
```
