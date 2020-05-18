ca = input()
new = []
for c in ca:
    if (c =='A'):
        print('X', end='')
    elif (c == 'B'):
        print('Y', end='')
    elif (c == 'C'):
        print('Z', end='')
    else:
        print(chr(ord(c)-3), end='')

    #a,b,c처리
###
# 1) ASCII
# 2) 알파벳 순서 배열 제공
for c in ca:
    if (c <='C'):
        print(chr(ord(c)-3) + 26, end='')
    else:
        print(chr(ord(c)-3), end='')

###

# computer : A
# combine : B

# compute > combine
# apple < orange
