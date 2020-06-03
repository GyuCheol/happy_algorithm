

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

while stack:
    # 맨마지막 요소를 지우면서 꺼냄 (stack pop)
    # 원래있던 순서가 뒤집어짐
    top = stack.pop()
    
    print(top)

