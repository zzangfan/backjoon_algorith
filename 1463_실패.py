n =int(input())

count = 0
dp = [0] 
while n != 1:

    for i in [3,2]:
        if (n-1)%i == 0 and (n- 1) != 0:
            n -= 1
            count +=1
            while n%i == 0:
                n = n//i
                
                count+=1
        elif n%i ==0:
            while n%i == 0:
                n = n//i
                
                count +=1

print(count)


