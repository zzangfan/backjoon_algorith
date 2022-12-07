from sys import stdin
input = stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(fx,fy,sx,sy):
    check =[[[[-1] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    check[fx][fy][sx][sy] = 0
    que = deque()
    que.append([fx,fy,sx,sy])

    while que:
        fx,fy,sx,sy = que.popleft()

        if check[fx][fy][sx][sy] >= 10:
            break
        
        for i in range(4):
            nfx = fx + dx[i]
            nfy = fy + dy[i]
            nsx = sx + dx[i]
            nsy = sy + dy[i]

            if not (0 <= nfx < n and 0 <= nfy < m) and not (0 <= nsx < n and 0 <= nsy < m):
                continue

            if not (0 <= nfx < n  and 0 <= nfy < m):
                return check[fx][fy][sx][sy] + 1
                
            if not (0 <= nsx < n and 0 <= nsy < m):
                return check[fx][fy][sx][sy] + 1
            
            if graph[nfx][nfy] == '#':
                nfx = fx
                nfy = fy
            if graph[nsx][nsy] == '#':
                nsx = sx
                nsy = sy

            if check[nfx][nfy][nsx][nsy] == -1:
                check[nfx][nfy][nsx][nsy] = check[fx][fy][sx][sy] + 1
                que.append((nfx,nfy,nsx,nsy))
    return -1


n,m = map(int,input().split())
graph = []
flag = True
for i in range(n):
    graph.append(list(input().rstrip()))
    for j in range(m):
        if graph[i][j] == "o":
            if flag:
                fx,fy =i,j
                flag = False
            else:
                sx,sy = i,j

print(bfs(fx,fy,sx,sy))