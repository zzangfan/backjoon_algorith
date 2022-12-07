n = int(input())
A = 5 * 60
B = 60
C = 10
Timer = [A,B,C]
A_list = []

rest = 0
for i in Timer:
    
    count = n // i
    A_list.append(count)
    n -=  i * count

if n !=0:
    print(-1)
else:
    for i in A_list:
        print(i,end=' ')

