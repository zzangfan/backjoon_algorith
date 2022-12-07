from collections import deque
import sys

input = sys.stdin.readline
N,K = map(int,input().split())
MAX = 10 ** 5
distance = [0] * (MAX+1)

def bfs(start):

    que = deque()
    que.append(start)
    
    while que:
        x = que.popleft()
        if x == K:
            print(distance[x])
            break

        for nx in (x -1, x + 1, x * 2):
            if 0 <= nx <= MAX and not distance[nx]:
                distance[nx] = distance[x] + 1
                que.append(nx)
        
bfs(N)

        

