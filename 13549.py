from collections import deque
import sys

intput = sys.stdin.readline

N,K = map(int,input().split())

distance = [-1] * 100001
distance[N] = 0

dx = [-1,1,2]

def bfs():

    que = deque()
    que.append(N)

    while que:
        x = que.popleft()
        
        if x == K:
            print(distance[x])
            return 
        for nx in (x + 1, x - 1, x * 2):

            
            if 0 <= nx <= 100000  and distance[nx] == -1 :
                             
                
                if nx == x * 2:
                    distance[nx] = distance[x]
                    que.appendleft(nx)
                else:
                    distance[nx] = distance[x] + 1
                    que.append(nx)
bfs()