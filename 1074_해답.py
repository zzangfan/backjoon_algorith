n,r,c = map(int,input().split())

count = 0
def dfs(x,y,n):
    global count
  
    if n == 2:
        for i in range(x,x+n):
            for j in range(y,y+n):
                count +=1
                if i== r and j == c:
                    print(count)
                    exit()
        return
        
    if not (x<=r<x+n) and (y <= c < y + n):
        count += n*n
        return

    for i in range(x, x + n,n//2):
        for j in range(y, y+ n, n//2):
            dfs(i,j,n//2)

dfs(0,0,2**n)
