
참고자료 : https://realpython.com/primer-on-python-decorators/

# Higher-Order Function란? (고차함수)

함수를 인자로 받을 수 있고, 함수를 결과로 반환할 수 있다.

함수를 다루는 함수!

```python
>>> def twice(f):
...     def result(a):
...         return f(f(a))
...     return result

>>> plusthree = lambda x: x + 3

>>> g = twice(plusthree)
    
>>> g(7)
13
```

# Decorator

데코레이터는 higher-order-functions을 부르는 간단한 문법이다.

정의에 따르면, 데코레이터는 다른 함수를 가지고 그 행동을 확장하는 함수이다.

이것을 이해하기는 어렵지만, 예제를보며 이해할 수 있을 것임.

## Functions

Decorator를 이해하기전, 먼저 함수가 어떻게 동작하는지 먼저 이해해야한다.

함수는 주어진 인자에 따라 결과를 반환한다.

```python
>>> def add_one(number):
...     return number + 1

>>> add_one(2)
3
```

일반적으로, 파이썬에서 함수는 입력에 따른 결과 값을 반환하는 것 이외 부작용을 가질 수 있을 것이다.

print() 함수는 None을 반환한다.
암튼 데코레이터 이해를 위해, 어떤 함수든 input이 어떤 값으로 반환된다는 것을 이해하고 있자.

## First-Class Objects (일급 객체)

파이썬에서는 함수는 일급 객체이다.

이 말은 즉, 파이썬은 함수의 인자로 취급될 수 있다는 말이다.

```python
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")
```

위 코드를 보면, say_hello, be_awesome 함수는 일반 인자를 받아 결과 값을 반환한다.

하지만 greet_bob 함수는 함수를 받아 함수의 결과 값을 반환한다.

greet_bob 함수에 다른 함수를 인자로 넣으면 아래와 같이, 결과를 얻을 수 있다.

```python
>>> greet_bob(say_hello)
'Hello Bob'

>>> greet_bob(be_awesome)
'Yo Bob, together we are the awesomest!'
```

여기서 함수를 인자로 넘길 때 ()에 대한 호출 없이 넘겼다는 것에 유의하자.

이것은 함수 자체를 참조하기 위해 함수를 개체처럼 인자 값으로 넘긴 것이다.

## Inner Functions (내장 함수)

파이썬에서 함수 안에 함수를 정의하는 것은 가능하다!

```python
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()
```

이렇게 선언하면, second_child, first_child 함수는 parent 함수 안에서만 참조가능하게된다.

## 함수를 반환하는 예시

```python
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child
```

parent 함수의 인자에따라 반환하는 함수가 변경이 되는 예제이다.

```python
>>> first = parent(1)
>>> second = parent(2)

>>> first
<function parent.<locals>.first_child at 0x7f599f1e2e18>

>>> second
<function parent.<locals>.second_child at 0x7f599dad5268>
```

이 예제를 통해서 parent 함수에 내장된 함수를 반환하여 바깥 영역에도 사용할 수 있게한다.

## Simple Decorators

이제 파이썬에서의 데코레이터를 볼 준비가 되었다.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
```

위 코드에서 say_whee()를 호출하면 어떤 함수가 실행될지 예측해보자.

```python
>>> say_whee()
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
```

이제 기존의 say_whee라는 정의된 함수는 사라지고, 
say_whee는 my_decorator 함수 내에 내장된 함수가 되었다.
즉, 기존의 say_whee 부분이 my_decorator의 wrapper 내의 내장 함수가 되어버린 격

```python
>>> say_whee
<function my_decorator.<locals>.wrapper at 0x7f3c5dfd42f0>
```

다음의 예시를 보자

```python
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)
```

say_whee()를 22시 이후 실행하면 아무것도 실행하지 않지만,
7~22시 사이에는 say_whee 함수가 실행된다.

## 위의 동작을 간편히 지원해주는 문법적인 설탕!! (Syntactic Sugar!)

위의 동작을 위해 매번 저렇게 함수안에 함수를 지정하는 것은 매우 피곤하다.
그리고 함수를 인자로하여 함수의 결과가 달라질 수 있는 그런 부분을 작성할 때 이러한 데코레이터 기능이 필요할 것이다. (특정 상황에서는 다른 행동을 요구하는 경우?)

그래서 파이썬은 이것을 문법을 통해 지원해주는데 이것을 decorator라고 함.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
```

위와 같은 코드를 실행하면 say_whee 함수를 호출할 때 wrapper에 의해 호출이 일어난다.


## 함수 인자와 함께 데코레이터 사용하기

데코레이터 함수에 인자를 가변 인자로 설정해야 데코레이터가 안정적으로 인자를 전달한다.

즉, 아래와 같이 해야한다.

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_my_name(name):
    print(name)

say_my_name('A')
```

## 함수 리턴값이 있는 곳에 데코레이터 사용

```python
def do_twice_with_output(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
        
    return wrapper_do_twice
```

wrapper 함수에 반환 값을 넣어둔다.


## wrapper 함수의 식별 설정

```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
```

위 코드와 같이 설정을 해주어야 함수의 __name__을 참조할 때 적절한 이름이 출력된다.
아닌 경우, wrapper_decorator의 이름을 확인하게 되는데 크게 신경 쓸 필요는 없어 보임.

## 응용 : 함수의 동작 시간을 출력하는 데코레이터

```python
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
```

wrapper가 시간을 측정하기에, 함수의 성능을 확인하는 데코레이터를 작성할 수도 있음.

