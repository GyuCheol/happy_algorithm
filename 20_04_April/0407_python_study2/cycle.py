number = tmp = int(input())
cycle = 0

while True:
    decimal = [tmp // 10, tmp % 10]
    tmp = (decimal[1] * 10) + (sum(decimal) % 10)
    cycle += 1

    if tmp == number:
        break

print(cycle)


