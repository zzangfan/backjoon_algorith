from collections import deque
import sys




def bfs(x,y):
    que = deque()
    que.append((x,y))

    visited[x][y] = 1
    cnt = 1

    while que:
        x,y = que.popleft()

        zeroes[x][y] = group

        for dx,dy in d:

            nx,ny = x + dx , y + dy

            if nx <0 or nx >= n or ny <0 or ny >=n:
                continue

            if visited[nx][ny]:
                continue

            if not graph[nx][ny]:

                que.append((nx,ny))
                visited[nx][ny] = 1

                cnt +=1

    return cnt

def find_cnt(x,y):

    data = set()
    for dx,dy in d:
        nx,ny = x + dx, y + dy
        
        if nx < 0 or nx >=n or ny < 0  or ny>=m:
            continue

        if not zeroes[nx][ny]:
            continue
        data.add(zeroes[nx][ny])

    cnt = 1

    for c in data:
        cnt += info[c]

        cnt %= 10

    return cnt
    

n,m = map(int,input().split())

graph = [[int(i) for i in input().strip()] for _ in range(n)]


visited = [[0] * m for _ in range(n)]

zeroes = [[0] * m for _ in range(n)]



group = 1

info = {}

d = ((-1,0),(1,0),(0,-1),(0,1))



for i in range(n):
    for j in range(m):
        if not graph[i][j] and not visited[i][j]:
            cnt = bfs(i,j)

            info[group] = cnt

            group +=1


answer = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):

        if graph[i][j]:

            answer[i][j] = find_cnt(i,j)

for i in range(n):
    print("".join(map(str,answer[i])))