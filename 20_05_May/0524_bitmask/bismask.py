

a = 0b0011 # 3
b = 0b0010 # 3

# and

print(a & b) # and 0b0010 = 2
print(a | b) # or  0b0011 = 3
print(a ^ b) # xor 0b0001 = 1

n = 0b1000
print(n << 1) # 0b0010 n * 2
print(n << 2) # 0b0100 n * (2^2) A << B = A * 2^B

# binary 2진 부호
# 근삿값 소수점..

print(n >> 1) # A / 2^B
# 1000 = 8
# 0100 = 4
# 0010 = 2
# 0001 = 1

# not
print(~a)

print('---------------------')

# 1 0001 << 2 = 0100

for bitmask in range(2**4):

    print(f'{bitmask:04b}')
    #if bitmask & (1 << 2) != 0:
    #    print('3번째 bit가 1')


