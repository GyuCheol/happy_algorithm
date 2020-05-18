

def func(a, b=1, c=1):
    print(a + b + c)

func(1)         # 1 (1, 1, 1)
func(1, 2)      # 2 (1, 2, 1)
func(1, 2, 3)   # 3 (1, 2, 3)
# func()          # 4 
func(1, c=100)


def func2(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

# func2(1, 2, 3, 4, 5, 6)

# 가변 인자 (명확히 정해지지 않은 인자)

def func3(*tuple):
    pass

def func4(**kwds):
    for k in kwds:
        print(k)

func3(1, 2, 3, 4, 5, 6, 7, 8) # tuple -> (1, 2, 3, 4, 5, 6, 7, 8)
func3(1, 2, 3)
func3()

func4(a=1, b=2, c=3, d=4) # dict -> {'a'=1, 'b'=2, 'c'=3, 'd'=4}

d = {
    'end':'@@@@'
}

print('asdasd', **d)
