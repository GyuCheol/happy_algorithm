
# No paint, No class
# 냥3

class Animal:

    def __hash__(self):
        return 15151

    # 추상 클래스 (명세만 있고, 구현은 없는 클래스)
    # 말하는 동작만 추상적으로 제공, 자식클래스가 꼭 구현해야함!
    def speak(self):
        raise NotImplementedError

class Cat(Animal):

    def speak(self):
        print('meoooooow')

class Human(object):

    def __init__(self):
        self.age = 0
        self.name = ''
        self.weight = 0
        self.height = 0

    # override 덮어쓰기?
    # 부모 클래스의 동작을 현재 클래스가 구현한대로 바꿔버림.
    def __repr__(self):
        return self.name

    def __len__(self):
        return self.height
    
    # 가변인자
    def __call__(self, *input, **kwargs):
        print(input)
    
    # operataor overloading
    def __eq__(self, b):
        return self.height == b.height
    
    # 이 함수를 override해야 dict의 key가 될 수 있음.
    def __hash__(self):
        return hash(f'{self.name}_{self.height}')

def sum(a, b):
    return a + b

def sum2(*input):
    print(input)

def sum3(**kwargs):
    print(kwargs)

l = [1, 2, 3]
a = Human()
b = Human()

a.name = 'A'
b.name = 'Z'
a.height = 168 # 헐
b.height = 168

d = {}

d[a] = 1000000

print(a == b)
print(hash(a))
print(hash(b))
# false
# false

print(a)
print(len(a))
print(len(l))
# 해당 개체의 __repr__ 함수를 호출해서 어떻게 묘사되는지 보여줄뿐
# print함수와 object간에 __repr__이 함수를 이용한 것이라고 이해할 수 있음.

# 1. 오류가 난다.
# 2. A가 출력된다.
# 3. <object human>... 어쩌고가 출력된다.
# 4. 알 수 없는 type이라고 나온다.

# 다형성을 통해서, 개체의 동작을 통합

