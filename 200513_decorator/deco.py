
import time

def timer(func):
    """Print the runtime of the decorated function"""
    
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


def do_twice(func):

    def wrapper():
        print('Before')
        func()
        func()
        print('After')

    return wrapper

@do_twice
def func():
    print("I'm an object")

@timer
def cook():
    print('cooking bread')


# python, javascript higher-order function 지원된다
# 다른 코딩 언어들은 함수가 고차함수가 아님.. (C/C++, C#, java)


# 함수에 데코레이터를 붙이면 동작이 확장이 됨!
# 함수 위에 다른 함수를 얹어서 기능을 확장함.

# 고차함수

# python object

# java / ECMA script

cook()



















# Sushi hub

# Aburi Sushi (SALMON 4pc)
# Nigiri Sushi (SALMON 4pc, TORO 4pc, TAMAGO 2pc)

