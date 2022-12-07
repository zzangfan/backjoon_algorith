import sys

n,m=map(int,input().split())
graph=[[p for p in sys.stdin.readline().strip()] for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
flag = False
def dfs(x,y,cnt,color,sx,sy):
    global flag

    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]

        if flag is True:
            return
        if nx >=n  or nx <0  or ny>=m or ny <0:
            continue

        if cnt >=4 and sx ==nx and sy ==ny:
            flag = True
            return True

        if visited[nx][ny] == 0 and graph[nx][ny] == color:
            visited[nx][ny] = 1
            dfs(nx,ny,cnt+1,color,sx,sy)
            visited[nx][ny] = 0
    
    return False
def solve():
    global flag
    for i in range(n):
        for j in range(m):
            sx = i
            sy = j
            visited[sx][sy] = True
            dfs(i,j,1,graph[i][j],sx,sy)
            if flag:
                return "Yes"

    return "No"
print(solve())