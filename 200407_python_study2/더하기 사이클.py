n  = int(input())
tmp = n
count = 0


while(True):
   
    numbers = [tmp // 10, tmp % 10]
    tmp = (numbers[1] * 10) + (sum(numbers) % 10)
    count += 1
    if (tmp == n):
        break
           
print(count)

