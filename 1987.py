from collections import deque
import sys
n,m = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(n)]
max_value = -sys.maxsize

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 1

def bfs(x,y):
    global answer
    que = set([(x,y,graph[x][y])])
    
  
   

    while que:
        x,y,ans = que.pop()

        answer = max(answer,len(ans))
        
        for i in range(4):
            nx,ny = x + dx[i],y +dy[i]
            


            if nx <0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] not in ans:
                que.add((nx,ny,ans+graph[nx][ny]))
               
                
          


bfs(0,0)
print(answer)
