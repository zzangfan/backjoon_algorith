from collections import deque
import sys
#distnace을 최대갓으로 난후 최솟값을 구하는 문제다
#대부분 bfs문제는 최솟값을 더하는 식이였는데 이런 문제도 있다니 신기하다.
input = sys.stdin.readline
d = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs():
    check = [[float('inf')] * W  for _ in range(H)]
    check[sr][sc] = -1
    que = deque([(sr,sc)])
    while que:
        x,y = que.popleft()
        if (x,y) == (gr, gc):
            return check[gr][gc]
        
        for dx,dy in d:
            nx = x + dx
            ny = y + dy

            while True:
                if not (0<=nx< H and 0 <=ny <W):
                    break
                if A[nx][ny] == '*':
                    break
                if check[nx][ny] < check[x][y] + 1:
                    break
                que.append((nx,ny))
                check[nx][ny] = check[x][y] + 1
                nx += dx
                ny += dy




W,H = map(int,input().split())
A, C = [], []
sr, sc, gr, gc = 0, 0, 0, 0
for i in range(H):
    A.append(list(input().strip()))
    for j in range(W):
       if A[i][j] == "C":
        C.append((i,j))

(sr, sc), (gr, gc) = C
print(bfs())
        