from collections import deque
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

count = 0
fish_count = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            s_x,s_y = i,j
            graph[i][j] = 0
            continue
      
        if graph[i][j] == 0:
            count += 1
            continue
        
        if graph[i][j] != 0:
            fish_count += 1
            continue
print(fish_count)
if count == (n*n)-1:
    print(0)
    exit()

d = ((1,0),(-1,0),(0,1),(0,-1))

def bfs(x,y,fish_count):
    global graph
    que = deque()
    que.append((x,y,2,0))
    time = 1
    while que:

        for _ in range(len(que)):
            x,y,size,fish = que.popleft()
           
            for dx,dy in d:
                nx = dx + x
                ny = dy + y

                if nx < 0  or nx >= n or ny <0 or ny >=n:
                    continue

                if graph[nx][ny] == 0 :
                    que.appendleft((nx,ny,size,fish))
                    continue
                if graph[nx][ny] !=0 :
                    if graph[nx][ny] < size:
                        if size == fish + 1:
                            size +=1
                            fish = 0
                        graph[nx][ny] = 0 
                        fish_count -= 1
                        que.append((nx,ny,size,fish+1))
                        
                    elif graph[nx][ny] == size:
                        que.append((nx,ny,size,fish))
                        

                    elif graph[nx][ny] > size:
                        que.append((x,y,size,fish))
        print(graph)
        if fish_count == 0:
            return time        
        time +=1

    return time
print(bfs(s_x,s_y,fish_count))