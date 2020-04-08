number = int(input())
new = 0

count = 0


while(1):
   
    if (number) >= 10:
        first = number/10
        second = number%10
        new = first + 2 * second        
        count += 1
        if (new == number):
            print(count)
            break
        else:
            continue

    else:
        print(count+1)
        break
    



