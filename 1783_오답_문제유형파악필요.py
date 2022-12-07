from collections import deque
n,m = map(int,input().split())

d = ((1,2),(2,1),(2,-1),(1,-2))

distance = [[False] * m for _ in range(n)]

def bfs(start_x,start_y):
    que = deque()
    que.append((start_x,start_y))
    distance[start_x][start_y] = True
    while que:
        for i in range(len(que)):
            x,y = que.popleft()
            for dx,dy in d:
                nx = x + dx
                ny = y + dy
                
                if nx <0 or nx >= n or ny <0  or ny >= m:
                    continue

                if distance[nx][ny] == False:
                    que.append((nx,ny))
                    distance[nx][ny] = True

bfs(0,0)
total = 0

for i in distance:
    total += sum(i)
print(total)
