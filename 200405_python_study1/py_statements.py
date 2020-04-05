
def foo():
    print('a')
    return 1

def bar():
    print('b')
    return 2

a, b = 0, 0

a, b = foo(), bar()
