n = int(input())
m = int(input())
error_list  = input().split()
cnt = abs(100 - n)

for i in range(1000001):
    for j in str(i):
        if j in error_list:
            break
    
    else:
        cnt = min(cnt,len(str(i)) + abs(i-n))
print(cnt)