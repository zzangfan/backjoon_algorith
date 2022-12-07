from collections import deque
import sys
min_value = sys.maxsize
n = int(input())
distance = [[-1] * n for _ in range(n)]
dcr = [(-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)]
sr,sc,er,ec = map(int,input().split())

def bfs(sr,sc):

    que = deque()
    que.append((sr,sc))
    distance[sr][sc] = 0

    while que:
        r,c = que.popleft()
        for i in dcr:
            dr,dc = i
            nr = dr + r
            nc = dc + c

            if nr < 0 or nr >= n  or nc <0 or nc >=n:
                continue

            if distance[nr][nc] == -1:
                que.append((nr,nc))
                distance[nr][nc] = distance[r][c] + 1
bfs(sr,sc)
print(distance[er][ec])
