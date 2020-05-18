
class Cat(object):

    # 사물이 가지는 상태 Property
    # 사물이 가지는 행동 Method

    # 생성자(Constructor)
    # Class의 명세를 메모리에 할당하는 함수
    # self는 현재 다루고 있는 object를 뜻함
    
    def __init__(self):
        self.weight = 0
        self.height = 0
        self.hungry = 0
        self.BMI = 0
    
    def eat(self, food):
        self.hungry -= 1
        self.weight += 1
    
    def sleep(self):
        self.weight += 1


# instance / object
lovely = Cat()
meow = Cat()

lovely.eat('츄르')

print(lovely.weight)

