from collections import deque
import sys
n,m = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(n)]
max_value = -sys.maxsize

dx = [-1,1,0,0]
dy = [0,0,-1,1]
alphabet = set()
distance = [[-1]*m for _ in range(n)]
def bfs(x,y):
    global alphabet
    que = deque()
    que.append((x,y))
    alphabet.update(graph[x][y])
    distance[x][y] = 0

    while que:
        x,y = que.popleft()
        temp_list = []
        for i in range(4):
            nx,ny = x + dx[i],y +dy[i]
            


            if nx <0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] not in alphabet and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                que.append((nx,ny))
                temp_list.append(graph[nx][ny])
        alphabet.update(temp_list)
        


bfs(0,0)
print(distance)
