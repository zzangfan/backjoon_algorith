from collections import deque

N,K = map(int,input().split())

distance = [0] * 100001
move = [0] * 100001
def path(x):
    arr = []
    temp = x
    for _ in range(distance[x] + 1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str,arr[::-1])))


def bfs():

    que = deque()
    que.append(N)

    while que:
        x = que.popleft()
        
        if x == K:
            print(distance[x])
            path(x)
            return x

        for nx in (x + 1, x - 1, 2 * x):
            
            if 0 <= nx <= 100000  and distance[nx] == 0:
               
                
                que.append(nx)
                distance[nx] = distance[x] + 1
                move[nx] = x

bfs()
