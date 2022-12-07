N = int(input())

for _ in range(N):
    m,n,x,y = [int(i) for i in input().split()]
    ans = -1

    while x <= m*n:
        if (x-y) % n == 0:
            ans = x
            break
        x += m
    
    print(ans)