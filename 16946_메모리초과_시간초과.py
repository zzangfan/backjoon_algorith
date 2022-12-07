import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]
answer = [[0] * m for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    
    global count 
    
    for i in range(4):
        nx,ny = x + dx[i], y+dy[i]
        
        if nx < 0  or nx >= n or ny <0  or ny >=m:
            
            continue

        if graph[nx][ny] == 0 and answer[nx][ny] == 0:
            answer[nx][ny] = 1
            count += 1
            dfs(nx,ny)
            answer[nx][ny] = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            
            count = 1
            dfs(i,j)
            answer[i][j] = count%10
for i in answer:
    print("".join(map(str,i)))






