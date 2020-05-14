

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

def do_twice_with_output(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
        
    return wrapper_do_twice

@my_decorator
def say_whee():
    print("Whee!")

@do_twice
def say_my_name(name):
    print(name)

say_whee()

say_my_name('A')

print(say_whee)
